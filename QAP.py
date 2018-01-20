class Qap:
	def __init__(self, path):
		self.solution_size = self.__get_solution_size(path)
		self.solution = self.generate_solution()
		self.mat_locations = self.__generate_locations(path)
		self.mat_facilities = self.__generate_facilities(path)
		self.deltas = self.__init_deltas()

	def generate_solution(self):
		"""
		:return: an array with a solution
		"""
		solution = []

		for i in range(0, self.solution_size):
			solution.append(i)

		# Solution of test
		# return [4,2,1,9,7,3,0,8,6,5]
		# return [1,6,7,0,8,3,5,4,2,9]
		return solution

	def to_string(self):
		res = ''
		for i in range(0, int(self.solution_size)):
			res += str(self.solution[i]) + '-'

		return res[:-1]

	def __get_solution_size(self, path):
		"""
		:param path: path of file
		:type path: str
		:return: size of the solution read in file
		"""
		with open(path, "r") as f:
			return int(f.readline().split(" ")[1])

	def __generate_locations(self, path):
		"""
		:return: a matrix with locations load in a file
		"""
		with open(path, "r") as f:
			data = f.readlines()

		i_line = 0
		locations = []
		for line in data:
			if i_line in range(1, self.solution_size + 1):
				locations.append(list(map(int, line[:-1].split(sep=" ", maxsplit=self.solution_size - 1))))
			i_line = i_line + 1

		return locations

	def __generate_facilities(self, path):
		"""
		:return: a matrix with facilities load in a file
		"""
		with open(path, "r") as f:
			data = f.readlines()

		i_line = 0
		facilities = []
		for line in data:
			if i_line in range(self.solution_size + 2, (self.solution_size * 2) + 2):
				facilities.append(list(map(int, line[:-1].split(sep=" ", maxsplit=self.solution_size - 1))))
			i_line = i_line + 1

		return facilities

	def __init_deltas(self):
		"""
		:return: an initialized matrix with computed deltas
		"""
		deltas = []
		for i in range(self.solution_size):
			delta_l = []
			for j in range(self.solution_size):
				delta_l.append(self.compute_delta(i, j))
			deltas.append(delta_l)

		return deltas

	def full_eval(self):
		"""
		:return: full evaluation of the solution
		:note : A = mat_locations
				B = mat_facilities
		"""
		cost = 0

		for i in range(self.solution_size):
			for j in range(self.solution_size):
				cost = cost + self.mat_locations[i][j] * self.mat_facilities[self.solution[i]][self.solution[j]]

		return cost

	def compute_delta(self, i, j):
		"""
		:param i: index to swap
		:param j: index to swap
		:type i: int
		:type j: int
		:return: Incremental evaluation for a swap of i and j ( Complexity: O(n) )
		"""
		delta = (self.mat_locations[i][i] - self.mat_locations[j][j]) \
		        * (self.mat_facilities[self.solution[j]][self.solution[j]]
		           - self.mat_facilities[self.solution[i]][self.solution[i]]) \
		        + \
		        (self.mat_locations[i][j] - self.mat_locations[j][i]) \
		        * (self.mat_facilities[self.solution[j]][self.solution[i]]
		           - self.mat_facilities[self.solution[i]][self.solution[j]])

		for k in range(self.solution_size):
			if k not in [i, j]:
				delta = delta + (self.mat_locations[k][i] - self.mat_locations[k][j]) \
				                * (self.mat_facilities[self.solution[k]][self.solution[j]]
				                   - self.mat_facilities[self.solution[k]][self.solution[i]]) \
				        + \
				        (self.mat_locations[i][k] - self.mat_locations[j][k]) \
				        * (self.mat_facilities[self.solution[j]][self.solution[k]]
				           - self.mat_facilities[self.solution[i]][self.solution[k]])

		return delta

	def compute_delta_fast(self, delta, mother_i, mother_j, i, j):
		"""
		 For ex. see E. Taillard, "COMPARISON OF ITERATIVE SEARCHES FOR THE QUADRATIC ASSIGNMENT PROBLEM",
		 ECOLE PLOYTECHNIQUE FÉDÉRALE DE LAUSANNE (EPFL), 1994.

		:param mother_i: index of previous swap
		:param mother_j: index of previous swap
		:param i: index to swap
		:param j: index to swap
		:param delta: previous delta compute for the swap of i and j
		:type mother_i: int
		:type mother_j: int
		:type i: int
		:type j: int
		:type delta: int
		:return: double incremental evaluation for a swap of i2 and j2 after i and j
		"""

		if (mother_i == -1) & (mother_j == -1):  # specific to OR API, the API return -1 if it don't know mother i and mother j
			return self.compute_delta(i=i, j=j)
		elif (mother_i == i) & (mother_j == j):
			return -delta
		elif (i == mother_i) | (i == mother_j) | (j == mother_i) | (j == mother_j):
			return self.compute_delta(i=i, j=j)
		else:
			# grp1 = (self.mat_locations[mother_i][i]
			#         - self.mat_locations[mother_i][j]
			#         + self.mat_locations[mother_j][j]
			#         - self.mat_locations[mother_j][i])
			# grp2 = (self.mat_facilities[self.solution[mother_j]][self.solution[i]]
			#         - self.mat_facilities[self.solution[mother_j]][self.solution[j]]
			#         + self.mat_facilities[self.solution[mother_i]][self.solution[j]]
			#         - self.mat_facilities[self.solution[mother_i]][self.solution[i]])
			# grp3 = (self.mat_locations[i][mother_i]
			#         - self.mat_locations[j][mother_i]
			#         + self.mat_locations[j][mother_j]
			#         - self.mat_locations[i][mother_j])
			# grp4 = (self.mat_facilities[self.solution[i]][self.solution[mother_j]]
			#         - self.mat_facilities[self.solution[j]][self.solution[mother_j]]
			#         + self.mat_facilities[self.solution[j]][self.solution[mother_i]]
			#         - self.mat_facilities[self.solution[i]][self.solution[mother_i]])
			#
			# print("debug = " + str(delta) + "+" + str(grp1) + "*" + str(grp2) + "+" + str(grp3) + "*" + str(grp4))
			# return delta + grp1 * grp2 + grp3 * grp4
			return (delta
			        + (self.mat_locations[mother_i][i]
			           - self.mat_locations[mother_i][j]
			           + self.mat_locations[mother_j][j]
			           - self.mat_locations[mother_j][i])
			        * (self.mat_facilities[self.solution[mother_j]][self.solution[i]]
			           - self.mat_facilities[self.solution[mother_j]][self.solution[j]]
			           + self.mat_facilities[self.solution[mother_i]][self.solution[j]]
			           - self.mat_facilities[self.solution[mother_i]][self.solution[i]])
			        + (self.mat_locations[i][mother_i]
			           - self.mat_locations[j][mother_i]
			           + self.mat_locations[j][mother_j]
			           - self.mat_locations[i][mother_j])
			        * (self.mat_facilities[self.solution[i]][self.solution[mother_j]]
			           - self.mat_facilities[self.solution[j]][self.solution[mother_j]]
			           + self.mat_facilities[self.solution[j]][self.solution[mother_i]]
			           - self.mat_facilities[self.solution[i]][self.solution[mother_i]])
			        )

	def swap_solution(self, i, j):
		"""
		:param i: item index of the solution
		:param j: item index of the solution
		:return: Swap two items of the solution1
		"""
		tmp = self.solution[i]
		self.solution[i] = self.solution[j]
		self.solution[j] = tmp

	def update_solution(self, new_solution):
		"""
		:param new_solution: new solution to update
		:type new_solution: str
		:return: update the solution
		"""
		tmp = new_solution.split("-")
		for i in range(len(tmp)):
			self.solution[i] = int(tmp[i])
