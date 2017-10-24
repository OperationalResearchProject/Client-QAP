from QAP import Qap


qap = Qap(10)
print("Test incremental evaluation")

fitness = qap.full_eval()

for i in range(qap.solution_size):
	for j in range(qap.solution_size):

		# compute with delta matrix (incremental evaluation)
		qap.deltas[i][j] = qap.compute_delta(i, j)
		fitij = fitness + qap.deltas[i][j]

		# compute without delta
		qap.swap_solution(i, j)
		fitij_full = qap.full_eval()
		qap.swap_solution(i, j)

		if fitij_full != fitij:
			print("Error ! ")
			print("fitness full = " + str(fitij_full))
			print("fitness ij = " + str(fitij))


print("Incremental Evaluation test is ended")
