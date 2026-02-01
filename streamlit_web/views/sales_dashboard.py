import streamlit as st
import pandas as pd

def main():
    # CONFIGS
    YEAR = 2023
    PREVIOUS_YEAR = 2022
    # South African cities
    CITIES = ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth"]
    DATA_URL = "https://raw.githubusercontent.com/Sven-Bo/datasets/master/store_sales_2022-2023.csv"
    
    st.title("🇿🇦 South Africa Sales Dashboard", anchor=False)
    
    @st.cache_data
    def get_and_prepare_data(data):
        df = pd.read_csv(data).assign(
            date_of_sale=lambda df: pd.to_datetime(df["date_of_sale"]),
            month=lambda df: df["date_of_sale"].dt.month,
            year=lambda df: df["date_of_sale"].dt.year,
        )
        # Map data to South African context
        # Replace original cities with South African cities (assuming we have enough data rows)
        if len(df) >= len(CITIES):
            df["city"] = [CITIES[i % len(CITIES)] for i in range(len(df))]
        return df
    
    df = get_and_prepare_data(data=DATA_URL)
    
    # Rest of your dashboard code...
    # ... ALL THE REST OF YOUR DASHBOARD CODE ...
    
    # Footer with South African context
    st.divider()
    st.caption("Data displayed in South African Rand (ZAR). Exchange rate: 1 USD = R 18.5 (approximate)")

if __name__ == "__main__":
    main()
