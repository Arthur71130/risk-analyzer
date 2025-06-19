#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 16:12:47 2025

@author: arthurdemacedo
"""

import streamlit as st



import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
st.title("Dashboard Portefeuille")
st.write("Visualisation des investissements")

# --- Données fictives de type marché financier
date_rng = pd.date_range(datetime.now() - timedelta(days=30), periods=300, freq='H')
prices = np.cumsum(np.random.randn(len(date_rng))) + 100
df = pd.DataFrame({'Date': date_rng, 'Price': prices})

# --- Graphique interactif
fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'], mode='lines', name='Prix'))

# --- Boutons pour changer d’échelle de temps
fig.update_layout(
    title="📈 Évolution du portefeuille",
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

# Espacement et mise en page
col1, col2 = st.columns([8, 1])  # 8/1 pour placer à droite

with col2:
    if st.button("🚪 Se déconnecter"):
        st.session_state.logged_in = False
        st.switch_page("app.py")  # retour à la page de login
