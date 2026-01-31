import argparse
import json
from pathlib import Path

import joblib
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def parse_args():
    parser = argparse.ArgumentParser(description="Train a RandomForest model on the Wine dataset.")
    parser.add_argument("--test-size", type=float, default=0.2, help="Test split size (default: 0.2)")
    parser.add_argument("--n-estimators", type=int, default=200, help="Number of trees (default: 200)")
    parser.add_argument("--random-state", type=int, default=42, help="Random seed (default: 42)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Ensure artifacts directory exists
    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Load a different dataset than Iris (modification)
    data = load_wine()
    X, y = data.data, data.target

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.random_state, stratify=y
    )

    # Train model
    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        random_state=args.random_state,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds, output_dict=True)

    # Save artifacts
    joblib.dump(model, artifacts_dir / "wine_model.pkl")

    metrics = {
        "dataset": "load_wine",
        "test_size": args.test_size,
        "n_estimators": args.n_estimators,
        "random_state": args.random_state,
        "accuracy": acc,
        "classification_report": report
    }
    with open(artifacts_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("--> Model training complete!\n")
    print(f"Accuracy: {acc:.4f}\n")
    print("Saved: artifacts/wine_model.pkl\n")
    print("Saved: artifacts/metrics.json\n")


if __name__ == "__main__":
    main()
