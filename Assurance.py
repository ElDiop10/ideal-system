import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import pickle
import joblib

# Charger le modèle
@st.cache_data
def load_model(model_path):
    """Charge le modèle depuis un fichier."""
    return joblib.load(model_path)

# Charger le modèle
model_path = "mm_model.pkl"
model = load_model(model_path)

# Prétraitement des données
def preprocess_data(data):
    categorical_features = ['sex', 'smoker', 'region']
    categorical_transformer = OneHotEncoder()
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features)],
        remainder='passthrough')
    return preprocessor.transform(data)

st.title('Prédiction des Charges Médicales')
st.subheader("Bay El Hadji Ousmane Diop")
st.markdown("Cette application web interactive pour prédire les charges médicales basées sur les caractéristiques des individus, en utilisant le meilleur modèle de régression parmi ceux évalués (Régression Multiple, Ridge, Lasso).")

# Interface utilisateur
age = st.number_input('Âge', min_value=0)
sex = st.selectbox('Sexe', ['male', 'female'])
bmi = st.number_input('BMI', min_value=0.0, format="%.2f")
children = st.number_input('Nombre d\'enfants', min_value=0)
smoker = st.selectbox('Fumeur', ['yes', 'no'])
region = st.selectbox('Région', ['southwest', 'southeast', 'northwest', 'northeast'])

if st.button('Faire une Prédiction'):
    # Préparer les données pour la prédiction
    new_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    # Prétraiter les données
    new_data_preprocessed = preprocess_data(new_data)

    # Faire la prédiction
    prediction = model.predict(new_data_preprocessed)
    st.write(f"La prédiction pour les nouvelles données est : ${prediction[0]:.2f}")
