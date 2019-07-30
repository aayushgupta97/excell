import pandas as pd
import numpy as np


def compare_column(file1, file2):
    file1_column_head = file1.columns.tolist()
    file2_column_head = file2.columns.tolist()
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


def get_columns(df):
    file_columns = [''.join(item.split('\n')) for item in df.columns.tolist()]
    # file_columns = file.columns.tolist()
    return file_columns

