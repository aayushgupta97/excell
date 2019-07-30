import csv
import pandas as pd
import numpy as np


def compare_column_csv(file1, file2):
    # df_1 = pd.DataFrame(file1)
    # print(type(df_1))
    # df_2 = pd.DataFrame(file2)
    file1_column_head = file1.columns.tolist()
    file2_column_head = file2.columns.tolist()
    # map(str.strip, file1_column_head)
    stripped_list_1 = [''.join(x.split('\n')) for x in file1_column_head]
    stripped_list_2 = [''.join(x.split('\n')) for x in file2_column_head]

    if stripped_list_1 == stripped_list_2:
        return ['The columns are equal']
    else:
        diff = (np.array(stripped_list_1) == np.array(stripped_list_2))
        return diff
        # return [list(zip(stripped_list_1[stripped_list_1.index(item)],
        # stripped_list_2[stripped_list_1.index(item)], diff))
        # for item in stripped_list_1 if item not in stripped_list_2]
        # indexed_diff = list(filter(lambda x : x == False, diff))


def compare_column_excel(file1, file2):
    file1 = pd.read_excel(file1)
    file2 = pd.read_excel(file2)
    file1_column_head = file1.columns.tolist()
    file2_column_head = file2.columns.tolist()
    stripped_list_1 = [''.join(x.split('\n')) for x in file1_column_head]
    stripped_list_2 = [''.join(x.split('\n')) for x in file2_column_head]

    if stripped_list_1 == stripped_list_2:
        return ['The columns are equal']
    else:
        diff = (np.array(stripped_list_1) == np.array(stripped_list_2))
        return diff


def compare_column_csv_excel(file1, file2, sheet):
    file1 = pd.read_csv(file1)
    file2 = pd.read_excel(file2, sheet_name=sheet)
    file1_column_head = file1.columns.tolist()
    file2_column_head = file2.columns.tolist()
    stripped_list_1 = [''.join(x.split('\n')) for x in file1_column_head]
    stripped_list_2 = [''.join(x.split('\n')) for x in file2_column_head]

    if stripped_list_1 == stripped_list_2:
        return ['The columns are equal']
    else:
        diff = (np.array(stripped_list_1) == np.array(stripped_list_2))
        return diff


def get_columns(df):
    file_columns = [''.join(item.split('\n')) for item in df.columns.tolist()]
    # file_columns = file.columns.tolist()
    return file_columns

def hello(nm):
    return f"hello {nm}"
