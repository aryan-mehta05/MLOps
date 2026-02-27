from __future__ import annotations

import json
from pathlib import Path

import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from .data import load_data, split_data


def project_root() -> Path:
  """
  Returns Lab3/ path regardless of where you run the script from.
  src/train.py -> src -> Lab3
  """
  return Path(__file__).resolve().parents[1]


def train_and_evaluate(random_state: int = 42) -> dict:
  """
  Train a stronger model than a basic decision tree:
    - StandardScaler + LogisticRegression

  Returns a metadata dict including metrics and schema details.
  """
  X, y, feature_names, class_names = load_data()
  X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.25, random_state=random_state)

  model = Pipeline(
    steps=[
      ("scaler", StandardScaler()),
      ("clf", LogisticRegression(max_iter=4000, random_state=random_state)),
    ]
  )

  model.fit(X_train, y_train)

  preds = model.predict(X_test)
  acc = accuracy_score(y_test, preds)

  report = classification_report(y_test, preds, output_dict=True)

  metadata = {
    "dataset": "sklearn.datasets.load_wine",
    "model": "Pipeline(StandardScaler -> LogisticRegression)",
    "random_state": random_state,
    "metrics": {
      "accuracy": acc,
      "classification_report": report,
    },
    "schema": {
      "feature_names": feature_names,
      "class_names": class_names,
      "num_features": len(feature_names),
      "num_classes": len(class_names),
    },
  }
  return model, metadata


def save_artifacts(model, metadata: dict) -> None:
  """
  Save:
    - model/wine_model.joblib
    - model/metadata.json
  """
  root = project_root()
  model_dir = root / "model"
  model_dir.mkdir(parents=True, exist_ok=True)

  model_path = model_dir / "wine_model.joblib"
  meta_path = model_dir / "metadata.json"

  joblib.dump(model, model_path)

  with open(meta_path, "w") as f:
    json.dump(metadata, f, indent=2)

  print("✅ Training complete")
  print(f"✅ Saved model: {model_path}")
  print(f"✅ Saved metadata: {meta_path}")
  print(f"✅ Accuracy: {metadata['metrics']['accuracy']:.4f}")


if __name__ == "__main__":
  model, metadata = train_and_evaluate(random_state=42)
  save_artifacts(model, metadata)