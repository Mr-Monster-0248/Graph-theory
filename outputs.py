"""
All outputs functions of the project
"""


def printMatrix(matrix):
    print("\t", end='')
    for i in range(len(matrix[0])):
        print(str(i) + "\t", end='')
    print('')
    for i in range(len(matrix)):
        print(str(i) + '\t', end='')
        for value in matrix[i]:
            print(str(value) + '\t', end='')
        print('')
    print()
