import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/drivers_data.csv")

st.set_page_config(page_title="F1 Fantasy Dashboard", layout="wide")
st.title("🏎 F1 Fantasy Insights Dashboard")

# Sidebar
drivers = df["driver"].unique()
selected_driver = st.sidebar.selectbox("Select a Driver", drivers)

# Filter data
driver_df = df[df["driver"] == selected_driver]

# Layout
col1, col2 = st.columns(2)

# Driver trend over races (points)
with col1:
    fig_points = px.line(
        driver_df,
        x="race",
        y="points",
        title=f"{selected_driver} – Points Over Races",
        markers=True
    )
    st.plotly_chart(fig_points, use_container_width=True)

# Price trend
with col2:
    fig_price = px.line(
        driver_df,
        x="race",
        y="price",
        title=f"{selected_driver} – Price Over Races",
        markers=True
    )
    st.plotly_chart(fig_price, use_container_width=True)

# Points per million spent
df["ppm"] = df["points"] / df["price"]
ppm_df = df[df["driver"] == selected_driver]

st.subheader(f"💰 Points per Million – {selected_driver}")
fig_ppm = px.bar(
    ppm_df,
    x="race",
    y="ppm",
    title=f"{selected_driver} – Points per Million Spent",
    labels={"ppm": "Points / Price (in millions)"},
    color="ppm",
    color_continuous_scale="Viridis"
)
st.plotly_chart(fig_ppm, use_container_width=True)

# Optionally export data
with st.expander("📥 Download Driver Data"):
    st.download_button(
        label="Download CSV",
        data=driver_df.to_csv(index=False),
        file_name=f"{selected_driver}_fantasy_data.csv",
        mime="text/csv"
    )
