# Simple-NN

A simple FastAPI application that serves a neural network model for classifying iris flowers using the classic Iris dataset.

## Features

- RESTful API for iris flower classification
- Simple neural network built with TensorFlow/Keras
- Input validation using Pydantic
- Trained on the Iris dataset (150 samples, 3 classes)

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple-nn
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

### Running the API

Start the FastAPI server:

```bash
uv run uvicorn iris_api.main:app --reload
```

The API will be available at `http://localhost:8000`.

### API Endpoints

#### GET /

Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the Iris API"
}
```

#### POST /predict

Predicts the iris flower class based on sepal and petal measurements.

**Request Body:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**
```json
{
  "Predicted_class": 0
}
```

**Class Labels:**
- 0: Setosa
- 1: Versicolor
- 2: Virginica

## Model Details

- **Architecture**: Simple feedforward neural network
  - Input layer: 4 neurons (sepal length, sepal width, petal length, petal width)
  - Hidden layer: 10 neurons with ReLU activation
  - Output layer: 3 neurons with softmax activation
- **Training**: 100 epochs, batch size 10, Adam optimizer, categorical cross-entropy loss
- **Dataset**: Iris dataset from scikit-learn (train/test split: 80/20)

## Dependencies

- FastAPI
- NumPy
- Pydantic
- scikit-learn
- TensorFlow

## Development

The model is trained when the module is imported. For production use, consider saving and loading the trained model instead of retraining on startup.
