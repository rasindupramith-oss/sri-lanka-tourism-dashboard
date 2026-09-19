import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration (Title, Icon, Wide Layout)
st.set_page_config(
    page_title="Sri Lanka Tourism Analytics | 2022 - 2026",
    page_icon="🇱🇰",
    layout="wide"
)

# 2. Header & Story Introduction
st.title("🇱🇰 The Great Comeback: Sri Lanka Tourism Recovery (2022 - 2026)")
st.markdown("""
*An interactive data dashboard exploring how Sri Lanka's tourism economy rebounded from the economic crisis into record-breaking arrivals.*  
**Created by Rasindu Pramith** | *Department of Statistics, University of Colombo*
""")
st.divider()

# 3. Load the Dataset
@st.cache_data
def load_data():
    df = pd.read_csv('sri_lanka_tourism_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# 4. Interactive Sidebar Filters
st.sidebar.header("🔍 Filter Dashboard Data")
years_available = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect(
    "Select Year(s):",
    options=years_available,
    default=years_available
)

countries_available = sorted(df['Country'].unique())
selected_countries = st.sidebar.multiselect(
    "Select Source Markets:",
    options=countries_available,
    default=countries_available
)

# Filter dataframe based on user selections
filtered_df = df[(df['Year'].isin(selected_years)) & (df['Country'].isin(selected_countries))]

# 5. Top-Level KPI Metric Cards
total_arrivals = filtered_df.groupby('Date')['Total_Monthly_Arrivals'].first().sum()
total_revenue = filtered_df.groupby('Date')['Est_Revenue_MUSD'].first().sum()
top_country = filtered_df.groupby('Country')['Arrivals'].sum().idxmax() if not filtered_df.empty else "N/A"

col1, col2, col3 = st.columns(3)
col1.metric("Total Tourist Arrivals", f"{total_arrivals:,.0f}")
col2.metric("Est. Foreign Earnings", f"${total_revenue/1000:,.2f} Billion USD")
col3.metric("Leading Source Country", top_country)

st.write("")

# 6. Chart 1: Monthly Trend Line Chart
st.subheader("📈 Monthly Arrival Trajectory (2022 - 2026)")
monthly_summary = filtered_df.groupby('Date')['Total_Monthly_Arrivals'].first().reset_index()

fig_trend = px.line(
    monthly_summary,
    x='Date',
    y='Total_Monthly_Arrivals',
    labels={'Total_Monthly_Arrivals': 'Number of Tourists', 'Date': 'Month / Year'},
    template='plotly_white'
)
fig_trend.update_traces(line=dict(color='#0984E3', width=3))
st.plotly_chart(fig_trend, use_container_width=True)

# 7. Row 2: Two Columns (Market Breakdown & Seasonality)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("🌍 Top Inbound Source Markets")
    country_summary = filtered_df.groupby('Country')['Arrivals'].sum().reset_index()
    fig_pie = px.pie(
        country_summary,
        names='Country',
        values='Arrivals',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with chart_col2:
    st.subheader("📅 Seasonality Patterns (Arrivals by Month)")
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    season_summary = filtered_df.groupby('Month')['Arrivals'].mean().reindex(month_order).dropna().reset_index()
    fig_season = px.bar(
        season_summary,
        x='Month',
        y='Arrivals',
        labels={'Arrivals': 'Avg Arrivals'},
        template='plotly_white',
        color='Arrivals',
        color_continuous_scale='Blues'
    )
    fig_season.tick_params = dict(axis='x', rotation=45)
    st.plotly_chart(fig_season, use_container_width=True)

# 8. Story Narrative Section
st.divider()
st.subheader("💡 The Story Behind the Numbers")
st.markdown("""
* **The 'V-Shaped' Rebound:** After bottoming out in mid-2022 during the foreign exchange and fuel crisis, tourist arrivals exhibited strong exponential recovery, breaking historical highs by late 2025.
* **Key Growth Engines:** **India** and **Russia** represent the largest source markets, together contributing over 35% of all inbound tourists.
* **Seasonal Surges:** Sri Lanka experiences its primary tourism peak between **December and March** (winter escape from Europe and East Asia), with a secondary summer peak in **July and August** (Esala Perahera festival season).
""")
