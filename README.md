# Segmentation des clients avec K-Means

## 1. Présentation du projet

Ce projet consiste à segmenter les clients d'un centre commercial à l'aide d'un algorithme de Machine Learning non supervisé : **K-Means**.

L'objectif est d'identifier des groupes de clients ayant des comportements similaires en fonction de leur revenu annuel et de leur score de dépense. Cette segmentation peut aider une entreprise à mieux comprendre ses clients et à adapter ses stratégies marketing.

## 2. Dataset

Le jeu de données contient **200 clients** et cinq variables initiales :

| Variable | Description |
|---|---|
| `CustomerID` | Identifiant unique du client |
| `Gender` | Genre du client |
| `Age` | Âge du client |
| `Annual Income (k$)` | Revenu annuel, exprimé en milliers de dollars |
| `Spending Score (1-100)` | Score de dépense attribué au client, compris entre 1 et 100 |

### Contrôle qualité

L'analyse initiale a permis de vérifier que le dataset ne contient :
- Aucune valeur manquante.
- Aucun doublon détecté.

## 3. Outils et technologies

- **Python** : développement du projet.
- **Pandas** : manipulation et analyse des données.
- **Matplotlib** : création des visualisations.
- **Seaborn** : exploration graphique des données.
- **Scikit-learn** : standardisation et clustering avec K-Means.

## 4. Méthodologie

Le projet suit les étapes suivantes :

1. Chargement et exploration du dataset.
2. Vérification de la qualité des données.
3. Analyse exploratoire et visualisation des variables.
4. Sélection du revenu annuel et du score de dépense.
5. Standardisation des variables avec `StandardScaler`.
6. Recherche du nombre de clusters à l'aide de la méthode du coude (*Elbow Method*).
7. Entraînement du modèle K-Means avec cinq clusters.
8. Analyse des caractéristiques de chaque segment.
9. Exportation des résultats et du graphique de segmentation.

## 5. Résultats de la segmentation

Le modèle K-Means a réparti les 200 clients en cinq segments.

| Cluster | Nombre de clients | Revenu annuel moyen (k$) | Score de dépense moyen |
|---|---:|---:|---:|
| 0 | 81 | 55,30 | 49,52 |
| 1 | 39 | 86,54 | 82,13 |
| 2 | 22 | 25,73 | 79,36 |
| 3 | 35 | 88,20 | 17,11 |
| 4 | 23 | 26,30 | 20,91 |

### Interprétation des segments

- **Cluster 0 — Dépenses modérées :** revenus moyens et score de dépense proche de la moyenne.
- **Cluster 1 — Revenus élevés et dépenses élevées :** clients à revenus élevés présentant des scores de dépense importants.
- **Cluster 2 — Revenus faibles et dépenses élevées :** clients ayant des revenus plus modestes, mais des scores de dépense élevés.
- **Cluster 3 — Revenus élevés et dépenses faibles :** clients à revenus élevés présentant des scores de dépense faibles.
- **Cluster 4 — Revenus faibles et dépenses faibles :** clients ayant des revenus et des scores de dépense relativement faibles.

Ces profils permettent de mieux comprendre les différences de comportement entre les groupes et d'envisager des stratégies marketing adaptées.

## 6. Livrables

Les fichiers générés sont enregistrés dans le dossier `outputs/`.

- `clients_segmentes.csv` : dataset initial enrichi d'une colonne `Cluster` contenant le groupe attribué à chaque client.
- `segmentation_clients.png` : visualisation des cinq clusters et de leurs centres.

## 7. Structure du projet

```text
Customer_Segmentation/
├── data/
│   └── Mall_Customers.csv
├── outputs/
│   ├── clients_segmentes.csv
│   └── segmentation_clients.png
├── src/
│   ├── data_loader.py
│   ├── data_quality.py
│   ├── visualization.py
│   └── clustering.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 8. Installation et exécution

### Prérequis

- Python installé sur la machine.
- Git, si le projet est récupéré depuis GitHub.

### Étape 1 — Récupérer le projet

Clonez le dépôt GitHub, puis placez-vous dans son dossier :

```bash
git clone URL_DU_DEPOT
cd Customer_Segmentation
```

Remplacez `URL_DU_DEPOT` par l'adresse réelle de votre dépôt.

### Étape 2 — Créer un environnement virtuel

Sous Windows :

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Étape 3 — Installer les dépendances

```powershell
pip install -r requirements.txt
```

### Étape 4 — Exécuter le projet

```powershell
py main.py
```

Le script charge les données, effectue les contrôles et les analyses prévus, entraîne le modèle et génère les résultats.

## 9. Limites du projet

La segmentation repose uniquement sur deux variables : le revenu annuel et le score de dépense. L'âge et le genre ne sont pas utilisés pour entraîner le modèle.

Le score de dépense est un indicateur fourni par le dataset ; il ne correspond pas directement à un montant d'achat ou à une mesure de rentabilité.

Les segments obtenus sont exploratoires. Des données supplémentaires sur les achats réels, la fréquence des visites et les marges permettraient d'affiner l'analyse métier.

## 10. Auteur

**Babou Diouf**

Projet de portfolio en analyse de données et Machine Learning non supervisé.
