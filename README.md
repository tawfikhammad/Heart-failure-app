# Heart Failure Prediction App

An application that predicts the likelihood of heart failure based on various health parameters using machine learning algorithms.

## Introduction
This project aims to provide a predictive analysis tool for heart failure. By leveraging machine learning techniques, the app analyzes user input data to assess the risk of heart failure.

## Dataset
The dataset used for training the model includes the following features:

- **Age**: Age of the patient [years]
- **Sex**: Sex of the patient [M: Male, F: Female]
- **ChestPainType**: Chest pain type 
  - TA: Typical Angina
  - ATA: Atypical Angina
  - NAP: Non-Anginal Pain
  - ASY: Asymptomatic
- **RestingBP**: Resting blood pressure [mm Hg]
- **Cholesterol**: Serum cholesterol [mm/dl]
- **FastingBS**: Fasting blood sugar 
  - 1: if FastingBS > 120 mg/dl
  - 0: otherwise
- **RestingECG**: Resting electrocardiogram results 
  - Normal: Normal
  - ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
  - LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria
- **MaxHR**: Maximum heart rate achieved [Numeric value between 60 and 202]
- **ExerciseAngina**: Exercise-induced angina 
  - Y: Yes
  - N: No
- **Oldpeak**: Oldpeak = ST [Numeric value measured in depression]
- **ST_Slope**: The slope of the peak exercise ST segment
  - Up: upsloping
  - Flat: flat
  - Down: downsloping
- **HeartDisease**: Output class 
  - 1: Heart disease
  - 0: Normal


## Features
- **Prediction**: Predicts the risk of heart failure based on user-provided health data.
- **User-Friendly Interface**: Use streamlit for easy input and output display for users.
- **Data Analysis**: Utilizes advanced machine learning algorithms for accurate predictions.

## Technology Stack

Jupyter Notebook | scikit-learn | pandas | numpy | matplotlib 

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/tawfikhammad/Heart-failure-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Heart-failure-app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

