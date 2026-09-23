# 🇱🇰 The Great Comeback: Sri Lanka Tourism Recovery Dashboard (2022–2026)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sri-lanka-tourism-analytics.streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Visualization](https://img.shields.io/badge/Visualization-Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
[![Data Source](https://img.shields.io/badge/Data-SLTDA%20Reports-0984E3?style=flat)](https://www.sltda.gov.lk/)
[![Affiliation](https://img.shields.io/badge/Affiliation-University%20of%20Colombo-gold?style=flat)](https://science.cmb.ac.lk/academic/departments/statistics/)

> **An interactive public-interest data analytics platform tracking Sri Lanka's post-crisis tourism rebound, foreign exchange generation, source market diversification, and seasonal arrival dynamics (2022–2026).**

🔗 **Live Interactive Application:** [sri-lanka-tourism-analytics.streamlit.app](https://sri-lanka-tourism-analytics.streamlit.app)

---

## 📌 Context & Motivation

Following the severe foreign exchange and macroeconomic crisis in 2022, tourism emerged as a vital pillar for Sri Lanka's economic stabilization. 

Inspired by the **Department of Statistics, University of Colombo's 25th Anniversary initiative**, this project was created to provide transparent, open-access visual analytics on the nation's tourism revival. It transforms official monthly reports from the **Sri Lanka Tourism Development Authority (SLTDA)** into an interactive decision-support tool for researchers, hospitality analysts, and policymakers.

---

## 🚀 Key Dashboard Features

* **📈 V-Shaped Arrival Trajectory:** Interactive time-series line tracking monthly tourist arrivals from the mid-2022 baseline through the record-breaking volumes of 2025/2026.
* **🌍 Inbound Source Market Breakdown:** Dynamic donut chart categorizing sovereign visitor contributions across primary origin markets (India, Russia, UK, Germany, China, etc.).
* **📅 Bimodal Seasonality Analyzer:** Aggregates multi-year arrivals chronologically (January to December) to quantify peak winter escape months against the mid-year cultural festival surge.
* **💰 Real-Time Macro KPIs:** Aggregates cumulative visitor counts, estimated foreign exchange earnings ($ Billion USD), and current leading source countries dynamically based on active filters.
* **🔍 Multi-Dimensional Filtering:** Flexible sidebar controls allowing custom filtering by year ranges and individual origin countries.

---

## 💡 Key Empirical Insights

1. **The V-Shaped Rebound:** After bottoming out during the fuel and power disruptions of mid-2022, inbound arrivals exhibited consistent exponential recovery, surpassing pre-crisis thresholds by late 2025.
2. **Growth Engines (India & Russia):** **India** and **Russia** consistently represent the two largest individual sovereign markets, collectively driving over **35% of all inbound visitor traffic**.
3. **Bimodal Seasonality:** Arrival volumes follow a distinct two-peak annual distribution:
   * **Primary Peak (December – March):** European and Northern Hemisphere winter escape tourists.
   * **Secondary Peak (July – August):** Regional travelers and diaspora visitors aligning with the historic *Kandy Esala Perahera* cultural festival season.

---

## 📊 Dataset Schema (`sri_lanka_tourism_data.csv`)

The underlying dataset harmonizes monthly SLTDA reports across the following dimensions:

| Field | Type | Description |
| :--- | :--- | :--- |
| `Date` | `datetime64` | Observation timestamp (Monthly granularity: YYYY-MM-01) |
| `Year` | `int64` | Calendar year (2022 to 2026) |
| `Month` | `string` | Full month name (January through December) |
| `Country` | `string` | Inbound origin market (e.g., India, Russia, UK, Germany) |
| `Arrivals` | `int64` | Disaggregated tourist count from the specified country |
| `Total_Monthly_Arrivals`| `int64` | Island-wide aggregate tourist volume for that month |
| `Est_Revenue_MUSD` | `float64` | Estimated monthly tourism foreign exchange earnings (Million USD) |

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.10+
* **Framework:** Streamlit Community Cloud
* **Data Manipulation:** Pandas (grouping, time-series parsing, categorical ordering)
* **Interactive Charting:** Plotly Express (`px.line`, `px.pie`, `px.bar`)
* **Styling:** Responsive light-theme layout with Plotly integration

---

## 💻 Local Installation & Setup

To run this dashboard on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/rasindupramith-oss/sri-lanka-tourism-dashboard.git
cd sri-lanka-tourism-dashboard

# 2. Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install required libraries
pip install -r requirements.txt

# 4. Launch the Streamlit application
streamlit run app.py
```

The application will launch automatically at `http://localhost:8501`.

---

## 👨‍💻 Author

**Rasindu Pramith**  
*Undergraduate, BSc (Hons) in Applied Statistics*  
*Faculty of Science, University of Colombo, Sri Lanka*  

* 🌐 **Portfolio:** [rasindupramith-oss.github.io](https://rasindupramith-oss.github.io/)
* 💼 **LinkedIn:** [linkedin.com/in/rasindu-pramith](https://www.linkedin.com/in/rasindu-pramith/)
* 💻 **GitHub:** [@rasindupramith-oss](https://github.com/rasindupramith-oss)

---

## 📄 License
This project is open-source and distributed under the [MIT License](LICENSE).
