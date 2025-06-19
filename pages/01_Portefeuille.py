#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 16:12:47 2025

@author: arthurdemacedo
"""

import streamlit as st

st.title("Dashboard Portefeuille")
st.write("Visualisation des investissements")


# Option de déconnexion
if st.button("Se déconnecter"):
    st.session_state.logged_in = False
    st.switch_page("app.py")
