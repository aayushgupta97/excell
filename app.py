from XL.columns import *
from XL.column_data import *

# column_header_check = compare_column_csv('FS_OWR_20.csv', 'FS_OWR_20 (copy).csv')
# column_header_check_2 = compare_column_excel('FS_OWR_20.csv', 'FS_OWR_20 (copy).csv')
# column_header_check_3 = compare_column_csv_excel('FS_OWR_20.csv', 'FS_OWR_20.xlsx', 'Sheet1')
# print(column_header_check_3)




# with open("output.csv", "w") as f:
#     csv_columns = ['Column Name', 'Passes', 'Fails', 'Checked Value', 'Different Values']
#     writer = csv.writer(f)
#     writer.writerow(csv_columns)
#     writer.writerows(zip(columns, pass_check_list, fail_check_list, check_list, column_different_values_list))

# print(get_columns('FS_OWR_20.csv'))


# first_row = get_first_row_data('FS_OWR_20.csv')
# cols = get_columns('FS_OWR_20.csv')
# # print(first_row)
#
# # print (get_fails('FS_OWR_20.csv', cols, first_row))
#
# result_list = get_results('FS_OWR_20.csv', cols, first_row)
# print(result_list)
# pass_list = result_list[0]
# fail_list = result_list[1]
#
# print(pass_list)
# print(fail_list)

# print(get_row_at_nth_position('FS_OWR_20.csv', 316))

# print(get_column_by_name('FS_OWR_20.csv', 'Taxability'))


# print(get_distinct_column_values('FS_OWR_20.csv'))
# print(get_null_values('FS_OWR_20.csv'))