class Matrix:
    def __init__(self, matrix=()):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(" ".join(str(value) for value in row) for row in self.matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        result = []
        for i in range(len(self.matrix)):
            row_result = []
            if len(self.matrix[i]) != len(other.matrix[i]):
                raise ValueError
            for j in range(len(self.matrix[i])):
                row_result.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row_result)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        if isinstance(other, (int, float)):
            for row in self.matrix:
                row_result = []
                for value in row:
                    row_result.append(value * other)
                result.append(row_result)
        elif isinstance(other, Matrix):
            for i in range(len(self.matrix)):
                row = self.matrix[i]
                if len(row) != len(other.matrix):
                    raise ValueError
                row_result = []
                for j in range(len(other.matrix[i])):
                    value_result = 0
                    for k in range(len(row)):
                        value_result += (row[k] * other.matrix[k][j])
                    row_result.append(value_result)
                result.append(row_result)
        else:
            raise TypeError
        return Matrix(result)

    @classmethod
    def num(cls, s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    @classmethod
    def factory(cls, ordinal=""):
        ordinal = str(" " + ordinal + " ").replace("  ", " ")
        size = int(input(f"Enter size of{ordinal}matrix:\n")[0])
        print(f"Enter{ordinal}matrix:")
        return Matrix([[Matrix.num(i) for i in input().split()] for _ in range(size)])


def user_input():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
    s = input("Your choice: ")
    if s == "1" or s == "3":
        matrix_1 = Matrix.factory("first")
        matrix_2 = Matrix.factory("second")
        if s == "1":
            return matrix_1 + matrix_2
        else:
            return matrix_1 * matrix_2
    elif s == "2":
        matrix = Matrix.factory()
        c = Matrix.num(input("Enter constant: "))
        return matrix * c
    elif s == "0":
        return False
    return True


a = True
while a:
    try:
        a = user_input()
        print("The result is:", a, sep="\n")
    except (ValueError, TypeError, IndexError, AttributeError):
        print("The operation cannot be performed.")
