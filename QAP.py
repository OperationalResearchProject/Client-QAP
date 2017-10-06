class Qap:
    def __init__(self, solution_size):
        self.mat_locations = self.__generate_locations()
        self.mat_facilities = self.__generate_facilities()
        self.solution = self.generate_solution(solution_size=solution_size)

    def generate_solution(self, solution_size):
        solution = ""

        for i in range(0, solution_size):
            solution += str(i) + "-"

        return solution[:-1]

    @staticmethod
    def __generate_locations():

        with open("test.txt", "r") as f:
            data = f.readlines()

        i_line = 0
        locations = []
        for line in data:
            if i_line in range(1, 31):
                locations.append(list(map(int, line[:-1].split(sep=" ", maxsplit=29))))
            i_line = i_line + 1

        return locations

    @staticmethod
    def __generate_facilities():
        with open("test.txt", "r") as f:
            data = f.readlines()

        i_line = 0
        facilities = []
        for line in data:
            if i_line in range(32, 62):
                facilities.append(list(map(int, line[:-1].split(sep=" ", maxsplit=29))))
            i_line = i_line + 1

        return facilities


q = Qap(10)
print(q.mat_locations)
