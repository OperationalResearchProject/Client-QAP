from QAP import Qap


qap = Qap(10)
test_incremental_eval = True
test_delta_matrix_value = True
test_double_incremental_eval = True

fitness = qap.full_eval()

for i in range(1, qap.solution_size):
	for j in range(0, i):

		# compute with delta matrix (incremental evaluation)
		d_computed = qap.compute_delta(i, j)
		qap.deltas[i][j] = d_computed
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


delta_ij = 0
delta_ij_full = 0

for i_previous in range(1, qap.solution_size):
	for j_previous in range(0, i_previous):
		qap.swap_solution(i_previous, j_previous)

		for i in range(1, qap.solution_size):
			for j in range(0, i):
				delta_ij_full = qap.compute_delta(i, j)
				delta_ij = qap.compute_delta_fast(qap.deltas[i][j], i_previous, j_previous, i, j)

				if delta_ij_full != delta_ij:
					test_double_incremental_eval = False
					print(str(delta_ij_full) + " == " + str(delta_ij))

		qap.swap_solution(j_previous, i_previous)


print("Test of incremental evaluation : " + str(test_incremental_eval))
print("Test of delta matrix values : " + str(test_delta_matrix_value))
print("Test of double incremental evaluation : " + str(test_double_incremental_eval))
