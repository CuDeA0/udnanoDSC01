"""loadData.py
Load in the dataset using pandas
"""
import os
import pandas as pd

def load():
    """
    This function loads the dataset in the data/ folder for the
    udnanoDSC01 project

    Outputs:
        Pandas dataframe with the data
    """
    # The file is referenced from where it is called, which should
    # be the top directory (one aboce this file)
    fileName = "data/d1.csv"
    # If the file can't be found then we let the user know there is
    # something very wrong and stop the system
    if not os.path.isfile(fileName):
        raise FileNotFoundError(f"File not found {fileName}. Validate data strucure")
    df = pd.read_csv(fileName)
    return df


def clean(df):
    """
    Clean the input datframe with a specific strategy.

    Input
         df    :[pandas.DataFrame] with the raw data
    Output
         df    :[pandas.DataFrame] with the cleaned data
    """
