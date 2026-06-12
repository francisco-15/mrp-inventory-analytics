# MRP Inventory Analytics Dashboard 📊📦

🌐 **Language / Idioma:** **English** 🇬🇧 | [Ver versión en Español 🇪🇸](./README.es.md)

🚀 **Live Project:** [Visit the Web Application](https://mrp-control-analytics.streamlit.app/)
🧪 **Exploratory Data Analysis:** [View Google Colab Notebook](https://colab.research.google.com/drive/1_kauPu9APz_9DaEF3KV2am5usiBq6gWY?usp=sharing)

---

## 💼 Business Context & Problem

In industrial inventory management, major inconsistencies were detected due to a lack of traceability in material movements, caused by missing data fields in the original dataset. This deficiency results in overstocking, translating into potentially massive losses due to Dead Stock.

This project was developed to perform a deep-dive analysis of these data logs to understand the nature and scale of the operational challenges, ultimately targeting these inefficiencies and optimizing the warehouse workflow.

* **Lack of Traceability:** Material outputs registered without an assigned requesting department, making it impossible to audit final consumption.
* **Dead Stock Accumulation:** Stagnant materials with zero turnover that occupy physical warehouse space and pose a high risk of loss due to obsolescence or expiration.
* **Stock Inconsistencies:** Auditing the stock balance sheet revealed unreliable records, including negative stock values and data mismatches with historical movement logs.

## 🚀 Developed Solution

An interactive, bilingual (English/Spanish) Executive Analytics Dashboard was built using Python and Streamlit to automate inventory auditing and provide actionable insights:

* **Class A Materials Value:** Identification of the economic impact of Class A materials, which represent 79.32% of the total inventory value. This insight allows management to prioritize control efforts on the assets driving the largest financial investment.
* **Economic Impact Metrics:** Translation of technical data into business KPIs, calculating the exact capital frozen in Dead Stock and unassigned movements to visualize the precise financial value (USD) at risk.
* **Supplier & Department Auditing:** Granular analysis of purchases per supplier and consumption per department, facilitating the detection of commercial inefficiencies and cost-saving opportunities across the supply chain.

## 🛠️ Tech Stack & Architecture

The system implements a modern data pipeline fully deployed in the cloud:

* **Database:** MySQL.
* **Cloud Infrastructure:** Relational database hosted on **Aiven Cloud**.
* **Languages & Libraries:** Python (`Pandas`, `SQLAlchemy`, `Matplotlib`, `Seaborn`).
* **Interface & Deployment:** `Streamlit` and `Streamlit Community Cloud`.

## 🧠🧗 Technical Challenges & Learnings

* **Cloud Migration & Permissions Restrictions (MySQL Error 1227):** When migrating the local database schema to *Aiven Cloud*, the remote server rejected the import script due to strict security policies regarding user privileges (`DEFINER` constraints on views).
  * *Solution:* Reconfigured the database export pipeline using advanced flags in MySQL Workbench (`--skip-definer` and `--skip-triggers`). This generated a clean, environment-neutral SQL dump compatible with cloud security standards, ensuring the underlying data model's integrity.

* **Automated Batch Processing:** When implementing the architecture to process material descriptions in batches, I faced a technical structural challenge as it was my first time applying this design pattern, combined with my first experience integrating the **Groq** API for text analysis inside the **Google Colab** environment.
  * *Solution:* Conducted deep research across reference repositories and leveraged Artificial Intelligence tools to restructure the script's logic, achieving an efficient, high-performance, and functional data enrichment pipeline.

## 💻 Local Installation & Usage

1. Clone the repository:
   ```bash
   git clone git@github.com:francisco-15/mrp-inventory-analytics.git
   ```
   
2. Instala las dependencias:
 ```bash
  pip install -r requirements.txt
  ```

3. Ejecutar:
 ```bash
 streamlit run app.py
 ```
  
