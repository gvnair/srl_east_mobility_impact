import streamlit as st
import pandas as pd
import altair as alt

# Title
st.title("SRL East: Travel Time Comparison")

# Load data
df = pd.read_csv("data/od_travel_times.csv")
df["OD Pair"] = df["Origin"] + " → " + df["Destination"]

# Select OD pair
od_pair = st.selectbox("Choose an OD pair:", df["OD Pair"].unique())

# Filter for selected OD pair
row = df[df["OD Pair"] == od_pair].iloc[0]

# Prepare data for chart
chart_data = pd.DataFrame({
    "Time Type": ["Peak Time", "Non-Peak Time", "SRL Estimated Time"],
    "Travel Time (min)": [row["Peak_Time"], row["Non_Peak_Time"], row["SRL_Estimated_Time"]]
})

# Bar chart
chart = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X('Time Type', sort=['Peak Time', 'Non-Peak Time', 'SRL Estimated Time']),
    y='Travel Time (min)',
    color='Time Type',
    tooltip=['Time Type', 'Travel Time (min)']
).properties(
    title=f"Travel Times for {od_pair}",
    width=500,
    height=400
)

st.altair_chart(chart, use_container_width=True)
