# Librerias ----------------------------------------
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier
from sklearn.model_selection import GridSearchCV
import os, sys

# Agregar la carpeta raíz del proyecto a sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

# Ahora importa la clase correctamente
from insight.explora_analysis import ExploraAnalysis  

# Loading data ---------------------------------------- 
url1 = "files/datasets/input/contract.csv"
url2 = "files/datasets/input/internet.csv"
url3 = "files/datasets/input/personal.csv"
url4 = "files/datasets/input/phone.csv"

contract = pd.read_csv(url1)
internet = pd.read_csv(url2)
personal = pd.read_csv(url3)
phone = pd.read_csv(url4)

# Análisis Exploratorio de Datos (EDA) ---------------------------------------- 
eda_contract = ExploraAnalysis(contract,"contract")  # Instancia de la clase ExploraAnalysis
eda_internet = ExploraAnalysis(internet,"internet")
eda_personal = ExploraAnalysis(personal,"personal")
eda_phone = ExploraAnalysis(phone,"phone")

# EDA de contract --------------------------------------------------------------
print("\n---------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------------\n")
eda_contract.run_general_analysis()
eda_contract.descriptive_analysis()
#eda_contract.run_visualization_analysis()

# EDA de internet --------------------------------------------------------------
print("\n---------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------------\n")
eda_internet.run_general_analysis()
eda_internet.descriptive_analysis()
#eda_internet.run_visualization_analysis()

# EDA de personal --------------------------------------------------------------
print("\n---------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------------\n")
eda_personal.run_general_analysis()
eda_personal.descriptive_analysis()
#eda_personal.run_visualization_analysis()

# EDA de phone --------------------------------------------------------------
print("\n---------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------------\n")
eda_phone.run_general_analysis()
eda_phone.descriptive_analysis()
#eda_phone.run_visualization_analysis()
