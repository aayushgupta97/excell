import pandas as pd
import numpy as np


def get_first_row_data(df):
    # file_columns = [''.join(item.split('\n')) for item in file.columns.tolist()]
    first_row = df.iloc[0].tolist()
    return first_row


def get_results(df, column_list, data_list):
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
    else:
        return 'Columns do not match. Cannot process further'
    pass_fail_list = [pass_check_list, fail_check_list]
    return pass_fail_list


def get_row_at_nth_position(df, row_no):
    return df.iloc[row_no].tolist()


def get_column_by_name(df, column_name):
    return df[column_name].tolist()


def get_distinct_column_values(df):
    column_names = df.columns.tolist()
    distinct_value_list = [[] for i in range(len(column_names))]
    count = 0
    for i in range(len(column_names)):
        n_uni = df[column_names[count]].nunique()
        uni = df[column_names[count]].unique()
        distinct_value_list[count].append(n_uni)
        distinct_value_list[count].append(uni)
        count += 1
    return distinct_value_list


def get_null_values(df):
    column_names = df.columns.tolist()
    null_value_list = [[] for i in range(len(column_names))]
    count = 0
    for i in range(len(column_names)):
        nl = df[column_names[count]].isnull().sum()
        null_value_list[count].append(nl)
        count += 1
    return null_value_list

