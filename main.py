from domain.Matrix import Matrix
from domain.MatrixBuilder import MatrixBuilder

if __name__ == '__main__':
    Builder = MatrixBuilder()
    my_matrix = Matrix(*Builder.build())
    print(f"First matrix:\n{my_matrix}")
    print(f"Negating matrix: \n{-my_matrix}")

    other_matrix = Matrix(*Builder.build())
    print(f"Second matrix:\n{other_matrix}")

    sum_matrices = my_matrix + other_matrix
    print(f"Addition: \n{sum_matrices}")

    dif_matrices = my_matrix - other_matrix
    print(f"Subtraction:\n{dif_matrices}")

    mul_by_constant = 3 * my_matrix
    print(f"Multiplication by constant:\n{mul_by_constant}")
