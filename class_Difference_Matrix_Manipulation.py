import numpy as np

class DifferenceMatrixManipulation:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def ConstructIdentityDifferenceMatrix(self, filenameA, filenameB, output_filename):

        strA = np.loadtxt(filenameA, delimiter='\t', unpack=True, dtype=str)
        strB = np.loadtxt(filenameB, delimiter='\t', unpack=True, dtype=str)

        row1 = strA[0, :]
        column1 = strB[0, :]

        number_of_columns = int(len(row1)) + 1
        number_of_rows = int(len(column1)) + 1

        Identity_difference_matrix = np.empty((number_of_rows, number_of_columns), dtype=object)

        Identity_difference_matrix[0, 0] = 0

        for i in range(0, len(row1)):
            column = int(i) + 1
            Identity_difference_matrix[0, column] = row1[i]

        for i in range(0, len(column1)):
            row = int(i) + 1
            Identity_difference_matrix[row, 0] = column1[i]

        for i in range(0, (len(row1) + 1)):
            if i == 0:
                pass
            else:

                for j in range(0, (len(column1) + 1)):
                    if j == 0:
                        pass
                    else:

                        if Identity_difference_matrix[i, 0] == Identity_difference_matrix[0, j]:
                            Identity_difference_matrix[i, j] = 1
                        else:
                            Identity_difference_matrix[i, j] = 0

        np.savetxt(output_filename, Identity_difference_matrix, delimiter='\t', fmt="%s")