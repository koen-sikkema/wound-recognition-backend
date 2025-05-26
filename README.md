# Wound Recognition Backend

This repository contains the backend for a wound recognition application using machine learning.

## Overview

This backend service handles image uploads, processes images through a machine learning model, stores prediction results, and provides API endpoints to interact with these functionalities.

## Features

- Upload wound images for prediction
- Process images with a TensorFlow/Keras ML model
- Store prediction results in a SQLite database
- Retrieve, delete, and list prediction history
- Designed with a service-based architecture
- Includes unit and integration tests

## Requirements

- Python 3.9+
- FastAPI
- SQLAlchemy
- TensorFlow
- Other dependencies listed in `requirements.txt`

## Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/koen-sikkema/wound-recognition-backend.git
   cd wound-recognition-backend
   ``` 

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix or MacOS
    venv\Scripts\activate     # For Windows
    ```

3. **Install dependencies:**
   ```py
   pip install -r requirements.txt
   ```

4. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

The API is now accessible at http://127.0.0.1:8000, with interactive documentation available at http://127.0.0.1:8000/docs.

## Testing
   ```bash 
   pytest -v
   ``` 

## Project structure
```py
wound-recognition-backend/
├── app/
│   ├── core/          # Configurations and utilities
│   ├── crud/          # Database operations
│   ├── database/      # Database initialization
│   ├── ml_manager/    # Machine learning model management
│   ├── routers/       # API routes
│   ├── schemas/       # Pydantic schemas
│   └── main.py        # Application entry point
├── tests/             # Unit and integration tests
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```
## 📄 API Endpoints

*  POST /upload/ - Upload a wound image.

* GET /result/{filename} - Retrieve the prediction result for a specific image.

* GET /predictions/ - View all stored predictions.

* DELETE /predictions/ - Delete all predictions from the database.

## 📄 License 

This license applies to the Machine learning-model: best_cnn.h5 

Enormously gratefull to [Fahim Ahamed!] (https://github.com/f-a-tonmoy/Wound-Classification-DL?tab=readme-ov-file)


MIT License

Copyright (c) 2025 Fahim Ahamed (Tonmoy)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

👤 Author
Koen Sikkema - Under the supervision of Egbert Wiltens in name of [Health-Hub Roden](https://www.health-hub.eu/)