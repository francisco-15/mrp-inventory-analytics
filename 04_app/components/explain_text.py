import streamlit as st
from db.queries import unspecified_dept_outputs, get_economic_impact_unspecified, get_economic_impact_dead_stock, \
get_economic_impact_a_class, plot_financial_supplier_summary, get_unassigned_materials, get_economic_impact_by_department

def render_explain():
    # data
    df_financial = plot_financial_supplier_summary() 
    df_unassigned_materials = get_unassigned_materials()
    df_economic_impact_by_department = get_economic_impact_by_department()
    df_unspecified_dept = unspecified_dept_outputs()
    count_unspecified_dept = df_unspecified_dept.iloc[0, 0]
    impact_unspecified = get_economic_impact_unspecified().iloc[0, 0]
    impact_dead_stock = get_economic_impact_dead_stock().iloc[0, 0]
    impact_a_class = get_economic_impact_a_class().iloc[0, 0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Materiales Emitidos sin Departamento")
        st.write(
             "Se registraron **16 salidas de almacén sin asignar**, lo que significa que se desconoce el "
             "departamento de destino final que recibió dichos insumos. Este vacío de trazabilidad representa "
             "un coste económico acumulado de **$7,509.41 USD**."
         )
         
        st.markdown("**Distribución porcentual por tipo de material:**")
        st.markdown(
             """
             * 🔴 **Rubber Splicing Tape 23:** 25.0% de las salidas.
             * 🔵 **Electrical Tape 33:** 25.0% de las salidas.
             * 🟢 **Leather Gloves:** 12.5% de las salidas.
             * 🟣 **Terminal Type Barracuda 2/0:** 12.5% de las salidas.
             * 🟠 **Otros materiales menores (4 tipos distintos):** 6.2% cada uno *(Pin Rod, Black Tirap, Barracuda Bimetal y Safety Helmet)*.
             """
         )
        
    with col2:
        # --- Sección de Resumen Ejecutivo: Impacto de Suministros y Alerta de Stock Muerto ---
        st.markdown("### 📊 Hallazgos Críticos de Stock Muerto e Impacto Operativo")
        
        st.write(
            "El análisis del inventario revela una acumulación crítica de **Stock Muerto** (materiales sin rotación) "
            "valorada en **\$2,706,061.36 USD**. Esta inmovilización de capital representa un riesgo inminente de "
            "obsolescencia o pérdida física en insumos de alta rotación como **Nitrile Gloves (Guantes de Nitrilo)**, "
            "los cuales saturan el espacio de almacenamiento sin generar valor operativo."
        )
        
        # --- Sección de Resumen Ejecutivo para Gráfico 2 (CORREGIDO - ANÁLISIS DE PROVEEDOR Y STOCK MUERTO) ---
        st.markdown("### 📦 Análisis de Adquisiciones y Alerta de Stock Muerto por Proveedor")
        st.write(
             "Al contrastar la tarjeta métrica de **Stock Muerto** de **\\$2,706,061.36 USD** con el histórico de compras, "
             "se evidencia que este capital congelado proviene de adquisiciones masivas concentradas en proveedores específicos. "
             "Existe un riesgo inminente de pérdida material y obsolescencia en insumos sin rotación que actualmente "
             "ocupan espacio crítico en el almacén, destacando el caso de **Nitrile Gloves (Guantes de Nitrilo)** entre otros."
         )
         
        st.markdown("**Desglose del Capital Inmovilizado vs. Inversión Activa:**")
        st.markdown(
             """
             * 🔘 **ELECTRA-NETWORK SUPPLY (Foco Crítico de Ineficiencia):** Es el principal responsable de la acumulación de inventario ocioso. Registra la alarmante cifra de **\\$1,394,373.27 USD** retenidos exclusivamente en **Stock Muerto** (barra gris), superando por casi el doble a su suministro operativo de Clase A (**\\$755,195.28 USD**).
             * 🔴 **GENERAL SERVICES & LOGISTICS CO. SUPPLIER (Líder en Suministro Útil):** Representa la inversión más saludable y estratégica. Concentra **\\$2,062,520.24 USD** en materiales críticos de alta rotación (Clase A), mientras que su Stock Muerto es comparativamente bajo (**\\$652,494.47 USD**), demostrando compras mejor alineadas a la demanda.
             * 🟡 **INDUSTRIAL GLOBAL SOLUTIONS (Balance de Riesgo):** Muestra un comportamiento intermedio con **\\$814,427.95 USD** en Clase A, pero mantiene congelados **\\$656,693.78 USD** en la categoría de Stock Muerto, igualando prácticamente su valor útil con el inventario sin movimiento.
             
             **Estrategia Comercial:** Intervenir de forma prioritaria el historial de compras con *ELECTRA-NETWORK SUPPLY* para frenar el flujo de almacenamiento innecesario de guantes de nitrilo y consumibles, evaluando con urgencia un plan de devolución o liquidación para recuperar parte de los **\\$2.70M USD** en riesgo.
             """
         )
        
    with col3:
        # --- Sección de Resumen Ejecutivo: Impacto Económico Clase A y Salidas por Departamento ---
         st.markdown("### 📈 Impacto Económico Clase A y Consumo Departamental")
         st.write(
             "El análisis de Pareto y criticidad del inventario determina que los **Materiales Clase A** "
             "son el motor financiero absoluto de la organización. Esta categoría concentra un impacto económico "
             "de **\\$2,618,922.47 USD**, representando el **79.32% del valor total del inventario**. "
             "Al cruzar este KPI global con el registro de salidas, identificamos exactamente qué departamentos "
             "están demandando este capital para su continuidad operativa."
         )
         
         st.markdown("**Análisis de Distribución de Salidas por Departamento:**")
         st.markdown(
             """
             * 🔵 **Operational Maintenance (Máximo Consumidor):** Es el principal dinamizador del gasto en la empresa. Absorbe de forma masiva **\\$1,560,358.13 USD** en materiales críticos de Clase A y **\\$413,381.89 USD** en Clases B y C. Mantener la continuidad operativa de esta área justifica el grueso de la inversión.
             * 🔵 **Electrical Services (Inversión Focalizada):** Representa el segundo mayor flujo de salida financiera con **\\$795,266.56 USD** dedicados estrictamente a componentes Clase A. Destaca positivamente por mantener un consumo mínimo en materiales secundarios o consumibles (Clases B y C) de apenas **\\$10,761.70 USD**.
             * 📊 **Optimization (Comportamiento Estable):** Presenta una ejecución financiera moderada y equilibrada, registrando salidas por **\\$274,771.21 USD** en Clase A y **\\$54,493.93 USD** en las categorías B y C.
             * ⚠️ **Anomalía en SSEE (Gasto Invertido):** Es el único departamento de alto volumen donde se rompe la tendencia lógica. El despacho de materiales de menor criticidad (Clases B y C) asciende a **\\$120,302.53 USD**, llegando casi a **duplicar** el consumo de materiales de alta prioridad Clase A, que apenas suma **\\$66,656.21 USD**.
             
             **Estrategia de Optimización:** El **90% del capital Clase A** (más de **\\$2.35M USD**) está concentrado exclusivamente en *Operational Maintenance* y *Electrical Services*. Las auditorías de almacén y las negociaciones de contratos a largo plazo deben enfocarse en estas dos áreas, mientras que *SSEE* requiere una revisión técnica para justificar su inusual demanda de materiales Clase B y C.
             """
         )