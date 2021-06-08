def make_matrix(matrix, number):
    original_row_list = matrix.split()
    original_column_list = matrix.split()
    row_matrix = []
    column_matrix = []
    # for row
    for sublist in original_row_list:
        row_matrix.append(original_row_list[0:number+1])
        for num in range(0, number+1):
            original_row_list.pop(num)

    # for column
    for i in range(number):
        column_list = []
        first_index = 0
        for num in range(first_index, len(original_column_list), number-1):
            column_list.append(num)
        column_matrix.append(column_list)
        first_index += 1

    return row_matrix, column_matrix


# def beautify_matrix(n, matrix):
#     row_matrix, column_matrix = make_matrix(matrix, n)
#     sum_lis = []
#     req_sum = 0
#     operations = 0
#     for num in row_matrix:
#         if req_sum < sum(num):
#             req_sum = sum(num)
#         sum_lis.append(sum(num))
#     for num in column_matrix:
#         if req_sum < sum(num):
#             req_sum = sum(num)
#         sum_lis.append(sum(num))
#     for num in sum_lis:
#         increment = num-req_sum
#         operations += increment
#     print(f'No.of Operations would be {operations}')


# beautify_matrix(3, "1 2 3 4 2 3 3 2 1")

make_matrix("1 2 3 4 2 3 3 3 2 1", 3)
