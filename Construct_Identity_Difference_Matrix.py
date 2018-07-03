from class_Difference_Matrix_Manipulation import DifferenceMatrixManipulation


if __name__ == "__main__":
    filenameA = '/home/18969577/Documents/Genolve/Identity_difference_matrix/class_Difference_Matrix_Manipulation/GenomeA_names_positions'
    filenameB = '/home/18969577/Documents/Genolve/Identity_difference_matrix/class_Difference_Matrix_Manipulation/GenomeB_names_positions'
    generate_difference_matrix = DifferenceMatrixManipulation()
    path, *remainder = filenameA.rpartition('/')
    output_filename = path + '/' + 'Identity_Difference_Marix' + '.txt'
    matrix = generate_difference_matrix.ConstructIdentityDifferenceMatrix(filenameA,filenameB, output_filename)
    print('Identity difference matrix written to ', output_filename)
