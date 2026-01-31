# Lab 1 - Dockerized Model Training (Modified)

This lab trains a RandomForest model on the **Wine dataset** (not Iris), evaluates it, and saves artifacts.

## Build the Docker Image
From inside `MLOps/Labs/Lab1`:

```bash
docker build -f dockerfile -t lab1:v2 .
```

Run with custom parameters:

```bash
mkdir -p artifacts
docker run --rm -v "$(pwd)/artifacts:/app/artifacts" lab1:v2 --n-estimators 500 --test-size 0.3
```

---

## Lab Overview & Modifications

In this lab, I implemented a fully Dockerized machine learning training pipeline using Python and scikit-learn. The container trains a Random Forest classifier on the Wine dataset, evaluates model performance using accuracy and a classification report, and saves both the trained model and evaluation metrics as reproducible artifacts. To ensure this lab is not identical to the original template, I replaced the dataset, added configurable hyperparameters via command-line arguments, and introduced an artifact-driven workflow that persists outputs outside the container using Docker volume mounts. This approach reflects real-world MLOps practices by emphasizing reproducibility, parameterization, and separation of code, data, and artifacts.
