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
        # Liste des marchés boursiers populaires
        markets = {
            "NASDAQ:AAPL": "Apple Inc.",
            "NYSE:MSFT": "Microsoft Corporation",
            "NASDAQ:GOOGL": "Alphabet Inc.",
            "NYSE:BRK-A": "Berkshire Hathaway Inc.",
            "NASDAQ:AMZN": "Amazon.com Inc."
        }

        # Sélection du marché boursier
        market_choice = st.selectbox("Choisissez un marché boursier", list(markets.keys()), format_func=lambda x: markets[x])

        if market_choice:
            try:
                # Récupération des informations du marché
                ticker = yf.Ticker(market_choice)
                info = ticker.info
                st.write(f"Nom: {info['shortName']}")
                st.write(f"Symbole: {info['symbol']}")
                st.write(f"Prix actuel: {info['currentPrice']}")

                # Ajouter des champs pour saisir des informations supplémentaires
                amount = st.number_input("Montant", min_value=0.01, value=100.0, step=0.01)
                purchase_date = st.date_input("Date d'achat", datetime.today())

                if st.button("Ajouter"):
                    st.success(f"Investissement ajouté: {amount} USD de {info['symbol']} à {info['currentPrice']} le {purchase_date}")
            except Exception as e:
                st.error("Erreur lors de la récupération des informations du marché.")

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
