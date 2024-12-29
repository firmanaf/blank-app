# Carbon Emissions Predictor

This repository contains a Streamlit application for predicting carbon emissions based on input feature values. The application allows users to adjust feature values using sliders in the sidebar and visualize the predicted carbon emissions from 2025 to 2045 in the main body.

---

## Features
- **Interactive sliders**: Adjust values for key features like population, NTL (Nighttime Light), line density, and land cover.
- **Prediction visualization**: View predicted carbon emissions trends from 2025 to 2045.
- **Model-driven insights**: Powered by a pre-trained Random Forest model.

---

## Requirements

Install the required dependencies using:
```bash
pip install -r requirements.txt
```

### Dependencies:
- `streamlit`
- `matplotlib`
- `pandas`
- `scikit-learn`
- `joblib`

---

## File Structure

```
|-- app.py                # Main Streamlit application script
|-- rf_model.pkl          # Pre-trained Random Forest model
|-- requirements.txt      # Python dependencies
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/carbon-emissions-predictor.git
   cd carbon-emissions-predictor
   ```

2. Ensure the `rf_model.pkl` file is in the project directory.

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
http://localhost:8501
   ```

---

## Application Overview

### Sidebar
- **Feature Sliders**: Adjust values for:
  - `population_2012`
  - `population_2023`
  - `ntl_2012`
  - `ntl_2023`
  - `line_density_2012`
  - `line_density_2023`
  - `land_cover_2012`
  - `land_cover_2023`

### Main Body
- **Visualization**: Line chart showing predicted carbon emissions from 2025 to 2045.
- **Data Table**: Tabular display of predicted emissions per year.

---

## Deploying to the Web

You can deploy this application using platforms like:
- **Streamlit Cloud**
- **Heroku**
- **AWS Elastic Beanstalk**

### Steps for Streamlit Cloud:
1. Push your repository to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repository.
4. Deploy your application.

---

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
