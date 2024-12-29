import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

# Load trained Random Forest model
rf_model = joblib.load("rf_model.pkl")  # Make sure the file exists in the same directory

# Define feature ranges for sliders
feature_ranges = {
    "population_2012": (0, 5000, 3000),
    "population_2023": (0, 5000, 3500),
    "ntl_2012": (0, 20, 10),
    "ntl_2023": (0, 20, 12),
    "line_density_2012": (0, 0.02, 0.01),
    "line_density_2023": (0, 0.02, 0.015),
    "land_cover_2012": (0, 10, 5),
    "land_cover_2023": (0, 10, 5),
}

# Streamlit app configuration
st.set_page_config(page_title="Carbon Emissions Predictor", layout="wide")

# Sidebar: Feature sliders
st.sidebar.header("Adjust Feature Values")
feature_values = {}
for feature, (min_val, max_val, default) in feature_ranges.items():
    feature_values[feature] = st.sidebar.slider(
        label=feature,
        min_value=min_val,
        max_value=max_val,
        value=default,
        step=0.1 if "density" in feature else 1,
    )

# Body: Prediction and Visualization
st.title("Predicted Carbon Emissions (2025-2045)")

# Generate data for prediction
years_to_predict = np.arange(2025, 2046)
input_data = pd.DataFrame({
    feature: [feature_values[feature]] * len(years_to_predict)
    for feature in feature_ranges.keys()
})
predicted_emissions = rf_model.predict(input_data)

# Plot predictions
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years_to_predict, predicted_emissions, marker='o', linestyle='-', label="Predicted Emissions")
ax.set_title("Carbon Emissions Prediction", fontsize=14)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Predicted Carbon Emissions", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12)
st.pyplot(fig)

# Display prediction data
st.write("Predicted Carbon Emissions (2025-2045):")
st.dataframe(pd.DataFrame({"Year": years_to_predict, "Emissions": predicted_emissions}))
