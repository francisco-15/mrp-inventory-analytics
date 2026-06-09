import streamlit as st
from components.resume_card import render_resume_cards
from components.show_plot import render_plots
from components.explain_text import render_explain

# config
st.set_page_config(
    page_title="Resumen Ejecutivo de Inventario",
    layout="wide",
    initial_sidebar_state="expanded"
    
)
st.header("Resumen ejecutivo del inventario")

# section cards
render_resume_cards()

# plot section
render_plots()

# explain section
render_explain()