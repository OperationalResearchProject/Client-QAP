from QAP import Qap


qap = Qap(10)
test_incremental_eval = True
test_delta_matrix_value = True
test_double_incremental_eval = True

fitness = qap.full_eval()

for i in range(qap.solution_size):
	for j in range(qap.solution_size):

		# compute with delta matrix (incremental evaluation)
		d_computed = qap.compute_delta(i, j)
		fitij = fitness + d_computed

		if d_computed != qap.deltas[i][j]:
			test_delta_matrix_value = False

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


print("Test of incremental evaluation : " + str(test_incremental_eval))
print("Test of delta matrix values : " + str(test_delta_matrix_value))
