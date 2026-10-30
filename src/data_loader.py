import pandas as pd


def load_data(file_path):
    #Charge le dataset clients depuis un fichier CSV.
    return pd.read_csv(file_path)
