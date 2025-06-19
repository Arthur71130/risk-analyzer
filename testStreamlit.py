import streamlit as st
import pandas as pd
import datetime

# Configuration de la page
st.set_page_config(page_title="📊 Analyse de Risque", layout="wide")

# Titre
st.title("📈 Analyse de Risque de Portefeuille (DEMO)")

st.markdown("Cette interface est un test de structure pour ton futur outil.")

# Upload de fichier
st.header("1️⃣ Charger un portefeuille")
uploaded_file = st.file_uploader("📁 Upload d’un CSV contenant les colonnes : `Ticker`, `Poids`", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Données chargées :")
    st.dataframe(df)
else:
    st.warning("Aucun fichier chargé.")

# Sélection de période
st.header("2️⃣ Définir la période d'analyse")

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Date de début", datetime.date(2020, 1, 1))
with col2:
    end_date = st.date_input("Date de fin", datetime.date(2024, 1, 1))

# Choix de la méthode d'analyse
st.header("3️⃣ Méthode d’analyse")

method = st.selectbox("Choisir une méthode de risque", ["VaR", "CVaR", "Volatilité"])

# Bouton de lancement
st.header("4️⃣ Lancer l’analyse")

if st.button("🚀 Exécuter (test)"):
    st.info(f"📌 Analyse en cours avec la méthode : **{method}**")
    st.write("⚠️ Ceci est une simulation – aucune donnée réelle traitée.")
