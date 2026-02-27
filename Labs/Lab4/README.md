# Lab 4: Model Development with Ray (Parallel Model Training Benchmark)

## Overview

This lab demonstrates scalable model development using **Ray** to
parallelize hyperparameter experimentation.\
I benchmark sequential vs parallel model training and quantify
performance gains using wall-clock runtime and model accuracy.

Enhancements beyond the base implementation include:

-   Structured hyperparameter grid experimentation
-   Sequential baseline benchmarking
-   Ray-based parallel execution using remote tasks
-   Speedup calculation and runtime comparison
-   Visualization of model performance trends
-   Residual diagnostics for sanity checking
-   Artifact persistence (model + metrics + benchmark summary)

This mirrors a realistic MLOps experimentation workflow where
reproducibility, scalability, and performance tracking are essential.

------------------------------------------------------------------------

## Dataset

-   Source: `sklearn.datasets.fetch_california_housing` (same as the professor but the implementation is completely different.)
-   Problem Type: Regression
-   Target: Median house value
-   Split: 80% train / 20% test
-   Random state: 42

------------------------------------------------------------------------

## Model

-   Algorithm: `RandomForestRegressor`
-   Hyperparameters explored:
    -   `n_estimators`
    -   `max_depth`
    -   `min_samples_leaf`
-   Internal parallelism disabled (`n_jobs=1`) to allow Ray to manage
    distributed execution efficiently.

------------------------------------------------------------------------

## Experimental Design

### 1️⃣ Sequential Baseline

All hyperparameter configurations are trained sequentially to establish
a runtime baseline.

### 2️⃣ Ray Parallel Execution

Parallel execution is implemented using:

-   `ray.init()`
-   `ray.put()` for shared object storage
-   `@ray.remote` for distributed execution
-   `ray.get()` for collecting results

This enables concurrent model training across CPU cores.

------------------------------------------------------------------------

## Speedup Formula

A speedup greater than 1 indicates the parallel approach is faster.

$$
\text{Speedup} = \frac{T_{\text{sequential}}}{T_{\text{parallel}}}
$$

> The speedup that I got for this run is: `4.39` \
> This suggests that my *parallel* model is **4.39x faster** than my *sequential* model.

------------------------------------------------------------------------

## Results

The notebook generates:

-   Runtime comparison (Sequential vs Ray Parallel)
-   Speedup factor calculation
-   Best-performing hyperparameter configuration
-   Top 5 configurations table
-   MSE performance visualization
-   Residual distribution plot for model diagnostics

------------------------------------------------------------------------

## Artifacts Saved

The following artifacts are stored in the `artifacts/` directory:

-   `best_model.joblib` -- Final trained model using the best
    configuration
-   `metrics.json` -- Contains:
    -   Best hyperparameter configuration
    -   Final MSE
    -   Sequential runtime
    -   Parallel runtime
    -   Speedup factor
-   `benchmark_summary.csv` -- Structured runtime comparison table

These outputs ensure reproducibility and experiment traceability.

------------------------------------------------------------------------

## Key MLOps Concepts Demonstrated

-   Parallel experimentation with Ray
-   Efficient object sharing with `ray.put`
-   Hyperparameter search benchmarking
-   Runtime performance measurement
-   Model selection workflow
-   Artifact persistence
-   Residual analysis for quality validation
-   Structured experiment tracking

------------------------------------------------------------------------

## How to Run

Install dependencies:

``` bash
pip install ray scikit-learn pandas matplotlib joblib
```

Run the notebook cells sequentially.

------------------------------------------------------------------------

## Conclusion

> This lab showcases how distributed execution significantly accelerates
model experimentation workflows.

By combining benchmarking, visualization, and artifact persistence, the
notebook reflects a production-aligned model development pipeline
grounded in modern MLOps practices.
