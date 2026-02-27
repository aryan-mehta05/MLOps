from __future__ import annotations

from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from .predict import load_metadata, predict_one, predict_batch


app = FastAPI(
  title="Lab 3 - FastAPI ML Inference (Wine Classifier)",
  description="A repurposed MLOps FastAPI lab with a stronger model, richer endpoints, and better artifacts.",
  version="1.0.0",
)


# -----------------------------
# Pydantic Schemas
# -----------------------------
class WineFeatures(BaseModel):
  """
  Request body for a single prediction.

  We take a list of floats in the SAME order as metadata.json feature_names.
  You can view the order using GET /metadata.
  """
  features: List[float] = Field(..., description="Feature vector in metadata feature order.")


class BatchWineFeatures(BaseModel):
  """
  Request body for batch prediction.
  """
  rows: List[List[float]] = Field(..., description="List of feature vectors.")


class PredictionResponse(BaseModel):
  class_id: int
  class_name: str
  probabilities: List[float]


class BatchPredictionResponse(BaseModel):
  results: List[PredictionResponse]


# -----------------------------
# Routes
# -----------------------------
@app.get("/", status_code=status.HTTP_200_OK)
async def root():
  return {"status": "ok", "message": "Wine classifier API is running. Visit /docs."}


@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
  return {"status": "healthy"}


@app.get("/metadata", status_code=status.HTTP_200_OK)
async def metadata():
  """
  Returns feature order, class names, and training metrics.
  """
  try:
    return load_metadata()
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict", response_model=PredictionResponse)
async def predict(payload: WineFeatures):
  """
  Predict a single sample.
  """
  try:
    meta = load_metadata()
    expected = meta["schema"]["num_features"]
    if len(payload.features) != expected:
      raise HTTPException(
        status_code=400,
        detail=f"Expected {expected} features, got {len(payload.features)}. See /metadata for feature order.",
      )

    cid, cname, probs = predict_one(payload.features)
    return {"class_id": cid, "class_name": cname, "probabilities": probs}

  except HTTPException:
    raise
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict_batch", response_model=BatchPredictionResponse)
async def predict_batch_route(payload: BatchWineFeatures):
    """
    Predict multiple samples in one request.
    """
    try:
        meta = load_metadata()
        expected = meta["schema"]["num_features"]

        for i, row in enumerate(payload.rows):
            if len(row) != expected:
                raise HTTPException(
                    status_code=400,
                    detail=f"Row {i} expected {expected} features, got {len(row)}. See /metadata for feature order.",
                )

        raw = predict_batch(payload.rows)
        return {"results": raw}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))