import argparse
from XL.columns import *
from XL.column_data import *
from XL.parse_files import *


parser = argparse.ArgumentParser(description='process csv and excel files.')
parser.add_argument('-csv', '--csv1', help='CSV file containing data', required=True)
parser.add_argument('--csv2', help='CSV file containing data', required=False)
parser.add_argument('-xl', '--xl1', help='excel file containing data', required=False)
parser.add_argument('--xl2', help='excel file containing data', required=False)


args = vars(parser.parse_args())
print(args)

csv1 = parse_csv(args['csv1'])
if args['csv2'] is not None:
    csv2 = parse_csv(args['csv2'])
if args['xl1'] is not None:
    xl1 = parse_excel(args['xl1'])
if args['xl2'] is not None:
    xl2 = parse_excel(args['xl2'])


print(get_results(csv1, get_columns(csv1), get_first_row_data(csv1)))

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


# csv1 = parse_csv(args['--csv1'])
# args = parser.parse_args()


# print(type(csv1))

# print(compare_column_csv('FS_OWR_20-Sheet1-Outward.csv', 'FS_OWR_20-Outward (1).csv'))
# print(get_distinct_column_values('FS_OWR_20-Sheet1-Outward.csv'))


#
# df1 = pd.read_csv('FS_OWR_20-Sheet1-Outward.csv')
# df2 = pd.read_csv('FS_OWR_20-Outward (1).csv')

# difference = df1[df1 != df2]
# print(difference.dropna())
# print(difference)

# print(get_column_by_name('FS_OWR_20-Sheet1-Outward.csv', 'State'))

# print(compare_column_csv(csv1, csv2))