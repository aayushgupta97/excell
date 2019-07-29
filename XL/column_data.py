import pandas as pd
import numpy as np


def get_first_row_data(file):
    file = pd.read_csv(file)
    # file_columns = [''.join(item.split('\n')) for item in file.columns.tolist()]
    df = pd.DataFrame(file)
    first_row = df.iloc[0].tolist()
    return first_row


def get_results(file, column_list, data_list):
    file = pd.read_csv(file)
    df = pd.DataFrame(file)
    fail_check_list = [0 for i in range(len(column_list))]
    pass_check_list = [0 for i in range(len(column_list))]
    file_columns = [''.join(item.split('\n')) for item in df.columns.tolist()]
    labelled_column = df.columns.tolist()
    count = 0
    if file_columns == column_list:
        for col in labelled_column:
            current_col = df[col].tolist()
            for row in current_col:
                if str(row) != str(data_list[count]):
                    fail_check_list[count] += 1
                else:
                    pass_check_list[count] += 1
            count = count + 1
    pass_fail_list = [pass_check_list, fail_check_list]
    return pass_fail_list

    # for col in lst:
    #     return df[col]
    # dd = list(pd.DataFrame(file))
    # df = file.iloc[1].tolist()
    # fail_check_list = [[] for i in range(len(lst))]
    # for i in range(len(lst)):
    #     if lst[i] == pd.iloc[]
    # return fail_check_list


# def get_passes(file, lst):

def get_row_at_nth_position(file, row_no):
    file  = pd.read_csv(file)
    df = pd.DataFrame(file)
    return df.iloc[row_no].tolist()

# def get_column_by_name()