# src/model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

from preprocessing import load_covid_data, load_economic_data, merge_data

def train_model():
    # Load and merge data
    covid_df = load_covid_data("data/covid_data_india.csv")
    econ_df = load_economic_data("data/economic_data_india.csv")
    df = merge_data(covid_df, econ_df)

    # Feature selection
    X = df[['confirmed', 'deaths', 'recovered', 'active']]
    y = df['unemployment_rate']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Model Evaluation:")
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R² Score:", r2_score(y_test, y_pred))

    # Save model
    joblib.dump(model, "src/unemployment_model.pkl")
    print("✅ Model saved to 'src/unemployment_model.pkl'")

if __name__ == "__main__":
    train_model()
