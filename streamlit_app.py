import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set the theme to dark
st.set_page_config(page_title="Balance - Mental Health Map UI", layout="wide")

# App Header
st.sidebar.image("path/to/logo.png", use_column_width=True)
st.sidebar.title("Balance")
user_name = st.sidebar.text_input("Enter your name", value="Sam")
st.sidebar.write(f"Hello {user_name}!")

# Main Section
st.title("Mental Health Map")

# Top Row: Welcome Message & Overview
st.subheader("Welcome Message & Overview")
st.markdown(f"""
    Hello {user_name}! Welcome to your personalized mental health dashboard.
    Here you can monitor your mental health status using real-time data from various biofeedback devices.
""")

# Include key metrics (use placeholders)
average_stress_level = 3.5  # Placeholder
recent_activities = "Meditation, Yoga, Walking"  # Placeholder

st.write(f"**Average Stress Level:** {average_stress_level}")
st.write(f"**Recent Activities:** {recent_activities}")

# Map and Data Visualization Section
st.subheader("Stress Level Heatmap")

# Placeholder for interactive map (replace with real data and interactive map in a real application)
map_data = pd.DataFrame({
    'lat': [37.7749, 34.0522, 40.7128],
    'lon': [-122.4194, -118.2437, -74.0060],
    'stress_level': [5, 3, 4]
})

fig = px.scatter_mapbox(
    map_data, lat="lat", lon="lon", color="stress_level", size="stress_level",
    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=3
)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken="your_mapbox_token_here")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

# Trend Graph
st.subheader("Trend Graph")

# Placeholder for trend graph (replace with real data in a real application)
trend_data = pd.DataFrame({
    'date': pd.date_range(start='1/1/2022', periods=100),
    'stress_level': np.random.randint(1, 6, size=100)
})

fig = px.line(trend_data, x='date', y='stress_level', title='Stress Level Over Time')
fig.update_layout(template="plotly_dark")
st.plotly_chart(fig)

# Metrics and Analysis Section
st.subheader("Metrics and Analysis")

# Daily Insights
st.write("**Daily Insights**")
st.write("**Highest Stress Period:** Afternoon")
st.write("**Lowest Stress Period:** Morning")

# Comparison Graph
st.subheader("Comparison Graph")

# Placeholder for comparison graph (replace with real data in a real application)
comparison_data = pd.DataFrame({
    'location': ['Location 1', 'Location 2', 'Location 3'],
    'stress_level': [3.5, 4.2, 2.8]
})

fig = px.bar(comparison_data, x='location', y='stress_level', title='Stress Level Comparison by Location')
fig.update_layout(template="plotly_dark")
st.plotly_chart(fig)

# User-Specific Data
st.subheader("User-Specific Data")

# Personal Metrics (use placeholders)
personal_metrics = {
    'HRV': [70, 72, 75, 68, 74],
    'EKG': [1.2, 1.3, 1.1, 1.4, 1.3],
    'GSR': [0.5, 0.55, 0.52, 0.48, 0.53]
}

for metric, values in personal_metrics.items():
    st.write(f"**{metric} Trends:**")
    fig = px.line(x=range(len(values)), y=values, title=f'{metric} Over Time')
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig)

# Footer
st.write("---")
st.write("[Terms of Service](#) | [Privacy Policy](#) | [Support](#)")

# Additional Navigation
st.sidebar.title("Navigation")
st.sidebar.write("[Dashboard](#)")
st.sidebar.write("[StressRelief Hub](#)")
st.sidebar.write("[Settings](#)")
