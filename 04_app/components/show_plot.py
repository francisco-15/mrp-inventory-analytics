import streamlit as st
from db.queries import plot_financial_supplier_summary, get_unassigned_materials, get_economic_impact_by_department
from components.engine_plot import engine
import seaborn as sns
import matplotlib.pyplot as plt

def render_plots():
    # data
    df_financial = plot_financial_supplier_summary() 
    df_unassigned_materials = get_unassigned_materials()
    df_economic_impact_by_department = get_economic_impact_by_department()

    # capture the global language
    language = st.session_state.get("idioma", "Español")

    # mapping of chart titles
    tile_plot = {
        "Español": {
            "p1": "MATERIALES EMITIDOS SIN DEPARTAMENTO",
            "p2": "Inversión Histórica en Adquisiciones por Proveedor",
            "p3": "Valor económico de materiales entregados por cada departamento"
        },
        "English": {
            "p1": "MATERIALS ISSUED WITHOUT DEPARTMENT",
            "p2": "Historical Procurement Investment by Supplier",
            "p3": "Economic Value of Materials Delivered by Each Department"
        }
    }

    # colors
    color1 = {'A': '#9B2226', 'B': '#CA6702', 'C': '#EE9B00', 'DEAD STOCK': '#AEB6BF'}
    color2 = {
        "RUBBER SPLICING TAPE 23": "#1f77b4",
        "ELECTRICAL TAPE 33": "#ff7f0e",
        "LEATHER GLOVES": "#2ca02c",
        "TERMINAL TYPE BARRACUDA 2/0": "#d62728",
        "1 1/4\" X 25 FT PIN X PIN ROD": "#9467bd",
        "LARGE BLACK TIRAP": "#8c564b",
        "TERMINAL TYPE BARRACUDA BIMETAL...": "#e377c2",
        "POLYPROPYLENE SAFETY HELMET...": "#7f7f7f"
    }
    
    col1, col2, col3 = st.columns(3)

    with col1:
         # count frequency of materials
         df_frequency = df_unassigned_materials['MATERIAL'].value_counts().reset_index()
         df_frequency.columns = ['MATERIAL', 'FREQUENCE']
         plot1 = {tile_plot[language]["p1"]: df_frequency}
         engine_plot1 = engine(
                        plot1,
                        'pie',
                        x_axis='MATERIAL',
                        y_axis='FREQUENCE',
                        palette=color2
         )

    with col2:
         # plot financial summary
         plot2 = {tile_plot[language]["p2"]: df_financial}
         engine_plot2 = engine(
                        plot2,
                         'bar',
                         'SUPPLIER',
                         'TOTAL_AMOUNT',
                         hue='ABC_CLASSIFICATION',
                         palette=color1,
                         unit='$'
         )

    with col3:
         # plot economic impact by department
         plot3 = {tile_plot[language]["p3"]: df_economic_impact_by_department}
         engine_plot3 = engine(plot3,
                         'bar',
                         'ECONOMIC_IMPACT',
                         'REQUESTING_DEPARTMENT',
                         hue='ABC_CLASSIFICATION',
                         palette='Set1',
                         unit='$',
                         use_formatter=True
                         )