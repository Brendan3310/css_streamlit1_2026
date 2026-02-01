import streamlit as st
import pandas as pd

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

# Add South African Rand conversion (approximate 18:1 ZAR:USD)
ZAR_EXCHANGE_RATE = 18.5

# Calculate total revenue for each city and year, and then calculate the percentage change
city_revenues = (
    df.groupby(["city", "year"])["sales_amount"]
    .sum()
    .unstack()
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] * 100)
)

# Display the data for each city in separate columns
st.subheader("City Performance Overview")
columns = st.columns(len(CITIES))
for i, city in enumerate(CITIES):
    with columns[i]:
        # Convert to ZAR for display
        zar_value = city_revenues.loc[city, YEAR] * ZAR_EXCHANGE_RATE if city in city_revenues.index else 0
        
        st.metric(
            label=f"**{city}**",
            value=f"R {zar_value:,.0f}",
            delta=f"{city_revenues.loc[city, 'change']:.0f}% change vs. PY" if city in city_revenues.index else "N/A",
        )

# Add some South African context
with st.expander("🇿🇦 About South African Economy"):
    st.markdown("""
    **Key Economic Indicators:**
    - **Currency:** South African Rand (ZAR)
    - **GDP Growth:** ~1.9% (2023)
    - **Major Industries:** Mining, Manufacturing, Tourism, Financial Services
    
    **Major Cities:**
    - **Johannesburg:** Economic hub, financial center
    - **Cape Town:** Legislative capital, tourism hub
    - **Durban:** Largest port, manufacturing center
    - **Pretoria:** Administrative capital
    - **Port Elizabeth:** Automotive manufacturing hub
    """)

# Selection fields
st.divider()
st.subheader("Detailed Analysis")

left_col, right_col = st.columns(2)
analysis_type = left_col.selectbox(
    label="Analysis by:",
    options=["Month", "Product Category", "Store Type"],
    key="analysis_type",
)
selected_city = right_col.selectbox("Select a city:", CITIES)

# Toggle for selecting the year for visualization
previous_year_toggle = st.toggle(
    value=False, label="Previous Year", key="switch_visualization"
)
visualization_year = PREVIOUS_YEAR if previous_year_toggle else YEAR

# Display the year above the chart based on the toggle switch
st.write(f"**Sales for {visualization_year} in {selected_city} (in ZAR)**")

# Filter data based on selection for visualization
if analysis_type == "Product Category":
    filtered_data = (
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("product_category", dropna=False)["sales_amount"]
        .sum()
        .reset_index()
    )
elif analysis_type == "Store Type":
    # Add store type analysis (assuming we have this column)
    # If not, create sample store types for South Africa
    store_types = ["Mall", "Shopping Center", "Township Store", "Airport", "Online"]
    if "store_type" not in df.columns:
        df["store_type"] = [store_types[i % len(store_types)] for i in range(len(df))]
    
    filtered_data = (
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("store_type", dropna=False)["sales_amount"]
        .sum()
        .reset_index()
    )
else:
    # Group by month number
    filtered_data = (
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("month", dropna=False)["sales_amount"]
        .sum()
        .reset_index()
    )
    # Ensure month column is formatted as two digits for consistency
    filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")
    
    # Add month names for South African context
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    filtered_data["month_name"] = filtered_data["month"].apply(
        lambda x: month_names[int(x)-1] if x.isdigit() else x
    )

# Convert to ZAR for display
if "sales_amount" in filtered_data.columns:
    filtered_data["sales_amount_zar"] = filtered_data["sales_amount"] * ZAR_EXCHANGE_RATE

# Display the data with appropriate labels
if analysis_type == "Month":
    chart_data = filtered_data.set_index("month_name")["sales_amount_zar"]
    st.bar_chart(chart_data)
else:
    # For product category or store type
    if analysis_type == "Product Category":
        key_col = "product_category"
    else:
        key_col = "store_type"
    
    chart_data = filtered_data.set_index(key_col)["sales_amount_zar"]
    st.bar_chart(chart_data)

# Add data table
with st.expander("View Detailed Data"):
    display_df = filtered_data.copy()
    display_df["Sales (ZAR)"] = display_df["sales_amount_zar"].round(0)
    display_df["Sales (USD)"] = display_df["sales_amount"].round(0)
    
    if analysis_type == "Month":
        st.dataframe(display_df[["month_name", "Sales (ZAR)", "Sales (USD)"]], 
                    use_container_width=True)
    else:
        st.dataframe(display_df[[key_col, "Sales (ZAR)", "Sales (USD)"]], 
                    use_container_width=True)

# Add quarterly summary
st.divider()
st.subheader("Quarterly Performance")

# Calculate quarterly data
df["quarter"] = df["date_of_sale"].dt.quarter
quarterly_data = (
    df.query("city == @selected_city & year == @visualization_year")
    .groupby("quarter")["sales_amount"]
    .sum()
    .reset_index()
)
quarterly_data["sales_amount_zar"] = quarterly_data["sales_amount"] * ZAR_EXCHANGE_RATE

# Display quarterly metrics
q_cols = st.columns(4)
quarter_names = ["Q1 (Jan-Mar)", "Q2 (Apr-Jun)", "Q3 (Jul-Sep)", "Q4 (Oct-Dec)"]
for i in range(4):
    with q_cols[i]:
        q_value = quarterly_data.loc[quarterly_data["quarter"] == i+1, "sales_amount_zar"]
        if len(q_value) > 0:
            st.metric(
                label=quarter_names[i],
                value=f"R {q_value.values[0]:,.0f}"
            )
        else:
            st.metric(
                label=quarter_names[i],
                value="R 0"
            )

# Footer with South African context
st.divider()
st.caption("Data displayed in South African Rand (ZAR). Exchange rate: 1 USD = R 18.5 (approximate)")