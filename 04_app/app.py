import streamlit as st
from components.resume_card import render_resume_cards
from components.show_plot import render_plots
from components.explain_text import render_explain
import os
# image path
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_web = os.path.join(current_dir,"images", "logo_web.svg")

# config 
st.set_page_config(
    page_title="Inventory Executive Summary",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=logo_web
)

# 🌐 language sidebar
idioma = st.sidebar.selectbox("🌐 Idioma / Language", ["Español", "English"])
st.session_state["idioma"] = idioma

# titles
if idioma == "Español":
    st.header("RESUMEN EJECUTIVO DEL INVENTARIO")
else:
    st.header("EXECUTIVE INVENTORY SUMMARY")

# section cards
render_resume_cards()

# plot section
render_plots()

# explain section
render_explain()