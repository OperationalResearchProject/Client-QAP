class Qap:
    def __init__(self, solution_size):
        self.solution_size = solution_size
        self.mat_locations = self.__generate_locations()
        self.mat_facilities = self.__generate_facilities()
        self.solution = self.generate_solution()

    def generate_solution(self):
        """
        :return: an array with a solution
        """
        solution = []

        for i in range(0, self.solution_size):
            solution.append(i)

        # Solution of test
        # return [4,2,1,9,7,3,0,8,6,5]
        return solution

    def __generate_locations(self):
        """
        :return: a matrix with locations load in a file
        """
        with open("test.txt", "r") as f:
            data = f.readlines()

        i_line = 0
        locations = []
        for line in data:
            if i_line in range(1, self.solution_size + 1):
                locations.append(list(map(int, line[:-1].split(sep=" ", maxsplit=self.solution_size - 1))))
            i_line = i_line + 1

        return locations

    def __generate_facilities(self):
        """
        :return: a matrix with facilities load in a file
        """
        with open("test.txt", "r") as f:
            data = f.readlines()

        i_line = 0
        facilities = []
        for line in data:
            if i_line in range(self.solution_size + 2, (self.solution_size*2) + 2):
                facilities.append(list(map(int, line[:-1].split(sep=" ", maxsplit=self.solution_size - 1))))
            i_line = i_line + 1

        return facilities

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
                   - self.mat_facilities[self.solution[i]][self.solution[i]])\
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

    def compute_delta_fast(self, delta, i, j, i2, j2):
        """
         For ex. see E. Taillard, "COMPARISON OF ITERATIVE SEARCHES FOR THE QUADRATIC ASSIGNMENT PROBLEM",
         ECOLE PLOYTECHNIQUE FÉDÉRALE DE LAUSANNE (EPFL), 1994.

        :param i: index of previous swap
        :param j: index of previous swap
        :param i2: index to swap
        :param j2: index to swap
        :param delta: previous delta compute for the swap of i and j
        :type i: int
        :type j: int
        :type i2: int
        :type j2: int
        :type delta: int
        :return: double incremental evaluation for a swap of i2 and j2 after i and j
        """

        if i == i2 & j == j2:
            return -delta
        elif i2 == i | i2 == j | j2 == i | j2 == j:
            return self.compute_delta(i=i2, j=j2)
        else:
            return (delta
                    + (self.mat_locations[i][i2]
                       - self.mat_locations[i][j2]
                       + self.mat_locations[j][j2]
                       - self.mat_locations[j][i2])
                    * (self.mat_facilities[self.solution[j]][self.solution[i2]]
                       - self.mat_facilities[self.solution[j]][self.solution[j2]]
                       + self.mat_facilities[self.solution[i]][self.solution[j2]]
                       - self.mat_facilities[self.solution[i]][self.solution[i2]])
                    + (self.mat_locations[i2][i]
                       - self.mat_locations[j2][i]
                       + self.mat_locations[j2][j]
                       - self.mat_locations[i2][j])
                    * (self.mat_facilities[self.solution[i2]][self.solution[j]]
                       - self.mat_facilities[self.solution[j2]][self.solution[j]]
                       + self.mat_facilities[self.solution[j2]][self.solution[i]]
                       - self.mat_facilities[self.solution[i2]][self.solution[i]])
                    )


q = Qap(10)
print(q.compute_delta(3, 8))
