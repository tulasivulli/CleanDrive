# 🚗 CleanDrive – CO₂ Emission Prediction Platform

CleanDrive is a machine learning–based web application that predicts **vehicle CO₂ emissions** using historical vehicle data.  
The platform provides an interactive and user-friendly interface to help users understand how vehicle specifications affect carbon emissions and promote environmentally responsible choices.

---

## 🌟 Features

- 🔐 **User Authentication**
  - Login and registration system for users
- 📊 **CO₂ Emission Prediction**
  - Predicts emissions based on vehicle specifications
- 🤖 **AI Assistant**
  - Helps users understand predictions and system usage
- 📈 **Interactive Dashboard**
  - Displays prediction results and insights
- 🌐 **Web-Based Interface**
  - Simple, clean, and responsive design

---

## 🛠️ Technologies Used

### Frontend
- HTML  
- CSS  

### Backend & Machine Learning
- Python  
- Streamlit  
- Scikit-learn  

---

## 🧠 Machine Learning Training Process

CleanDrive uses **Supervised Machine Learning (Regression)** to predict vehicle CO₂ emissions.

### 🔹 1. Dataset
- Vehicle emission dataset (CSV format)
- Contains features such as:
  - Engine Size
  - Number of Cylinders
  - Fuel Consumption (City / Highway)
  - Fuel Type
  - CO₂ Emissions (target variable)

---

### 🔹 2. Data Preprocessing
- Removed missing and inconsistent values
- Encoded categorical features (Fuel Type)
- Selected relevant features
- Split the dataset into:
  - **Training set (80%)**
  - **Testing set (20%)**

---

### 🔹 3. Model Selection
- **Random Forest Regressor** was chosen because:
  - It handles non-linear data effectively
  - Reduces overfitting
  - Provides better accuracy for regression tasks

---

### 🔹 4. Model Training
The model is trained using Scikit-learn:

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
