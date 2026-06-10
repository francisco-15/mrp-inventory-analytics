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

    # capture the global language
    language = st.session_state.get("idioma", "Español")

    # corporate translations dictionary with f-strings and secure injections (\\$)
    text = {
        "Español": {
            "col1_t1": "### Materiales Emitidos sin Departamento",
            "col1_c1": f"Se registraron **{count_unspecified_dept} salidas de almacén sin asignar**, lo que significa que se desconoce el departamento de destino final que recibió dichos insumos. Este vacío de trazabilidad representa un coste económico acumulado de **\\${impact_unspecified:,.2f} USD**.",
            "col1_t2": "**Distribución porcentual por tipo de material:**",
            "col1_l1": """
             * 🔴 **Rubber Splicing Tape 23:** 25.0% de las salidas.
             * 🔵 **Electrical Tape 33:** 25.0% de las salidas.
             * 🟢 **Leather Gloves:** 12.5% de las salidas.
             * 🟣 **Terminal Type Barracuda 2/0:** 12.5% de las salidas.
             * 🟠 **Otros materiales menores (4 tipos distintos):** 6.2% cada uno *(Pin Rod, Black Tirap, Barracuda Bimetal y Safety Helmet)*.
             """,
            "col2_t1": "### 📊 Hallazgos Críticos de Stock Muerto e Impacto Operativo",
            "col2_c1": f"El análisis del inventario revela una acumulación crítica de **Stock Muerto** (materiales sin rotación) valorada en **\\${impact_dead_stock:,.2f} USD**. Esta inmovilización de capital representa un riesgo inminente de obsolescencia o pérdida física en insumos de alta rotación como **Nitrile Gloves (Guantes de Nitrilo)**, los cuales saturan el espacio de almacenamiento sin generar valor operativo.",
            "col2_t2": "### 📦 Análisis de Adquisiciones y Alerta de Stock Muerto por Proveedor",
            "col2_c2": f"Al contrastar la tarjeta métrica de **Stock Muerto** de **\\${impact_dead_stock:,.2f} USD** con el histórico de compras, se evidencia que este capital congelado proviene de adquisiciones masivas concentradas en proveedores específicos. Existe un riesgo inminente de pérdida material y obsolescencia en insumos sin rotación que actualmente ocupan espacio crítico en el almacén, destacando el caso de **Nitrile Gloves (Guantes de Nitrilo)** entre otros.",
            "col2_sub_title": "**Desglose del Capital Inmovilizado vs. Inversión Activa:**",
            "col2_l1": """
             * 🔘 **ELECTRA-NETWORK SUPPLY (Foco Crítico de Ineficiencia):** Es el principal responsable de la acumulación de inventario ocioso. Registra la alarmante cifra de **\\$1,394,373.27 USD** retenidos exclusivamente en **Stock Muerto** (barra gris), superando por casi el doble a su suministro operativo de Clase A (**\\$755,195.28 USD**).
             * 🔴 **GENERAL SERVICES & LOGISTICS CO. SUPPLIER (Líder en Suministro Útil):** Representa la inversión más saludable y estratégica. Concentra **\\$2,062,520.24 USD** en materiales críticos de alta rotación (Clase A), mientras que su Stock Muerto es comparativamente bajo (**\\$652,494.47 USD**), demostrando compras mejor alineadas a la demanda.
             * 🟡 **INDUSTRIAL GLOBAL SOLUTIONS (Balance de Riesgo):** Muestra un comportamiento intermedio con **\\$814,427.95 USD** in Clase A, pero mantiene congelados **\\$656,693.78 USD** en la categoría de Stock Muerto, igualando prácticamente su valor útil con el inventario sin movimiento.
             
             **Estrategia Comercial:** Intervenir de forma prioritaria el historial de compras con *ELECTRA-NETWORK SUPPLY* para frenar el flujo de almacenamiento innecesario de guantes de nitrilo y consumibles, evaluando con urgencia un plan de devolución o liquidación para recuperar parte de los **\\$2.70M USD** en riesgo.
             """,
            "col3_t1": "### 📈 Impacto Económico Clase A y Consumo Departamental",
            "col3_c1": f"El análisis de Pareto y criticidad del inventario determina que los **Materiales Clase A** son el motor financiero absoluto de la organización. Esta categoría concentra un impacto económico de **\\${impact_a_class:,.2f} USD**, representando el **79.32% del valor total del inventario**. Al cruzar este KPI global con el registro de salidas, identificamos exactamente qué departamentos están demandando este capital para su continuidad operativa.",
            "col3_t2": "**Análisis de Distribución de Salidas por Departamento:**",
            "col3_l1": """
             * 🔵 **Operational Maintenance (Máximo Consumidor):** Es el principal dinamizador del gasto en la empresa. Absorbe de forma masiva **\\$1,560,358.13 USD** en materiales críticos de Clase A y **\\$413,381.89 USD** en Clases B y C. Mantener la continuidad operativa de esta área justifica el grueso de la inversión.
             * 🔵 **Electrical Services (Inversión Focalizada):** Representa el segundo mayor flujo de salida financiera con **\\$795,266.56 USD** dedicados estrictamente a componentes Clase A. Destaca positivamente por mantener un consumo mínimo en materiales secundarios o consumibles (Clases B y C) de apenas **\\$10,761.70 USD**.
             * 📊 **Optimization (Comportamiento Estable):** Presenta una ejecución financiera moderada y equilibrada, registrando salidas por **\\$274,771.21 USD** en Clase A y **\\$54,493.93 USD** en las categorías B y C.
             * ⚠️ **Anomalía en SSEE (Gasto Invertido):** Es el único departamento de alto volumen donde se rompe la tendencia lógica. El despacho de materiales de menor criticidad (Clases B y C) asciende a **\\$120,302.53 USD**, llegando casi a **duplicar** el consumo de materiales de alta prioridad Clase A, que apenas suma **\\$66,656.21 USD**.
             
             **Estrategia de Optimización:** El **90% del capital Clase A** (más de **\\$2.35M USD**) está concentrado exclusivamente en *Operational Maintenance* y *Electrical Services*. Las auditorías de almacén y las negociaciones de contratos a largo plazo deben enfocarse en estas dos áreas, mientras que *SSEE* requiere una revisión técnica para justificar su inusual demanda de materiales Clase B y C.
             """
        },
        "English": {
            "col1_t1": "### Materials Issued Without Department",
            "col1_c1": f"There were **{count_unspecified_dept} unassigned warehouse outputs** recorded, meaning the final destination department that received these supplies is unknown. This traceability gap represents an accumulated economic cost of **\\${impact_unspecified:,.2f} USD**.",
            "col1_t2": "**Percentage distribution by material type:**",
            "col1_l1": """
             * 🔴 **Rubber Splicing Tape 23:** 25.0% of total outputs.
             * 🔵 **Electrical Tape 33:** 25.0% of total outputs.
             * 🟢 **Leather Gloves:** 12.5% of total outputs.
             * 🟣 **Terminal Type Barracuda 2/0:** 12.5% of total outputs.
             * 🟠 **Other minor materials (4 distinct types):** 6.2% each *(Pin Rod, Black Tirap, Barracuda Bimetal, and Safety Helmet)*.
             """,
            "col2_t1": "### 📊 Critical Dead Stock Findings & Operational Impact",
            "col2_c1": f"Inventory analysis reveals a critical accumulation of **Dead Stock** (non-moving materials) valued at **\\${impact_dead_stock:,.2f} USD**. This tied-up capital represents an imminent risk of obsolescence or physical loss in high-turnover items like **Nitrile Gloves**, which saturate storage space without generating operational value.",
            "col2_t2": "### 📦 Procurement Analysis & Dead Stock Alert by Supplier",
            "col2_c2": f"Contrasting the **Dead Stock** metric card of **\\${impact_dead_stock:,.2f} USD** with historical purchases shows that this frozen capital originates from bulk acquisitions concentrated among specific suppliers. There is an imminent risk of material loss and obsolescence in non-moving items currently taking up critical warehouse space, highlighting the case of **Nitrile Gloves** among others.",
            "col2_sub_title": "**Breakdown of Tied-up Capital vs. Active Investment:**",
            "col2_l1": """
             * 🔘 **ELECTRA-NETWORK SUPPLY (Critical Inefficiency Focus):** Main contributor to idle inventory accumulation. It records an alarming **\\$1,394,373.27 USD** held exclusively in **Dead Stock** (grey bar), almost doubling its useful Class A operational supply (**\\$755,195.28 USD**).
             * 🔴 **GENERAL SERVICES & LOGISTICS CO. SUPPLIER (Useful Supply Leader):** Represents the healthiest and most strategic investment. It concentrates **\\$2,062,520.24 USD** in high-turnover critical materials (Class A), while its Dead Stock is comparatively low (**\\$652,494.47 USD**), proving purchases are better aligned with actual demand.
             * 🟡 **INDUSTRIAL GLOBAL SOLUTIONS (Risk Balance):** Shows intermediate behavior with **\\$814,427.95 USD** in Class A, but keeps **\\$656,693.78 USD** frozen in the Dead Stock category, practically matching its useful value with non-moving inventory.
             
             **Commercial Strategy:** Prioritize reviewing the purchase history with *ELECTRA-NETWORK SUPPLY* to halt the unnecessary influx of nitrile gloves and consumables, urgently evaluating a return or liquidation plan to recover part of the **\\$2.70M USD** at risk.
             """,
            "col3_t1": "### 📈 Class A Economic Impact & Departmental Consumption",
            "col3_c1": f"Pareto and inventory criticality analysis determines that **Class A Materials** are the absolute financial driver of the organization. This category concentrates an economic impact of **\\${impact_a_class:,.2f} USD**, representing **79.32% of the total inventory value**. By crossing this global KPI with output logs, we identify exactly which departments are demanding this capital for operational continuity.",
            "col3_t2": "**Departmental Output Distribution Analysis:**",
            "col3_l1": """
             * 🔵 **Operational Maintenance (Top Consumer):** The primary driver of spending in the company. It massively absorbs **\\$1,560,358.13 USD** in critical Class A materials and **\\$413,381.89 USD** in Classes B and C. Securing operational continuity for this area justifies the bulk of the investment.
             * 🔵 **Electrical Services (Focused Investment):** Represents the second largest financial output flow with **\\$795,266.56 USD** dedicated strictly to Class A components. It stands out positively for maintaining minimal consumption in secondary materials or consumables (Classes B and C) of just **\\$10,761.70 USD**.
             * 📊 **Optimization (Stable Performance):** Presents a moderate and balanced financial execution, registering outputs of **\\$274,771.21 USD** in Class A and **\\$54,493.93 USD** in categories B and C.
             * ⚠️ **SSEE Anomaly (Inverted Spending):** The only high-volume department breaking the logical trend. The dispatch of lower criticality materials (Classes B and C) reaches **\\$120,302.53 USD**, nearly **doubling** the consumption of high-priority Class A materials, which only amounts to **\\$66,656.21 USD**.
             
             **Optimization Strategy:** Over **90% of Class A capital** (more than **\\$2.35M USD**) is exclusively concentrated in *Operational Maintenance* and *Electrical Services*. Warehouse audits and long-term contract negotiations must focus on these two areas, while *SSEE* requires a technical review to justify its unusual demand for Class B and C materials.
             """
        }
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(text[language]["col1_t1"])
        st.write(text[language]["col1_c1"])
        st.markdown(text[language]["col1_t2"])
        st.markdown(text[language]["col1_l1"])
        
    with col2:
        st.markdown(text[language]["col2_t1"])
        st.write(text[language]["col2_c1"])
        st.markdown(text[language]["col2_t2"])
        st.write(text[language]["col2_c2"])
        st.markdown(text[language]["col2_sub_title"])
        st.markdown(text[language]["col2_l1"])
        
    with col3:
        st.markdown(text[language]["col3_t1"])
        st.write(text[language]["col3_c1"])
        st.markdown(text[language]["col3_t2"])
        st.markdown(text[language]["col3_l1"])