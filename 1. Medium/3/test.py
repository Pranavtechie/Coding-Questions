def getlists(matrix, number):
    raw_row_list = matrix.split()  # [1,2,3,4,5,6]
    raw_column_list = matrix.split()
    row_list = []
    # for rows
    for i in range(0, len(raw_row_list), number):
        row_list.append([raw_row_list[i, i+(number-1)]])

    # for columns
    for i in range(0, len)
