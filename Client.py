import sys
import getopt
import Config

import grpc
from QAP import Qap
from protoGenerated import tabousearch_pb2_grpc
from protoGenerated import messages_pb2


def main(argv):
	qap = Qap(Config.qap_file)
	server = Config.server + ":" + Config.port
	print("Connection to server " + server)

	channel = grpc.insecure_channel(server)

	try:
		opts, args = getopt.getopt(argv, "ht", ["hillclimber", "tabousearch"])
	except getopt.GetoptError:
		print("Error :")
		print("\tuse -h or --hillclimber to use hillclimber algorithm")
		print("\tuse -t or --tabousearch to use tabousearch algorithm")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--hillclimber"):
			print("\nHillClimber process is not yet implemented......")

		elif opt in ("-t", "--tabousearch"):
			print("\nTabou Search process is started......")
			process_ts(channel=channel, qap=qap)


def process_ts(channel, qap):
	stub = tabousearch_pb2_grpc.TabouSearchServiceStub(channel=channel)

	# Init solution for test
	qap.solution = [4, 2, 1, 9, 7, 3, 0, 8, 6, 5]  # todo : remove after debug
	qap.swap_solution(3, 8)  # todo : remove after debug
	move_init = qap.compute_delta(3, 8)  # todo : remove after debug
	fitness_init = qap.full_eval()  # todo : remove after debug

	print("full_ 3-8 : " + str(fitness_init))  # todo : remove after debug
	print("delta 3-8 : " + str(move_init))  # todo : remove after debug
	print("sol_  3-8 : " + qap.to_string())  # todo : remove after debug
	print()

	# Initialisation of the transaction
	response = stub.InitTransaction(messages_pb2.InitTransactionRequest(
			customer='Client-QAP-Test',
			solutionSize=qap.solution_size,
			type="qap",
			fitness=fitness_init,
			solution=qap.to_string()
	))

	for i in range(10):
		fitnesses = []

		for j in range(0, len(response.solutions)):
			# solution have to be updated with the mother solution
			if j == 0:
				qap.update_solution(response.solutions[j].mother_solution)

			# swap and compute the solution with simple incremental evaluation
			qap.swap_solution(response.solutions[j].i, response.solutions[j].j)
			delta = qap.compute_delta(response.solutions[j].i, response.solutions[j].j)
			delta2 = qap.compute_delta_fast(delta=qap.deltas[response.solutions[j].i][response.solutions[j].j],
			                                mother_i=response.solutions[j].mother_i,
			                                mother_j=response.solutions[j].mother_j,
			                                i=response.solutions[j].i,
			                                j=response.solutions[j].j)

			# Debug print
			dfull = qap.full_eval()
			dsimple = response.solutions[j].mother_fitness - delta
			ddouble = response.solutions[j].mother_fitness - delta2

			print("computed delta["+str(response.solutions[j].i)+"]["+str(response.solutions[j].j)+"] = "+str(delta))
			print("computed delta2["+str(response.solutions[j].i)+"]["+str(response.solutions[j].j)+"] = "+str(delta2))

			if delta != delta2:  # todo : the problem is delta2
				#  todo : the problem is the previous delta value or the compute value ??
				print("\n\n =============== DEBUG : ================")
				print("iteration n° " + str(i)+"/10")
				print("current solution = " + str(qap.to_string()))
				print("fitness mother = " + str(response.solutions[j].mother_fitness))  # fitness of mother solution
				print("delta simple / delta double = " + str(delta) + " / " + str(delta2))
				print("fitness full   = " + str(dfull))    # full evaluation
				print("fitness simple = " + str(dsimple))  # simple incremental eval
				print("fitness double = " + str(ddouble))  # double incremental eval

				print("\nSolution received :")
				print(response.solutions[j])

				raise ValueError('The fitness seems to be bad.')
			print()

			# update deltas matrix after each compute delta
			qap.deltas[response.solutions[j].i][response.solutions[j].j] = delta2

			# prepare fitnesses array to send
			fitnesses.append(response.solutions[j].mother_fitness - delta2)

			# swap solution to reset
			qap.swap_solution(response.solutions[j].i, response.solutions[j].j)

		# send fitness
		mess = messages_pb2.MultiFitnessRequest(
				id=response.id,
				fitnesses=fitnesses
		)

		# send solutions
		for s in response.solutions:
			sol = mess.solutions.add()
			sol.i = s.i
			sol.j = s.j
			sol.mother_solution = s.mother_solution

		response = stub.SendFitness(mess)

	stop = stub.StopTransaction(messages_pb2.StopRequest(id=response.id, message='done'))
	print("Tabou Search process is finished, the best solution find for this transaction is ")
	print(stop)


if __name__ == "__main__":
	main(sys.argv[1:])
