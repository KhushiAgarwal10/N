# Network Security ML Project

## Project Overview

This project is an end-to-end Machine Learning pipeline for Network Security applications. The project includes:

* Data ingestion
* Data validation
* Data transformation
* Model training
* Model evaluation
* FastAPI integration
* MLflow tracking
* MongoDB connection

The project is designed using modular programming and production-level ML pipeline architecture.

---

# Project Architecture

```text
NetworkSecurity/
│
├── app.py
├── requirements.txt
├── setup.py
├── .env
├── README.md
├── artifacts/
├── notebook/
├── networksecurity/
│   ├── components/
│   ├── pipeline/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── utils/
│   ├── constant/
│
├── templates/
└── logs/
```

---

# Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Programming Language  |
| FastAPI      | Backend API           |
| Uvicorn      | ASGI Server           |
| MongoDB      | Database              |
| MLflow       | Experiment Tracking   |
| Scikit-learn | Machine Learning      |
| Pandas       | Data Processing       |
| NumPy        | Numerical Computation |

---

# Virtual Environment Setup

The project already uses a virtual environment named `myenv`.

Activate virtual environment:

## Windows

```bash
myenv\Scripts\activate
```

After activation:

```bash
(myenv) PS E:\NetworkSecurity>
```

## Linux / Mac

```bash
source myenv/bin/activate
```

---

# Install Dependencies

Create a `requirements.txt` file.

```txt
python-dotenv
pandas
numpy
scikit-learn
seaborn
matplotlib
pymongo==3.12.0
certifi
pyaml
mlflow
fastapi
uvicorn
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# Upgrade Pip

```bash
python.exe -m pip install --upgrade pip
```

---

# MongoDB Setup

Create a MongoDB Atlas account.

Steps:

1. Create cluster
2. Create database user
3. Add IP address
4. Copy connection string

Example connection string:

```python
mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

---

# Create `.env` File

```env
MONGO_DB_URL=your_mongodb_connection_string
```

---

# Verify MongoDB Connection

```python
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("MONGO_DB_URL"))
```

---

# Setup Project Package

Create `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Khushi Agarwal",
    packages=find_packages()
)
```

Install local package:

```bash
pip install -e .
```

---

# Logging Module

Logging helps track project execution and errors.

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Project Started")
```

---

# Exception Handling

Custom exception handling improves debugging.

Example:

```python
class NetworkSecurityException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        super().__init__(self.error_message)
```

---

# Training Pipeline

The ML pipeline automates:

```text
Data Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Model Training
      ↓
Model Evaluation
```

---

# MLflow Setup

MLflow is used for:

* experiment tracking
* model logging
* parameter logging
* metric tracking

Start MLflow UI:

```bash
mlflow ui
```

Default URL:

```text
http://127.0.0.1:5000
```

---

# FastAPI Setup

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Create `app.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Network Security Project Running"}
```

---

# Run FastAPI Application

Run server using Uvicorn:

```bash
uvicorn app:app --reload
```

Server runs on:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Uvicorn

Uvicorn is an ASGI server used to run FastAPI applications.

Responsibilities:

* Runs FastAPI server
* Handles requests
* Supports asynchronous APIs
* Provides hot reload during development

Example:

```bash
uvicorn app:app --reload
```

---

# Features Implemented Till Now

* Virtual environment setup
* Requirements installation
* MongoDB connection
* Environment variables
* Package setup
* Logging module
* Exception handling
* Training pipeline structure
* MLflow integration
* FastAPI setup
* Uvicorn server setup

---

# Future Improvements

* Docker integration
* AWS deployment
* CI/CD pipeline
* Model monitoring
* Kubernetes deployment
* Automated retraining pipeline

---

# Author

Khushi Agarwal
