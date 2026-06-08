import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Advanced Analytics")

if "data" not in st.session_state or st.session_state.data is None:
    st.warning("Upload dataset from sidebar")
    st.stop()

df = st.session_state.data.copy()

st.subheader("Dataset Preview")

st.dataframe(df.head(20))

st.subheader("Category Analysis")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Profit Analysis")

profit_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig = px.pie(
    profit_category,
    names="Category",
    values="Profit"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Customer Segment Analysis")

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    segment_sales,
    x="Segment",
    y="Sales"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Sales vs Profit")

fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Category"
)

st.plotly_chart(fig, use_container_width=True)