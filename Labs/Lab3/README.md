# Lab 3 -- FastAPI ML Inference (Repurposed Wine Classifier)

## Overview

This lab implements a production-style FastAPI service that serves
predictions from a trained scikit-learn model.

Compared to the original template, this version includes several
improvements:

-   Uses the **Wine dataset** (multi-class classification) instead of
    Iris\
-   Trains a stronger model: **Pipeline(StandardScaler →
    LogisticRegression)**\
-   Saves reproducible artifacts: `model/wine_model.joblib` and
    `model/metadata.json`\
-   Adds richer endpoints: `/health`, `/metadata`, `/predict`,
    `/predict_batch`\
-   Loads the model once using caching instead of reloading per request\
-   Provides batch inference capability\
-   Includes structured metadata for schema + metrics transparency

This lab demonstrates clean model training, artifact management, API
serving, and reproducibility --- aligned with practical MLOps workflows.

------------------------------------------------------------------------

## Project Structure

    Lab3/
    │
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    ├── model/
    │   └── wine_model.joblib (generated)
    │   └── metadata.json (generated)
    └── src/
        ├── __init__.py
        ├── data.py
        ├── train.py
        ├── predict.py
        └── main.py

------------------------------------------------------------------------

## 1️⃣ Create and Activate Virtual Environment

From inside `MLOps/Labs/Lab3`:

``` bash
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip:

``` bash
python -m pip install --upgrade pip
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 2️⃣ Train the Model

Run:

``` bash
python -m src.train
```

This generates:

-   `model/wine_model.joblib`
-   `model/metadata.json`

The metadata file stores:

-   Feature names and order
-   Class names
-   Model type
-   Accuracy and classification report
-   Dataset information

------------------------------------------------------------------------

## 3️⃣ Run the FastAPI Server

Start the API:

``` bash
uvicorn src.main:app --reload
```

Open in your browser:

-   Interactive Docs: http://127.0.0.1:8000/docs
-   Metadata endpoint: http://127.0.0.1:8000/metadata

------------------------------------------------------------------------

## Available Endpoints

### GET `/`

Basic root check.

### GET `/health`

Health check endpoint.

### GET `/metadata`

Returns:

-   Feature order
-   Class names
-   Model info
-   Evaluation metrics

### POST `/predict`

Single prediction.

Example request:

``` json
{
  "features": [13.2, 1.78, 2.14, 11.2, 100.0, 2.65, 2.76, 0.26, 1.28, 4.38, 1.05, 3.4, 1050.0]
}
```

Example response:

``` json
{
  "class_id": 0,
  "class_name": "class_0",
  "probabilities": [0.92, 0.05, 0.03]
}
```

------------------------------------------------------------------------

### POST `/predict_batch`

Batch inference.

Example request:

``` json
{
  "rows": [
    [13.2, 1.78, 2.14, 11.2, 100.0, 2.65, 2.76, 0.26, 1.28, 4.38, 1.05, 3.4, 1050.0],
    [12.4, 2.1, 2.3, 21.0, 95.0, 2.1, 2.5, 0.3, 1.5, 3.2, 1.1, 2.9, 900.0]
  ]
}
```

------------------------------------------------------------------------

## Model Details

-   Dataset: `sklearn.datasets.load_wine`
-   Model: `Pipeline(StandardScaler → LogisticRegression)`
-   Multi-class classification (3 classes)
-   Stratified train/test split
-   Model evaluation stored in metadata

------------------------------------------------------------------------

## Key MLOps Concepts Demonstrated

-   Clean dataset abstraction (`data.py`)
-   Reproducible model training
-   Artifact persistence (model + metadata)
-   Schema-aware inference validation
-   Model caching for performance
-   Batch inference endpoint
-   Structured API design
-   Version-controlled project structure

------------------------------------------------------------------------

## Notes

-   Feature order matters. Always check `/metadata` to confirm feature
    sequence.

-   If the API raises a model-not-found error, retrain using:

    ``` bash
    python -m src.train
    ```

------------------------------------------------------------------------

## Conclusion

This lab demonstrates a clean separation of:

-   Data loading\
-   Model training\
-   Artifact storage\
-   Inference logic\
-   API serving

The result is a reproducible, modular, and production-aligned FastAPI
machine learning service.
