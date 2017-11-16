import sys
import getopt

import grpc
from QAP import Qap
from protoGenerated import tabousearch_pb2_grpc
from protoGenerated import messages_pb2


def main(argv):
	qap = Qap("test.txt")
	server = '127.0.0.1:50051'
	print("Connection to serveur " + server)

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
	qap.solution = [4, 2, 1, 9, 7, 3, 0, 8, 6, 5]
	qap.swap_solution(3, 8)
	move_init = qap.compute_delta(3, 8)
	fitness_init = qap.full_eval()

	print("full 3-8 : " + str(fitness_init))
	print("move 3-8 : " + str(move_init))
	print("sol  3-8 : " + qap.to_string())
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

		# todo : si c'est la meme mother_solution qu'avant, faut remettre un backup de delta ???
		# todo : (car delta est modifié à chaque fois)
		for j in range(0, len(response.solutions)):
			# solution have to be updated with the mother solution
			if j == 0:
				qap.update_solution(response.solutions[j].mother_solution)

			# swap and compute the solution with simple incremental evaluation
			qap.swap_solution(response.solutions[j].i, response.solutions[j].j)
			delta = qap.compute_delta(response.solutions[j].i, response.solutions[j].j)
			delta2 = qap.compute_delta_fast(delta=qap.deltas[response.solutions[j].i][response.solutions[j].j],
			                                i=response.solutions[j].mother_i,
			                                j=response.solutions[j].mother_j,
			                                i2=response.solutions[j].i,
			                                j2=response.solutions[j].j)

			# Debug print
			dfull = qap.full_eval()
			dsimple = response.solutions[j].mother_fitness - delta
			ddouble = response.solutions[j].mother_fitness - delta2
			print("full == " + str(dfull))
			print("delt == " + str(dsimple))
			print("delt2 = " + str(ddouble))

			if (dfull != ddouble) & (dfull != dsimple): # dfull is good (checked with c++ code)
				# todo : chercher un random dans le code server sinon peut-etre que les tableau ne sont pas dans le bon ordre
				# todo : semble exploser quand i = 0, j = 1, mother_i = 1 et mother_j = 3

				# todo : test en enlevant delta2 et essayer de reproduire le bug
				print("iteration i = " + str(i))
				print("curent sol = " + str(qap.to_string()))
				print("delta = " + str(delta))
				print("delta2 = " + str(delta2))
				print("del old = " + str(qap.deltas[response.solutions[j].i][response.solutions[j].j]))
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
