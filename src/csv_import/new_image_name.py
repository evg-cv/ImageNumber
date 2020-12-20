import pandas as pd

from settings import CSV_PATH


def extract_new_name_from_old(number):

    contents = pd.read_csv(CSV_PATH, header=None)
    new_name = contents.loc[contents[9] == int(number)].values.tolist()[0][1]

    return new_name


if __name__ == '__main__':

    extract_new_name_from_old(number=10)
