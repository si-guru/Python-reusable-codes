import pandas as pd


def get_excel_as_dataframe(file_object):
    dataframe = None
    try:
        dataframe = pd.read_excel(file_object)
    except Exception as ex:
        print(ex)
    return dataframe