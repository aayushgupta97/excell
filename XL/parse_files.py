import pandas as pd
import numpy as np


def parse_csv(filepath):
    file = pd.read_csv(filepath)
    df = pd.DataFrame(file)
    return df


def parse_excel(filepath):
    file = pd.read_excel(filepath)
    df = pd.DataFrame(file)
    return df
