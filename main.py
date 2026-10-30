import pandas as pd

from src.data_loader import load_data
from src.data_quality import check_missing_values, check_duplicates
from src.visualization import plot_distributions, plot_income_vs_spending

from src.clustering import (
    prepare_features,
    scale_features,
    find_optimal_clusters,
    train_kmeans,
    plot_clusters,
    summarize_clusters,
    save_segmented_data
)

def main():
    
    # Chargement du dataset
    df = load_data("data/Mall_Customers.csv")

    # Affichage des premières lignes
    print("APERÇU DES DONNÉES")
    print(df.head())

    # Dimensions du dataset
    print("\nDIMENSIONS DU DATASET")
    print(df.shape)

    # Informations générales
    print("\nINFORMATIONS GÉNÉRALES")
    df.info()

    # Statistiques descriptives
    print("\nSTATISTIQUES DESCRIPTIVES")
    print(df.describe())


    check_missing_values(df)
    check_duplicates(df)

    
    plot_distributions(df)
    plot_income_vs_spending(df)
    

    features = prepare_features(df)
    
    print("\nVARIABLES RETENUES POUR LE CLUSTERING")
    print(features.head())
    print("\nDIMENSIONS DES VARIABLES")
    print(features.shape)
    
    scaled_features, scaler = scale_features(features)

    
    print("\nAPERÇU DES DONNÉES STANDARDISÉES")
    print(scaled_features[:5])
    print("\nDIMENSIONS DES DONNÉES STANDARDISÉES")
    print(scaled_features.shape)
    

    find_optimal_clusters(scaled_features)

    model, labels = train_kmeans(scaled_features)

    print("\nRÉPARTITION DES CLIENTS PAR CLUSTER")
    print(pd.Series(labels).value_counts().sort_index())


    plot_clusters(features, labels, model, scaler,"outputs/segmentation_clients.png")
    
    summary = summarize_clusters(df, labels)
    print("\nPROFIL DES CLUSTERS")
    print(summary)
    

    save_segmented_data(
        df,
        labels,
        "outputs/clients_segmentes.csv"
    )

if __name__ == "__main__":
    main()




