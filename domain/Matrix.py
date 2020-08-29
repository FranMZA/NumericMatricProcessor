class Matrix:
    def __init__(self, dim, values):
        self.dim = tuple(dim)
        self.values = values

    def __str__(self) -> str:
        matrix_string = ""
        for row_index in range(self.dim[0]):
            matrix_string += f"{' '.join(str(el) for el in self.values[row_index])}\n"
        return matrix_string

    def __add__(self, other):
        self.dim_validator(other)

        new_matrix_values = list()
        for row_index in range(self.dim[0]):
            row = list()
            for col_index in range(self.dim[1]):
                row.append(self.values[row_index][col_index] + other.values[row_index][col_index])
            new_matrix_values.append(row)
        return Matrix(self.dim, new_matrix_values)

    def __neg__(self):
        neg_matrix_values = list()
        for row in self.values:
            neg_matrix_values.append([-element for element in row])
        return Matrix(self.dim, neg_matrix_values)

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, constant):
        new_matrix_values = list()
        for row in self.values:
            new_matrix_values.append([element * constant for element in row])
        return Matrix(self.dim, new_matrix_values)

    def __rmul__(self, constant):
        return self.__mul__(constant)

    def dim_validator(self, other):
        if self.dim != other.dim:
            raise IndexError('Dimensions of the matrices are different')
        else:
            return None
