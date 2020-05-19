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



def print_matrix(mat, n, m):
    for row in range(n):
        for column in range(m):
            print(mat[row][column], end=' ')
        print()


def main():
    while True:
        print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit')
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
        elif choice == 0:
            break


if __name__ == '__main__':
    main()

