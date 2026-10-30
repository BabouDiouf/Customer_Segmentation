
def check_missing_values(df):
    #Affiche le nombre de valeurs manquantes par colonne
    missing = df.isnull().sum()
    print("\nVALEURS MANQUANTES")
    print(missing)
    return missing


def check_duplicates(df):
    #Compte les lignes dupliquées
    duplicates = df.duplicated().sum()
    print(f"\nNombre de doublons : {duplicates}")
    return duplicates
