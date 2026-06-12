# Dashboard de Analítica de Inventarios MRP 📊📦

🌐 **Language / Idioma:** [View English Version 🇬🇧](./README.md) | **Español** 🇪🇸

🚀 **Proyecto en vivo:** [Visitar la Aplicación Web](https://mrp-control-analytics.streamlit.app/)
🧪 **Análisis exploratorio de datos:** [Ver Google Colab](https://colab.research.google.com/drive/1_kauPu9APz_9DaEF3KV2am5usiBq6gWY?usp=sharing)

---

## 💼 Contexto y Problema de Negocio

En la gestión de inventarios industriales, se detectaron inconsistencias de gran envergadura debido a la falta de trazabilidad en los movimientos de material, causada por datos no proporcionados en el dataset original. Esta deficiencia genera una retención de insumos que se traduce en posibles pérdidas monumentales por concepto de stock muerto (Dead Stock).

Este proyecto nació con la finalidad de realizar un análisis profundo de estos datos para comprender la naturaleza y el calibre de las problemáticas presentes en esta gestión, con el fin de atacar estas ineficiencias y optimizar el flujo de trabajo del almacén.

* **Falta de trazabilidad:** Salidas de materiales sin registrar el departamento solicitante, lo que impide auditar el consumo final.
* **Acumulación de stock muerto:** Acumulación de materiales sin rotación que ocupan espacio físico y representan un alto riesgo de pérdida por obsolescencia o vencimiento.
* **Errores de stock:** Al auditar la hoja de control de existencias, se identificó información poco fidedigna, incluyendo stocks negativos e inconsistencias con los registros históricos.

## 🚀 Solución Desarrollada

Se construyó un Dashboard Analítico Ejecutivo y bilingüe (Español/Inglés) utilizando Python y Streamlit para automatizar la auditoría de inventarios y proveer insights accionables:

* **Valor de materiales Clase A:** Identificación del impacto económico de los materiales Clase A, los cuales representan el 79.32% del valor total del inventario. Este insight permite a la gerencia priorizar esfuerzos de control en los activos que representan la mayor inversión.
* **Métricas de Impacto Económico:** Conversión de datos técnicos a indicadores de negocio, calculando el capital exacto congelado en Stock Muerto y movimientos no asignados, permitiendo visualizar el valor monetario (USD) en riesgo.
* **Auditoría de Proveedores y Departamentos:** Análisis detallado de compras por proveedor y consumo por departamento, facilitando la detección de ineficiencias comerciales y oportunidades de mejora en la cadena de suministro.

## 🛠️ Stack Tecnológico y Arquitectura

El sistema implementa una arquitectura de datos moderna y completamente desplegada en la nube:

* **Base de Datos:** MySQL.
* **Infraestructura Cloud:** Base de datos relacional alojada en **Aiven Cloud**.
* **Lenguajes y Librerías:** Python (`Pandas`, `SQLAlchemy`, `Matplotlib`, `Seaborn`).
* **Interfaz y Despliegue:** `Streamlit` y `Streamlit Community Cloud`.

## 🧠🧗 Retos Técnicos y Aprendizajes

* **Migración a la Nube y Restricciones de Permisos (MySQL Error 1227):** Al migrar el esquema de la base de datos local a *Aiven Cloud*, el servidor remoto rechazó el script de importación debido a políticas estrictas de seguridad sobre los privilegios de usuario (restricciones de `DEFINER` en las vistas).
  * *Solución:* Se reconfiguró el flujo de exportación utilizando parámetros avanzados en MySQL Workbench (`--skip-definer` y `--skip-triggers`). Esto permitió generar un volcado SQL neutro y compatible con los estándares de seguridad en la nube, garantizando la integridad del modelo de datos.

* **Automatización de Procesos por Lotes (Batch Processing):** Al implementar la lógica para procesar materiales por lotes, enfrenté un desafío técnico debido a que era mi primera experiencia aplicando esta arquitectura sumado con la primera vez que trabajba con groq en análiis del google colab.
  * *Solución:* Realicé una investigación profunda en repositorios de referencia y utilicé el apoyo de herramientas de Inteligencia Artificial para reestructurar la lógica de mi script, logrando una implementación funcional y eficiente.

## 💻 Instalación y Uso Local

1. Clona el repositorio:
   ```bash
   git clone git@github.com:francisco-15/mrp-inventory-analytics.git

2. Instala las dependencias:
 ```bash
  pip install -r requirements.txt

4. Ejecutar:
 ```bash
 streamlit run app.py
  
