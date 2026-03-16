import joblib
import os
os.getcwd()

model = joblib.load("./models/diabetes_model.pkl")
scaler = joblib.load("./models/scaler.pkl")
paciente = [[2,130,72,22,90,31,0.4,45]]

paciente = scaler.transform(paciente)

pred = model.predict(paciente)

print(pred)
#Anda da una advertencia: UserWarning: X does not have valid feature names, but StandardScaler was fitted with feature names


