import streamlit as st
from db.queries import unspecified_dept_outputs, get_economic_impact_unspecified, get_economic_impact_dead_stock, \
get_economic_impact_a_class

def render_resume_cards():
    # data
    df_unspecified_dept = unspecified_dept_outputs()
    count_unspecified_dept = df_unspecified_dept.iloc[0, 0]
    impact_unspecified = get_economic_impact_unspecified().iloc[0, 0]
    impact_dead_stock = get_economic_impact_dead_stock().iloc[0, 0]
    impact_a_class = get_economic_impact_a_class().iloc[0, 0]

    # styles
    # Icono centrado en una caja de 95px
    icon_style = "display: flex; justify-content: center; align-items: center; height: 95px; font-size: 3rem; margin: 0;"
    # Títulos y datos con fuentes aumentadas
    title_style = "margin: 0; color: #64748b; font-size: 1.1rem; font-weight: 500;"
    value_style = "margin: 0; font-size: 1.8rem; font-weight: 700; color: #0f172a;"
    sub_style = "margin: 0; font-size: 1rem; font-weight: 600;"

    col1, col2, col3 = st.columns(3)

    # firts card ----> unspecified_dept
    with col1:
        with st.container(border=True):
            c1, c2 = st.columns([1, 3.5])
            with c1:

                st.image("./images/box.png", width=300)
            with c2:
                st.markdown(f"<p style='{title_style}'>Materiales Sin Depto.</p>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='{value_style} color:#991b1b;'>${impact_unspecified:,.2f}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='{sub_style} color:#d97706;'>⚠️ {count_unspecified_dept} salidas sin asignar</p>", unsafe_allow_html=True)

    # second card ------> dead stock
    with col2:
        with st.container(border=True):
            c1, c2 = st.columns([1, 3.5])
            with c1:
                st.image("./images/dead_stock.png", width=300)
            with c2:
                st.markdown(f"<p style='{title_style}'>Valor Stock Muerto</p>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='{value_style} color:#991b1b;'>${impact_dead_stock:,.2f}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='{sub_style} color:#dc2626;'>🚨 Riesgo en Almacén</p>", unsafe_allow_html=True)

    # third card -------> economic value A class
    with col3:
        with st.container(border=True):
            c1, c2 = st.columns([1, 3.5])
            with c1:
                st.image("./images/a_class.png", width=100)
            with c2:
                st.markdown(f"<p style='{title_style}'>Impacto Econ. Clase A</p>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='{value_style} color:#15803d'>${impact_a_class:,.2f}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='{sub_style} color:#22c55e;'>💸 79,32% Valor Inventario</p>", unsafe_allow_html=True)