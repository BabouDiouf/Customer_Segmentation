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

## Interprétation métier et recommandations marketing

L'objectif de cette segmentation est d'identifier des groupes de clients présentant des comportements similaires en matière de revenu annuel et de score de dépense. Ces profils peuvent aider une entreprise à adapter ses actions marketing, à personnaliser ses offres et à mieux répartir ses ressources.

### 1. Clients à dépenses modérées — Cluster 0

**Profil :** 81 clients, soit 40,5 % du portefeuille analysé. Leur revenu annuel moyen est de 55,30 k$ et leur score de dépense moyen est de 49,52.

**Recommandations :**
- Mettre en place des programmes de fidélité.
- Proposer des produits complémentaires afin d'augmenter le panier moyen.
- Personnaliser les recommandations selon les achats et préférences observés.

**Objectif métier :** améliorer progressivement l'engagement et les dépenses des clients.

### 2. Clients à revenu élevé et dépenses élevées — Cluster 1

**Profil :** 39 clients, soit 19,5 % du portefeuille. Leur revenu annuel moyen est de 86,54 k$ et leur score de dépense moyen est de 82,13.

**Recommandations :**
- Proposer des avantages exclusifs et des offres personnalisées.
- Mettre en avant les nouveautés et les produits premium.
- Renforcer la fidélisation grâce à une expérience client de qualité.

**Objectif métier :** maintenir leur engagement et favoriser leur fidélité à long terme.

### 3. Clients à revenu faible et dépenses élevées — Cluster 2

**Profil :** 22 clients, soit 11 % du portefeuille. Leur revenu annuel moyen est de 25,73 k$ et leur score de dépense moyen est de 79,36.

**Recommandations :**
- Tester des promotions ciblées et des offres accessibles.
- Proposer des lots ou des réductions adaptées aux produits recherchés.
- Mesurer la rentabilité des campagnes avant de les généraliser.

**Objectif métier :** maintenir l'engagement tout en contrôlant les coûts promotionnels.

### 4. Clients à revenu élevé et dépenses faibles — Cluster 3

**Profil :** 35 clients, soit 17,5 % du portefeuille. Leur revenu annuel moyen est de 88,20 k$ et leur score de dépense moyen est de 17,11.

**Recommandations :**
- Identifier les éventuels freins à l'achat.
- Tester des recommandations personnalisées et des campagnes de réactivation.
- Analyser les préférences et les réactions aux offres proposées.

**Objectif métier :** identifier les leviers susceptibles d'améliorer leur engagement commercial.

### 5. Clients à revenu faible et dépenses faibles — Cluster 4

**Profil :** 23 clients, soit 11,5 % du portefeuille. Leur revenu annuel moyen est de 26,30 k$ et leur score de dépense moyen est de 20,91.

**Recommandations :**
- Privilégier des campagnes de communication peu coûteuses.
- Présenter des offres d'entrée de gamme pertinentes.
- Évaluer les réactions des clients avant d'investir davantage dans leur acquisition ou leur fidélisation.

**Objectif métier :** développer progressivement l'engagement tout en maîtrisant les coûts marketing.

### Indicateurs à suivre après les campagnes

Pour évaluer l'efficacité de ces recommandations, une entreprise pourrait suivre :
- Le taux de conversion par segment.
- Le panier moyen et la fréquence d'achat.
- Le taux de réachat et de rétention.
- Le chiffre d'affaires généré par segment.
- Le coût des campagnes et leur retour sur investissement.

### Limites de l'analyse

Cette segmentation repose sur le revenu annuel et le score de dépense fournis dans le dataset. Elle ne mesure pas directement le chiffre d'affaires réel, la marge ou la valeur vie client (Customer Lifetime Value).

Les recommandations proposées sont des hypothèses à tester avec des données de ventes réelles et des résultats de campagnes marketing. Elles ne constituent pas des conclusions causales.

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
git clone https://github.com/BabouDiouf/Customer_Segmentation.git
cd Customer_Segmentation
```

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
