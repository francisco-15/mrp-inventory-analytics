import streamlit as st
from components.resume_card import render_resume_cards
from components.show_plot import render_plots
from components.explain_text import render_explain

# config (Obligatoriamente debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="Resumen Ejecutivo de Inventario / Inventory Executive Summary",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🌐 Selector de idioma centralizado en la barra lateral
idioma = st.sidebar.selectbox("🌐 Idioma / Language", ["Español", "English"])
st.session_state["idioma"] = idioma

# Título principal adaptativo
if idioma == "Español":
    st.header("Resumen ejecutivo del inventario")
else:
    st.header("Executive Inventory Summary")

# section cards
render_resume_cards()

# plot section
render_plots()

# explain section
render_explain()