import streamlit as st
import numpy as np
import joblib

def load_model(model_path):
    """Charge le modèle depuis un fichier."""
    return joblib.load(model_path)

def predict_species(model, input_data):
    """Effectue une prédiction de l'espèce en fonction des données d'entrée."""
    prediction = model.predict(input_data)[0]
    species_names = ['setosa', 'versicolor', 'virginica']
    return species_names[prediction]

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    st.title("Prédiction des espèces d'iris")
    st.subheader("Bay El Hadji Ousmane Diop")
    st.write("Utilisez les valeurs ci-dessous pour prédire l'espèce d'une fleur d'iris.")
    
    # Entrées utilisateur
    sepal_length = st.number_input("Donnez la Longueur du sépale (cm)")
    sepal_width = st.number_input("Donnez la Largeur du sépale (cm)")
    petal_length = st.number_input("Donnez la Longueur du pétale (cm)")
    petal_width = st.number_input("Donnez la Largeur du pétale (cm)")
    
    if st.button("Prédire"):
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Charger le modèle
        model_path = "model_logisticR.pkl"
        model = load_model(model_path)

        # Faire la prédiction
        predicted_species = predict_species(model, input_data)
        
        # Afficher le résultat
        st.success(f"L'espèce prédite est : {predicted_species}")
        


if __name__ == "__main__":
    main()
