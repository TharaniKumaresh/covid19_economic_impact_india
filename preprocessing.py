# src/preprocessing.py

import pandas as pd

def load_covid_data(filepath):
    covid_df = pd.read_csv(filepath, parse_dates=['date'])
    covid_df = covid_df[['date', 'state', 'confirmed', 'deaths', 'recovered']]
    covid_df = covid_df.groupby('date').sum().reset_index()
    covid_df['active'] = covid_df['confirmed'] - covid_df['recovered'] - covid_df['deaths']
    return covid_df

def load_economic_data(filepath):
    econ_df = pd.read_csv(filepath, parse_dates=['date'])
    econ_df = econ_df[['date', 'unemployment_rate', 'gdp_growth', 'inflation_rate']]
    return econ_df

def merge_data(covid_df, econ_df):
    merged_df = pd.merge(covid_df, econ_df, on='date', how='inner')
    merged_df = merged_df.dropna()
    return merged_df

if __name__ == "__main__":
    covid_data = load_covid_data("data/covid_data_india.csv")
    econ_data = load_economic_data("data/economic_data_india.csv")
    merged_data = merge_data(covid_data, econ_data)

    print("Merged Data Preview:")
    print(merged_data.head())

    def export_merged_data():
        covid_df = load_covid_data("data/covid_data_india.csv")
    econ_df = load_economic_data("data/economic_data_india.csv")
    merged_df = merge_data(covid_df, econ_df)

    # Save for Power BI
    merged_df.to_csv("data/dashboard_data.csv", index=False)
    print("✅ Exported merged data to 'data/dashboard_data.csv'")

if __name__ == "__main__":
    export_merged_data()

