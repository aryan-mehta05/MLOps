from __future__ import annotations

import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


def load_data() -> tuple[np.ndarray, np.ndarray, list[str], list[str]]:
  """
  Load the Wine dataset and return:
    - X: features
    - y: targets
    - feature_names: list of feature names in correct order
    - class_names: list of class names (as strings)

  Why Wine?
    - More realistic than Iris (13 numeric features, 3 classes)
    - Common for multi-class classification demos
  """
  ds = load_wine()
  X = ds.data
  y = ds.target
  feature_names = list(ds.feature_names)
  class_names = [str(c) for c in ds.target_names]
  return X, y, feature_names, class_names


def split_data(
  X: np.ndarray,
  y: np.ndarray,
  test_size: float = 0.25,
  random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
  """
  Split features/targets into train/test sets with stratification.

  Stratification helps preserve class balance in both sets.
  """
  return train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=random_state,
    stratify=y,
  )