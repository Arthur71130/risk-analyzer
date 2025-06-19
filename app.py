import streamlit as st
import pandas as pd
import datetime


st.write("Bienvenue")

# Initialiser session_state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Fonction de "connexion" fictive
def login():
    if st.session_state.username == "admin" and st.session_state.password == "pass":
        st.session_state.logged_in = True
        st.success("Connexion réussie !")
    else:
        st.error("Identifiants incorrects.")

# Si pas connecté, on affiche la page de connexion
if not st.session_state.logged_in:
    st.title("🔐 Connexion")
    st.text_input("Nom d'utilisateur", key="username")
    st.text_input("Mot de passe", type="password", key="password")
    st.button("Se connecter", on_click=login)
    st.stop()  # ⛔ Empêche de charger la suite de l'app
else:
    st.switch_page("pages/1_Portefeuille.py")  # Redirection vers une vraie page
