Employee Retention Prediction

This repository contains a machine-learning project to predict employee job-change/retention (binary classification).
The goal is to identify employees likely to leave so businesses can take proactive retention actions.
The project includes data preprocessing, feature engineering, model training (LightGBM used as best model), evaluation. 
A Streamlit app for interactive predictions. See the project brief and workflow in the project documentation.


App.py                       <- Streamlit app for live predictions. :contentReference[oaicite:4]{index=4}
job_change_model.pkl         <- Trained model artifact (LightGBM best model)
aug_train.csv                <- Training dataset
aug_test.csv                 <- Test dataset
notebooks/                   <- Exploratory notebooks & training scripts (if present)
requirements.txt             <- Python package requirements
Capstone PPT .pptx           <- Project presentation / documentation. :contentReference[oaicite:5]{index=5}
