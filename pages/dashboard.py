import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Executive Dashboard")

if "data" not in st.session_state or st.session_state.data is None:
    st.warning("Upload dataset from sidebar")
    st.stop()

df = st.session_state.data.copy()

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order.ID"].nunique()
total_customers = df["Customer.ID"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Total Sales", f"${total_sales:,.0f}")
c2.metric("📈 Total Profit", f"${total_profit:,.0f}")
c3.metric("📦 Orders", total_orders)
c4.metric("👥 Customers", total_customers)

st.divider()

col1, col2 = st.columns(2)

with col1:

    top_products = (
        df.groupby("Product.Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product.Name",
        orientation="h",
        title="Top Products"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    country_sales = (
        df.groupby("Country")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.pie(
        country_sales,
        names="Country",
        values="Sales",
        title="Country Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("🌎 Regional Performance")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🤖 AI Business Insights")

best_product = (
    df.groupby("Product.Name")["Sales"]
    .sum()
    .idxmax()
)

best_country = (
    df.groupby("Country")["Sales"]
    .sum()
    .idxmax()
)

st.success(f"Top Product: {best_product}")
st.info(f"Highest Revenue Country: {best_country}")

csv = df.to_csv(index=False)

st.download_button(
    "📥 Download Dataset",
    csv,
    "sales_report.csv",
    "text/csv"
)