from QAP import Qap


qap = Qap(10)
test_incremental_eval = True
test_double_incremental_eval = True

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

		# Test if the full evaluation of the solution is equal to the simple incremental evaluation
		if fitij_full != fitij:
			test_incremental_eval = False
			print("Error ! ")
			print("fitness full = " + str(fitij_full))
			print("fitness ij = " + str(fitij))


print("All test of incremental evaluation are passed : " + str(test_incremental_eval))
