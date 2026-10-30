import matplotlib.pyplot as plt
import seaborn as sns


def plot_distributions(df):
    #Affiche la distribution des principales variables
    columns = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

    for column in columns:
        plt.figure(figsize=(7, 4))
        sns.histplot(data=df, x=column, kde=True)
        plt.title(f"Distribution de {column}")
        plt.tight_layout()
        plt.show()


def plot_income_vs_spending(df):
    #Visualise le revenu annuel selon le score de dépense
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Gender"
    )
    plt.title("Revenu annuel et score de dépense")
    plt.tight_layout()
    plt.show()