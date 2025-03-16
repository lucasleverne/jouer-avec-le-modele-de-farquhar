# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 08:15:18 2025

@author: LEVERNE
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def farquhar_model(Ci, Vcmax, Jmax, Rd, Kc, Ko, O, gamma_star):
    """
    Calcule le taux d'assimilation nette de CO2 (A) en fonction de la concentration interne de CO2 (Ci)
    en utilisant le modèle de Farquhar.
    """
    Vc = (Vcmax * (Ci - gamma_star)) / (Ci + Kc * (1 + O / Ko))
    J = (Jmax * (Ci - gamma_star)) / (4 * (Ci + 2 * gamma_star))
    A = min(Vc, J) - Rd
    return A, Vc, J

def plot_farquhar_curve(Vcmax, Jmax, Rd, Kc, Ko, O, gamma_star):
    Ci_values = np.linspace(0, 1000, 400)  # µmol mol-1
    A_values = []
    Vc_values = []
    J_values = []

    for Ci in Ci_values:
        A, Vc, J = farquhar_model(Ci, Vcmax, Jmax, Rd, Kc, Ko, O, gamma_star)
        A_values.append(A)
        Vc_values.append(Vc)
        J_values.append(J)

    plt.figure(figsize=(10, 6))
    plt.plot(Ci_values, A_values, label='Courbe A/Ci', color='blue')
    plt.plot(Ci_values, Vc_values, label='Vc', linestyle='--', color='green')
    plt.plot(Ci_values, J_values, label='J', linestyle='--', color='red')
    plt.xlabel('Concentration interne de CO2 (Ci) (µmol mol-1)')
    plt.ylabel('Taux d\'assimilation nette de CO2 (A) (µmol m-2 s-1)')
    plt.title('Courbe A/Ci avec le modèle de Farquhar')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Interface Streamlit
st.title("Modèle de Farquhar Interactif")

# Curseurs pour les paramètres
Vcmax = st.slider("Vcmax", min_value=10.0, max_value=200.0, value=60.0, step=10.0)
Jmax = st.slider("Jmax", min_value=10.0, max_value=200.0, value=120.0, step=10.0)
Rd = st.slider("Rd", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
Kc = st.slider("Kc", min_value=100.0, max_value=1000.0, value=405.0, step=10.0)
Ko = st.slider("Ko", min_value=100.0, max_value=500.0, value=278.0, step=10.0)
O = st.slider("O", min_value=100.0, max_value=300.0, value=210.0, step=10.0)
gamma_star = st.slider("gamma_star", min_value=10.0, max_value=100.0, value=42.75, step=1.0)

# Afficher le graphique
plot_farquhar_curve(Vcmax, Jmax, Rd, Kc, Ko, O, gamma_star)
