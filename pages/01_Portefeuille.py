import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf

# Espacement et mise en page
col1, col2 = st.columns([4, 1])  # 4/1 pour placer à droite

with col2:
    if st.button("🚪 Se déconnecter"):
        st.session_state.logged_in = False
        st.switch_page("app.py")  # retour à la page de login

with col1:
    st.title("Dashboard Portefeuille")

st.write("Visualisation des investissements")

# Bouton pour ajouter un investissement
if st.button("Ajouter un investissement"):
    with st.expander("Ajouter un nouvel investissement", expanded=True):
        search_term = st.text_input("Rechercher un titre (ex: NASDAQ:AAPL)")

        if search_term:
            try:
                # Recherche du titre avec yfinance
                ticker = yf.Ticker(search_term)
                info = ticker.info
                st.write(f"Nom: {info['shortName']}")
                st.write(f"Symbole: {info['symbol']}")
                st.write(f"Prix actuel: {info['currentPrice']}")

                # Ajouter des champs pour saisir des informations supplémentaires
                quantity = st.number_input("Quantité", min_value=1, value=1)
                purchase_date = st.date_input("Date d'achat", datetime.today())

                if st.button("Ajouter"):
                    st.success(f"Investissement ajouté: {quantity} unités de {info['symbol']} à {info['currentPrice']} le {purchase_date}")
            except Exception as e:
                st.error("Ticker non trouvé ou erreur de recherche.")

# --- Données fictives de type marché financier
date_rng = pd.date_range(datetime.now() - timedelta(days=30), periods=300, freq='H')
prices = np.cumsum(np.random.randn(len(date_rng))) + 100
df = pd.DataFrame({'Date': date_rng, 'Price': prices})

# --- Graphique interactif
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'], mode='lines', name='Prix'))

# --- Boutons pour changer d’échelle de temps
fig.update_layout(
    title="Évolution du portefeuille",
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1j", step="day", stepmode="backward"),
                dict(count=7, label="1s", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)

st.plotly_chart(fig, use_container_width=True)
