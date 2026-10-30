
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os


def prepare_features(df):
    #Sélectionne les variables utilisées pour le clustering
    return df[["Annual Income (k$)", "Spending Score (1-100)"]]


def scale_features(features):
    #Standardise les variables pour le clustering.
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features, scaler


def find_optimal_clusters(scaled_features):
    #Calcule et affiche l'inertie pour plusieurs valeurs de K
    inertias = []
    k_values = range(1, 11)

    for k in k_values:
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(scaled_features)
        inertias.append(model.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(k_values, inertias, marker="o")
    plt.title("Méthode du coude — choix du nombre de clusters")
    plt.xlabel("Nombre de clusters (K)")
    plt.ylabel("Inertie")
    plt.xticks(list(k_values))
    plt.tight_layout()
    plt.show()


def train_kmeans(scaled_features, n_clusters=5):
    #Entraîne K-Means et retourne les étiquettes des clusters
    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(scaled_features)
    return model, labels



def plot_clusters(features, labels, model, scaler,output_path):
    #Visualise les clusters et leurs centres."""
    plt.figure(figsize=(9, 6))
    plt.scatter(
        features.iloc[:, 0], #features["Annual Income (k$)"],
        features.iloc[:, 1], #features["Spending Score (1-100)"],
        c=labels,
        cmap="viridis",
        s=60
    )

    centers = scaler.inverse_transform(model.cluster_centers_)

    plt.scatter(
        centers[:, 0],
        centers[:, 1],
        marker="X",
        s=250,
        c="red",
        label="Centres des clusters"
    )

    plt.title("Segmentation des clients avec K-Means")
    plt.xlabel("Revenu annuel (k$)")
    plt.ylabel("Score de dépense (1-100)")
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()



def summarize_clusters(df, labels):
    #Résume les caractéristiques de chaque cluster
    results = df.copy()
    results["Cluster"] = labels

    summary = results.groupby("Cluster").agg(
        Nombre_clients=("CustomerID", "count"),
        Age_moyen=("Age", "mean"),
        Revenu_moyen=("Annual Income (k$)", "mean"),
        Score_depense_moyen=("Spending Score (1-100)", "mean")
    ).round(2)

    return summary


def save_segmented_data(df, labels, output_path):
    #Ajoute les clusters aux clients et exporte le résultat
    results = df.copy()
    results["Cluster"] = labels

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    results.to_csv(output_path, index=False)

    print(f"Dataset segmenté enregistré : {output_path}")