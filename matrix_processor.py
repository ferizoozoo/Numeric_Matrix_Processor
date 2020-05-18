def read_matrix(n, m):
    matrix = [[] for _i in range(n)]
    for row in range(n):
        matrix[row] = list(map(int, input().split()))
    return matrix


def matrix_addition(a, b):
    n = len(a)
    m = len(a[0])
    result_matrix = [[0 for _i in range(m)] for _i in range(n)]
    for row in range(n):
        for column in range(m):
            result_matrix[row][column] = a[row][column] + b[row][column]
    return result_matrix


def print_matrix(mat, n, m):
    for row in range(n):
        for column in range(m):
            print(mat[row][column], end=' ')
        print()


def main():
    matrices = []
    for _i in range(2):
        n, m = list(map(int, input().split()))
        matrices.append(read_matrix(n, m))
    if len(matrices[0]) != len(matrices[1]) or len(matrices[0][0]) != len(matrices[1][0]):
        print('ERROR')
        exit()
    result = matrix_addition(matrices[0], matrices[1])
    print_matrix(result, len(result), len(result[0]))


if __name__ == '__main__':
    main()

