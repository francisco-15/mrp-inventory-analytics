import streamlit as st
from components.resume_card import render_resume_cards

st.set_page_config(
    page_title="Resumen Ejecutivo de Inventario",
    layout="wide",
    initial_sidebar_state="expanded"
    
)
st.header("Resumen ejecutivo del inventario")

# section cards
render_resume_cards()