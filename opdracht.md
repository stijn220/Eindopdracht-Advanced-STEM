Eindopdracht Advanced STEM - Luchtkwaliteit Voorspellingssysteem
================================================================

Introductie
-----------

In deze eindopdracht ga je in **duo's** werken aan een systeem voor het analyseren en voorspellen van luchtkwaliteit in Nederland. De focus ligt op fijnstof (PM2.5), wat een belangrijke indicator is voor luchtkwaliteit. Langdurige blootstelling aan verhoogde concentraties fijnstof kan leiden tot verschillende gezondheidsklachten, met name aan de luchtwegen en longen. Kleine deeltjes (PM2.5) kunnen dieper in de longen doordringen dan grotere deeltjes (PM10) en vormen daardoor een groter gezondheidsrisico.

Je combineert kennis van API-ontwikkeling, datapreprocessing, en machine learning om een voorspellingssysteem te maken dat een week vooruit kan voorspellen.

Dataset
-------

De data is afkomstig van het Rijksinstituut voor Volksgezondheid en Milieu (RIVM) via het [Luchtmeetnet](https://data.rivm.nl/data/luchtmeetnet/). Voor deze opdracht zijn de volgende bestanden beschikbaar gesteld in een zip bestand:

-   PM2.5 metingen over heel 2023
-   PM2.5 metingen per maand voor 2024
-   Een voorbeeld notebook om te starten

De data bevat metingen van verschillende weerstations door heel Nederland.

Opdracht Structuur
------------------

### Fase 1: Data Processing & Model Development

#### Data Preprocessing

-   Laad en analyseer de ruwe dataset
-   Identificeer missing values en implementeer een passende (multiple) imputation strategie
-   Pas dimensionaliteitsreductie methode toe zoals geleerd in de datacamp

#### Feature Engineering & Dimensionaliteitsreductie

-   Gebruik PCA om de data van verschillende meetstations te combineren
-   Selecteer het optimale aantal PCA componenten voor je model
-   Analyseer hoeveel variantie behouden blijft

#### Model Ontwikkeling

-   Train een tijdreeksmodel dat tot een week vooruit kan voorspellen
-   Valideer het model met verschillende metrics
-   Sla het getrainde model op voor gebruik in de API

### Fase 2: API Development

#### API Ontwikkeling met Flask

Ontwikkel een Flask API met:

-   `/predict` (GET): Retourneert luchtkwaliteitsvoorspellingen voor de komende week in JSON. Elke dag zijn er dus nieuwe voorspellingen.

**Optionele** endpoints:

-   `/update-model` (POST): Voor het updaten van model parameters
-   `/train` (POST): Voor het trainen op nieuwe maand data

Technische Vereisten
--------------------

1.  **Data Processing**
    -   Kies en implementeer een geschikte (multiple) imputation methode
    -   Voer dimensionaliteitsreductie methode uit zoals in datacamp geleerd
2.  **Machine Learning**
    -   Implementeer PCA om PM2.5 van de stationsdata te combineren
    -   Train een tijdreeks voorspellingsmodel
    -   Valideer model performance
3.  **API Development**
    -   Ontwikkel het voorspellings-endpoint
    -   Implementeer error handling
    -   Zorg voor gestructureerde JSON responses

Beoordeling (100 punten)
------------------------

1.  Jupyter notebook (50 punten):
    -   Data analyse (15 punten)
    -   Model ontwikkeling (20 punten)
    -   Validatie resultaten (10 punten)
    -   Onderbouwing van gemaakte keuzes (5 punten)
2.  Python files (50 punten):\
    **app.py** (35 punten):
    -   Geïntegreerde code uit de notebook, voorkeur in een class (10 punten)
    -   Flask API implementatie (15 punten)
    -   Error handling (5 punten)
    -   Documentatie in de code (5 punten)**use_api.py** (15 punten):
    -   Demonstratie van API gebruik (5 punten)
    -   Code om requests te maken naar alle endpoints (5 punten)
    -   Verwerking van de API responses naar een pandas DataFrame (5 punten)
