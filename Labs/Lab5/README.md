# Lab 5 – GitHub Actions CI for Math Utilities (Testing + Coverage)

**Author:** Aryan Mehta

---

## Overview

This lab implements a **CI-driven testing workflow** using GitHub Actions for a comprehensive Python math utilities module.  
It expands a basic calculator example into a **feature-rich utilities library** with strong validation, extensive unit tests, and automated CI pipelines.

The project demonstrates how to:
- Build a modular Python utility library
- Write thorough test suites using **pytest** and **unittest**
- Achieve **100% test coverage**
- Automate testing with **GitHub Actions**
- Generate and store test artifacts (JUnit XML, coverage reports)

---

## Project Structure

```
MLOps/
├── .github/
│   └── workflows/
│       ├── lab5-pytest.yml
│       └── lab5-unittest.yml
└── Labs/
    └── Lab5/
        ├── data/
        │   └── __init__.py
        ├── src/
        │   ├── __init__.py
        │   └── math_utils.py
        ├── test/
        │   ├── __init__.py
        │   ├── test_pytest.py
        │   └── test_unittest.py
        ├── workflows/ (reference copies)
        ├── .gitignore
        ├── requirements.txt
        └── README.md
```

---

## Features

### Math Utilities Module

The `math_utils.py` file includes **20+ functions**, organized into:

#### 1. Arithmetic Operations
- add
- subtract
- multiply
- divide
- safe_divide

#### 2. Power & Transformations
- power
- square
- cube

#### 3. Numeric Helpers
- modulus
- absolute_value
- round_number
- floor_number
- ceil_number

#### 4. Aggregations
- average
- maximum
- minimum

#### 5. Number Theory
- factorial
- fibonacci
- is_even
- is_odd
- is_prime
- gcd
- lcm

#### 6. Misc Utilities
- percentage
- clamp

> *All functions include:*
> - input validation
> - error handling
> - edge case handling (zero, negatives, booleans, etc.)

---

## Testing Strategy

### Pytest Suite
- Located in `test/test_pytest.py`
- Covers:
  - valid inputs
  - edge cases
  - invalid inputs (exceptions)
  - numeric validation branches

### Unittest Suite
- Located in `test/test_unittest.py`
- Mirrors pytest coverage for redundancy

---

## Coverage

```
Coverage: 100%
```

Achieved by:
- Testing all validation branches
- Testing error conditions explicitly
- Covering loop branches (e.g., prime number logic)

---

## Local Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests Locally

### Pytest

```bash
pytest -v test/test_pytest.py
```

### Unittest

```bash
python -m unittest -v test.test_unittest
```

### Coverage *(Reported in Terminal)*

```bash
pytest -v test/test_pytest.py --cov=src --cov-report=term
```

---

## GitHub Actions CI

Two workflows are configured:

### 1. Pytest CI (`lab5-pytest.yml`)
- Runs pytest
- Generates coverage
- Outputs JUnit report
- Uploads artifacts

### 2. Unittest CI (`lab5-unittest.yml`)
- Runs unittest suite
- Validates core functionality

### Trigger Conditions
- Push to `main`
- Pull requests affecting `Lab5`

---

## CI Improvements Over Professor's Base Lab

- Updated to modern GitHub Actions versions
- Scoped workflows to Lab5 only
- Added coverage reporting
- Added artifact upload
- Improved logging with verbose test output

---

## Key MLOps Concepts Demonstrated

- Continuous Integration (CI)
- Automated testing pipelines
- Test coverage enforcement
- Modular code design
- Validation and error handling
- Artifact generation and storage
- Reproducibility

---

## Conclusion

This lab demonstrates a **production-ready CI pipeline** for Python projects.

By combining:
- a well-structured utility module,
- extensive testing,
- and automated CI workflows,

the project reflects real-world MLOps practices focused on **reliability, scalability, and maintainability**.
