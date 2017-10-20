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

	# Initialisation of the transaction
	response = stub.InitTransaction(messages_pb2.InitTransactionRequest(
			customer='Client-QAP-Test',
			solutionSize=qap.solution_size,
			type="qap",
			fitness=9999999999,
			solution=qap.to_string()
	))

	print(response)


if __name__ == "__main__":
	main(sys.argv[1:])
