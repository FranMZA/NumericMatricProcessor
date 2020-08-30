from domain.Matrix import Matrix
from domain.MatrixBuilder import MatrixBuilder


class Main:
    def __init__(self):
        self.state = True
        self.option = -1
        self.builder = MatrixBuilder()

    def main(self):
        while self.state:
            print('1. Add matrices\n'
                  '2. Multiply matrix by a constant\n'
                  '3. Multiply matrices\n'
                  '0. Exit')

            self.option = input('Your choice:').strip()

            if self.option == '1':
                self.matrix_addition()
                continue
            elif self.option == '2':
                self.matrix_prod_constant()
                continue
            elif self.option == '3':
                self.matrix_mat_prod()
                continue
            elif self.option == '0':
                self.state = False
                continue

    def matrix_addition(self):
        matrices = self.matrix_list()
        print('The result is:')
        print(matrices[0] + matrices[1])

    def matrix_prod_constant(self):
        message_dim = 'Enter size of matrix:'
        message_val = 'Enter matrix:'
        matrix = Matrix(*self.builder.build(message_dim, message_val))
        constant = float(input('Enter constant:\n').strip())
        print('The result is:')
        print(constant * matrix)

    def matrix_mat_prod(self):
        matrices = self.matrix_list()
        print('The result is:')
        print(matrices[0] ** matrices[1])

    def matrix_list(self):
        matrices = list()
        aux = ('first', 'second')
        for i in range(2):
            message_dim = f'Enter size of {aux[i]} matrix:'
            message_val = f'Enter {aux[i]} matrix:'
            matrices.append(Matrix(*self.builder.build(message_dim, message_val)))
        return matrices


if __name__ == '__main__':
    processor = Main()
    processor.main()

