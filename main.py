class Matrix:
    def __init__(self, n, rows):
        self.n = n
        self.rows = rows

    n = 0
    rows = []

# reads the input from a file
def get_input(filename):
    with open(filename) as file:
        l = file.read().splitlines()
    n = int(l[0])
    for i in range(1, n + 1):
        l[i] = l[i].split()
        l[i] = [float(i) for i in l[i]]

    m = Matrix(n, l[1:])
    return m


# main method for carrying out the calculations
def calculate(matrix):
    n = matrix.n
    rank = n
    unit_matrix = create_unit(n)
    degenerate_rows = []
    for i in range(0, n):
        pivot = matrix.rows[i][i]
        if pivot != 1:
            if pivot == 0:
                exchanged = False
                for j in range(i + 1, n):
                    if matrix.rows[j][i] != 0:
                        row_exchange(matrix, i, j)
                        row_exchange(unit_matrix, i, j)
                        exchanged = True
                        pivot = matrix.rows[i][i]
                        break
                if not exchanged:
                    rank -= 1
                    degenerate_rows.append(i)
                    continue

            c = 1 / pivot
            scalar_multiplication(matrix, i, c)
            scalar_multiplication(unit_matrix, i, c)
        # print(matrix.rows)
        for j in range(0, n):
            if j != i:
                coefficient = matrix.rows[j][i]
                row_addition(matrix, j, i, -coefficient)
                row_addition(unit_matrix, j, i, -coefficient)
        # print(matrix.rows)
        # print(rank)

    if rank == n:
        result = 'Unique solution: '
        for i in range(0, n):
            result += str(round(matrix.rows[i][n], 5)) + ' '
        print(result)
        inverted = 'Inverted A:\t'
        for i in range(0, n):
            for j in range(0, n):
                inverted += str(round(unit_matrix.rows[i][j], 5)) + ' '
            inverted += '\n\t\t\t'
        print(inverted)
    else:
        no_solution = False
        for index in degenerate_rows:
            if matrix.rows[index][n] != 0:
                no_solution = True
        if no_solution:
            print('Inconsistent problem')
        else:
            result1 = 'Arbitrary variables: '
            result2 = 'Arbitrary solution: '
            for i in range(len(degenerate_rows)):
                result1 += '0 '
            print(result1)
            for i in range(0, n):
                if i in degenerate_rows:
                    result2 += '0 '
                else:
                    result2 += str(matrix.rows[i][n]) + ' '
            print(result2)


# creates a unit matrix of size n*n
def create_unit(n):
    rows = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if j == i:
                row.append(1)
            else:
                row.append(0)
        rows.append(row)
    unit_matrix = Matrix(n - 1, rows)
    return unit_matrix


# multiplies the row at index r2 by the coefficient and adds it to row at index r1
def row_addition(matrix, r1, r2, coefficient):
    r3 = []
    n = matrix.n
    for i in range(0, n + 1):
        r3.append(round(matrix.rows[r1][i] + matrix.rows[r2][i] * coefficient, 6))
    matrix.rows[r1] = r3


# multiplies the row at given index of a matrix by a scalar
def scalar_multiplication(matrix, r, c):
    cr = []
    n = matrix.n
    for i in range(0, n + 1):
        cr.append(matrix.rows[r][i] * c)
    matrix.rows[r] = cr


# exchanges two rows of a matrix
def row_exchange(matrix, r1, r2):
    temp = matrix.rows[r1]
    matrix.rows[r1] = matrix.rows[r2]
    matrix.rows[r2] = temp
    return matrix


filenames = ['Data1.txt', 'Data2.txt', 'Data3.txt', 'Data4.txt']
for i in range(0, 4):
    matrix = get_input(filenames[i])
    calculate(matrix)
    print('')
