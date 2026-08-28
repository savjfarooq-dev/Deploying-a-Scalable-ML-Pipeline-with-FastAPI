# Deploying a Scalable ML Pipeline with FastAPI

This project implements a machine learning pipeline for predicting whether or not an individual's annual income is greater than $50,000 using Census data from 1994. The project includes model training and evaluation, categorical slice performance analysis, unit testing, continuous integration, and a FastAPI
application for model inference.

## Project Repository

GitHub Repository:
https://github.com/savjfarooq-dev/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

## Environment Setup

The project was developed using Python 3.10.

A Conda environment can be created  by using the supplied file: environment.yml

## Data

The model uses the Census Income dataset contained in:

data/census.csv

## Unit Tests

The project includes three unit tests covering:

- Label conversion
- Model training
- Model metric calculations

## Continuous Integration

GitHub Actions is configured to run automated testing and flake8 checks
when changes are pushed to the repository.

The project currently passes both the pytest and flake8 checks.

## API

A RESTful API is implemented using FastAPI.

The API provides:

- GET / - Returns a welcome message.
- POST / data/ - Accepts Census data and returns a model prediction.

## Project Supporting Documents

Required project screenshots are stored in the screenshots/ directory,
including:
- continuous_integration.png
- local_api.png
- unit_test.png

## Model Card

The model card is contained in `model_card.md` documents the model details, intended use, training and evaluation data, performance metrics, ethical considerations, caveats, and recommendations.