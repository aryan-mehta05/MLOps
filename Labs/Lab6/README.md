# Lab 6 – MLflow-Based Wine Quality Classification

**Author:** Aryan Mehta

---

## Overview

In this lab, I implemented an end-to-end machine learning experiment pipeline using **MLflow**, **scikit-learn**, and **XGBoost** to predict whether a wine is high quality.

Instead of only reproducing the base lab, I expanded the implementation to make it more robust and production-oriented. My implementation includes:

- automated dataset download
- combining red and white wine datasets
- binary target engineering for high-quality wine prediction
- multi-model experimentation
- full MLflow tracking (params, metrics, artifacts, models)
- model comparison using validation AUC
- retraining the best model as a production candidate
- threshold tuning
- batch inference
- feature importance analysis
- model registration and reload verification

---

## Dataset

I used the **Wine Quality Dataset** (UCI repository), which contains physicochemical properties of red and white wines.

### Files used:
- `winequality-red.csv`
- `winequality-white.csv`
- `winequality.names`

The dataset is automatically downloaded inside the notebook for reproducibility.

---

## Problem Formulation

I converted the original wine quality score into a **binary classification problem**:

- `1` → High quality wine (quality ≥ 7)  
- `0` → Not high quality wine  

This transformation made the problem more aligned with real-world decision-making scenarios.

---

## Project Structure

```
Lab6/
├── data/
├── artifacts/
├── mlruns/
├── .gitignore
├── requirements.txt
└── Lab6_MLflow_Wine_Quality.ipynb
```

---

## Experiment Workflow

### 1. Data Preparation
- Loaded and merged red + white wine datasets
- Added `is_red` indicator feature
- Cleaned column names
- Verified no missing values

### 2. Train/Validation/Test Split
- Stratified split:
  - 60% train
  - 20% validation
  - 20% test

### 3. Model Training

I trained and compared three models:

- Logistic Regression
- Random Forest
- XGBoost

Each model was wrapped in a preprocessing pipeline.

---

## MLflow Tracking

I configured MLflow with a local tracking URI and logged:

### Parameters
- model-specific hyperparameters
- dataset sizes
- feature count

### Metrics
- accuracy
- precision
- recall
- F1 score
- AUC

### Artifacts
- confusion matrices
- classification reports
- comparison tables
- threshold tuning results

### Models
- each trained model
- final production candidate model

---

## Model Comparison

I compared models using validation metrics and selected the best model based on:

### Selection Criterion:
**Highest Validation AUC**

### Best Model:
**XGBoost**

---

## Evaluation

### Validation Performance (Best Model)
- AUC ≈ 0.89
- F1 ≈ 0.65

### Test Performance
- Accuracy ≈ 0.83
- Precision ≈ 0.54
- Recall ≈ 0.72
- F1 ≈ 0.62
- AUC ≈ 0.88

---

## Advanced Additions

### Threshold Tuning
I evaluated multiple classification thresholds instead of using a fixed 0.5 cutoff.

---

### ROC Curve Comparison
I plotted ROC curves for all models to compare ranking performance.

---

### Precision-Recall Curve
Since the dataset is imbalanced, I used PR curves to better understand performance on the positive class.

---

### Feature Importance
I extracted and visualized feature importance from the best model.

---

### Batch Inference
I demonstrated batch predictions using the final trained model.

---

### Model Registration
I registered the best model in MLflow and verified it by loading it back.

---

## Key Learnings

Through this lab, I learned how to:

- design structured ML experiments
- track experiments using MLflow
- compare models using appropriate metrics
- handle imbalanced classification problems
- move from experimentation to production candidate models
- register and reuse trained models

---

## Conclusion

This lab demonstrates a complete ML lifecycle:

- data ingestion
- preprocessing
- experimentation
- evaluation
- model selection
- production candidate creation
- model registry integration

---

## How to Run

### 1. Setup environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run notebook
Open and run:
```bash
Lab6_MLflow_Wine_Quality.ipynb
```

### 3. Launch MLflow UI
```bash
mlflow ui
```

Open:
http://127.0.0.1:5173
