🎗️ SheCare AI — Breast Cancer Detection Model
SheCare AI is a machine learning model that detects breast cancer risk from medical data. It is the AI engine powering the SheCare platform, designed to support early detection and women's health awareness.
 Model Performance
MetricScoreAccuracy94.74%AUC0.9931Log Loss0.1819
The model correctly diagnoses 94 out of 100 patients.

Features

✅ Binary classification — Benign vs Malignant
✅ Trained on the Wisconsin Breast Cancer Dataset (569 patients, 30 features)
✅ LightGBM model with feature engineering
✅ REST API with FastAPI
✅ Ready to connect to the SheCare frontend


 Project Structure
shecare-ai/
│
├── CancerPrediction.ipynb   # Model training notebook
├── braintumor.ipynb         # Brain tumor detection notebook
├── api.py                   # FastAPI REST API
├── cancer_model.pkl         # Trained model (generated after training)
├── scaler.pkl               # Data scaler (generated after training)
├── requirements.txt         # Python dependencies
└── README.md

 Installation
bashgit clone https://github.com/tarek-brahimi/shecare-ai.git
cd shecare-ai
pip install -r requirements.txt

 Train the Model
Open and run CancerPrediction.ipynb in Jupyter Notebook:
bashjupyter notebook CancerPrediction.ipynb
This will generate cancer_model.pkl and scaler.pkl.

 Run the API
bashpython -m uvicorn api:app --reload
API will be live at: http://127.0.0.1:8000

📡 API Endpoints
GET /
Check if the API is running.
Response:
json{
  "message": "SheCare AI est en ligne "
}

POST /predict
Run a breast cancer risk assessment.
Request body:
json{
  "features": [17.99, 10.38, 122.8, 1001.0, 0.1184, ...]
}

 Must contain exactly 30 numeric values (medical measurements).

Response:
json{
  "resultat": "Bénin ",
  "probabilite": 0.9231,
  "message": "Consulte un médecin pour confirmation"
}
FieldDescriptionresultat"Bénin" or "Malin "probabiliteConfidence score between 0 and 1messageRecommendation message

🔗 Frontend Integration
This API is connected to the SheCare Compass frontend.
User types "scan" in chat
        ↓
SheCare Frontend (React)
        ↓
POST /predict
        ↓
FastAPI + LightGBM Model
        ↓
Returns diagnosis result

Top Features Used by the Model

worst_perimeter — Size of the tumor
worst_radius — Radius of the tumor
worst_concave_points — Concavity of the tumor boundary
mean_concave_points — Average concavity
worst_texture — Texture variation


 Tech Stack

Python 3.10+
LightGBM — Gradient boosting model
Scikit-learn — Data preprocessing
FastAPI — REST API
Uvicorn — ASGI server
Pandas / NumPy — Data manipulation

 Author
Tarek Brahimi

GitHub: @tarek-brahimi


Disclaimer
This tool is for educational and research purposes only. It is not a substitute for professional medical advice. Always consult a qualified healthcare provider for medical decisions.