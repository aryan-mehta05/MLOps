from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Tuple

import joblib
import numpy as np


def project_root() -> Path:
  return Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def load_model():
  """
  Load the model ONCE and cache it.
  This avoids re-loading on every request.
  """
  model_path = project_root() / "model" / "wine_model.joblib"
  if not model_path.exists():
    raise FileNotFoundError(
      f"Model not found at {model_path}. Run training first: python -m src.train"
    )
  return joblib.load(model_path)


@lru_cache(maxsize=1)
def load_metadata() -> Dict[str, Any]:
  meta_path = project_root() / "model" / "metadata.json"
  if not meta_path.exists():
    raise FileNotFoundError(
      f"Metadata not found at {meta_path}. Run training first: python -m src.train"
    )
  return json.loads(meta_path.read_text())


def predict_one(feature_vector: List[float]) -> Tuple[int, str, List[float]]:
  """
  Predict a single row.

  Returns:
    class_id (int)
    class_name (str)
    probabilities (list[float])
  """
  meta = load_metadata()
  class_names = meta["schema"]["class_names"]

  model = load_model()

  X = np.array([feature_vector], dtype=float)
  class_id = int(model.predict(X)[0])

  # LogisticRegression supports predict_proba
  probs = model.predict_proba(X)[0].tolist()
  class_name = class_names[class_id]

  return class_id, class_name, probs


def predict_batch(vectors: List[List[float]]) -> List[Dict[str, Any]]:
  """
  Predict multiple rows in one request.
  """
  results = []
  for v in vectors:
    cid, cname, probs = predict_one(v)
    results.append({"class_id": cid, "class_name": cname, "probabilities": probs})
  return results