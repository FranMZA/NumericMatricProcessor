class MatrixBuilder:
    def build(self, m_dim=None, m_val=None):
        print(f'{m_dim}')
        dim_matrix = self.dim_input()
        print(f'{m_val}')
        values = list()
        for row_index in range(dim_matrix[0]):
            values.append(self.row_input(dim_matrix[1]))
        return dim_matrix, values

    @staticmethod
    def dim_input():
        # check if dims are positive integers
        dims = [int(dim) for dim in input().split()]
        if len(dims) != 2:
            raise IndexError('Wrong number of dimensions')
        for i in range(len(dims)):
            if dims[i] <= 0:
                dims[i] = 1
        return dims

    @staticmethod
    def row_input(num_cols):
        # check if the row has the correct number of elements
        # num elements given by dim_matrix[1] (num of columns)
        row = [float(num) for num in input().split()]
        if len(row) != num_cols:
            if len(row) > num_cols:
                raise IndexError('Length of row is bigger than dimension of matrix')
            else:
                raise IndexError('Length of row is smaller than dimension of matrix')
        return row
