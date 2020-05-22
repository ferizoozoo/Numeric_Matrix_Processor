import math

def read_matrix(n, m):
    matrix = [[] for _i in range(n)]
    for row in range(n):
        matrix[row] = list(map(float, input().split()))
    return matrix


def matrix_addition(a, b):
    n = len(a)
    m = len(a[0])
    result_matrix = [[0 for _i in range(m)] for _i in range(n)]
    for row in range(n):
        for column in range(m):
            result_matrix[row][column] = a[row][column] + b[row][column]
    return result_matrix


def matrix_multiplication_by_constant_c(a, c):
    n = len(a)
    m = len(a[0])
    for row in range(n):
        for column in range(m):
            a[row][column] *= c


def matrix_multiplication(a, b):
    if len(a[0]) != len(b):
        print('the dimensions do not match.')
        return []
    n = len(a)
    m = len(b[0])
    result = [[0 for _i in range(m)] for _i in range(n)]
    for row in range(n):
        for column in range(m):
            for k in range(len(b)):
                result[row][column] += a[row][k] * b[k][column]
    return result


def cofactor(matrix, row, column, n):
    cofac = [[0 for _i in range(n - 1)] for _i in range(n - 1)]
    i = j = 0
    for r in range(n):
        for c in range(n):
            if r != row and c != column:
                cofac[i][j] = matrix[r][c]
                j += 1
                if j == n - 1:
                    j = 0
                    i += 1
    return cofac


def determinant(matrix):
    n = len(matrix)
    det = 0
    sign = 1
    if n == 1:
        return matrix[0][0]
    for col in range(n):
        det += sign * matrix[0][col] * determinant(cofactor(matrix, 0, col, n))
        sign = -sign
    return det


def print_matrix(mat, n, m):
    for row in range(n):
        for column in range(m):
            print(mat[row][column], end=' ')
        print()


class TransposeMatrix:
    def __init__(self):
        print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        self.choice = int(input())
        self.n, self.m = list(map(int, input().split()))
        self.new_matrix = [[0 for _i in range(self.m)] for _i in range(self.n)]
        self.matrix = read_matrix(self.n, self.m)
        self.menu()


    def menu(self):
        if self.choice == 1:
            self.main_diagonal()
        elif self.choice == 2:
            self.side_diagonal()
        elif self.choice == 3:
            self.vertical_line()
        elif self.choice == 4:
            self.horizontal_line()


    def main_diagonal(self):
        for row in range(self.n):
            for column in range(self.m):
                self.new_matrix[row][column] = self.matrix[column][row]


    def side_diagonal(self):
        for row in range(self.n):
            for column in range(self.m):
                self.new_matrix[row][column] = self.matrix[self.n - 1 - column][self.m - 1 - row]


    def vertical_line(self):
        for row in range(self.n):
            for column in range(self.m):
                 self.new_matrix[row][column] = self.matrix[row][self.m - 1 - column]


    def horizontal_line(self):
        for row in range(self.n):
            for column in range(self.m):
                self.new_matrix[row][column] = self.matrix[self.n - 1 - row][column]


    def print_transposed_matrix(self):
        print_matrix(self.new_matrix, self.n, self.m)


def transpose_main_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0 for _i in range(m)] for _i in range(n)]
    for row in range(n):
        for column in range(m):
            new_matrix[row][column] = matrix[column][row]
    return new_matrix


def inverse(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n != m:
        return
    determinant_of_matrix = determinant(matrix)
    if determinant_of_matrix == 0:
        return
    cofactor_matrix = [[0 for _i in range(n)] for _i in range(n)]
    for row in range(n):
        for column in range(n):
            cofactor_matrix[row][column] = math.pow(-1, row + column) * determinant(cofactor(matrix, row, column, n))
    matrix_multiplication_by_constant_c(cofactor_matrix, float(1) / determinant_of_matrix)
    return transpose_main_diagonal(cofactor_matrix)


def main():
    while True:
        print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6.Inverse matrix\n0. Exit')
        choice = int(input())
        if choice == 1:
            matrices = []
            for _i in range(2):
                n, m = list(map(int, input().split()))
                matrices.append(read_matrix(n, m))
            if len(matrices[0]) != len(matrices[1]) or len(matrices[0][0]) != len(matrices[1][0]):
                print('ERROR')
                break
            result = matrix_addition(matrices[0], matrices[1])
            print_matrix(result, len(result), len(result[0]))
        elif choice == 2:
            n, m = list(map(int, input().split()))
            matrix = read_matrix(n, m)
            c = int(input())
            matrix_multiplication_by_constant_c(matrix, c)
            print_matrix(matrix, n, m)
        elif choice == 3:
            matrices = []
            for _i in range(2):
                n, m = list(map(int, input().split()))
                matrices.append(read_matrix(n, m))
            result = matrix_multiplication(matrices[0], matrices[1])
            if len(result) > 0:
                print_matrix(result, len(matrices[0]), len(matrices[1][0]))
        elif choice == 4:
            transposed = TransposeMatrix()
            if transposed:
                transposed.print_transposed_matrix()
        elif choice == 5:
            n, m = list(map(int, input().split()))
            if n != m:
                print('Could not calculate the determinant.')
                continue
            print(determinant(read_matrix(n, m)))
        elif choice == 6:
            n, m = list(map(int, input().split()))
            if n != m:
                print('The matrix is not invertible.')
                continue
            print_matrix(inverse(read_matrix(n, m)), n, m)
        elif choice == 0:
            break


if __name__ == '__main__':
    main()

