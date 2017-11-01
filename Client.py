import sys
import getopt

import grpc
from QAP import Qap
from protoGenerated import tabousearch_pb2_grpc
from protoGenerated import messages_pb2


def main(argv):
	qap = Qap(10)
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

	for i in range(1000):
		fitnesses = []

		for j in range(0, len(response.solutions)):
			# swap and compute the solution
			qap.swap_solution(response.solutions[j].i, response.solutions[j].j)
			# delta = qap.compute_delta(response.solutions[j].i, response.solutions[j].j)
			#
			# # update deltas matrix after each compute delta
			# qap.deltas[response.solutions[j].i][response.solutions[j].j] = delta

			fitnesses.append(qap.full_eval())  # todo : send fitness and not move ! delta + mother_fitness

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
