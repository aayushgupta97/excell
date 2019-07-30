import argparse
import csv

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


def columns():
    cols = get_columns(csv1)


def write_csv():
    data = list(zip(get_columns(csv1), get_first_row_data(csv1)))
    df = pd.DataFrame(data)
    header = ("Columns", "First row vals")
    df.columns = header
    df.to_csv('output.csv', index=False)


write_csv()


def write_csv_np(zip_obj):
    """
    function to write the csv using csv module instead of pandas
    :param zip_obj:
    :return:
    """
    csv_columns = ['A', 'B', 'C']
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(csv_columns)
        writer.writerows(zip_obj)