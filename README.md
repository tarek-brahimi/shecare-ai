🧠 SheCare AI - Breast Cancer Detection
📌 Overview

SheCare AI is a machine learning project that helps detect breast cancer from medical data/images.
It is part of the SheCare platform, designed to support early detection and awareness.

🚀 Features
AI model for classification (benign / malignant)
Data preprocessing pipeline
Training script
Prediction (inference) support
Ready for integration with frontend (SheCare app)
🧠 Model Information
Type: Machine Learning / Deep Learning model
Output: Binary classification
Benign
Malignant
Framework: (add here → TensorFlow / PyTorch / Sklearn depending on your repo)
📁 Project Structure
shecare-ai/
│
├── data/              # Dataset files
├── model/             # Trained model
├── training.py        # Model training script
├── inference.py      # Prediction script
├── utils.py           # Helper functions
└── README.md
⚙️ Installation
git clone https://github.com/tarek-brahimi/shecare-ai.git
cd shecare-ai
pip install -r requirements.txt
🧪 Usage
1. Train model
python training.py
2. Run prediction
python inference.py
🔗 Integration with Frontend

This model is designed to be connected to the SheCare frontend application.

Future version:

API using FastAPI / Flask
Endpoint: /predict
📊 Goal

The goal of this project is to improve early breast cancer detection using AI and make it accessible through a simple web interface.

👨‍💻 Author

Tarek Brahimi