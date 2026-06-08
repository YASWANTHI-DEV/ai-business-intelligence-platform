import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

st.title("🔮 Sales Forecasting")

if "data" not in st.session_state or st.session_state.data is None:
    st.warning("Upload dataset from sidebar")
    st.stop()

df = st.session_state.data.copy()

df["Order.Date"] = pd.to_datetime(
    df["Order.Date"]
)

monthly_sales = (
    df.groupby(
        df["Order.Date"].dt.to_period("M")
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["MonthIndex"] = np.arange(
    len(monthly_sales)
)

X = monthly_sales[["MonthIndex"]]

y = monthly_sales["Sales"]

model = LinearRegression()

model.fit(X, y)

next_month = np.array(
    [[monthly_sales["MonthIndex"].max() + 1]]
)

prediction = model.predict(next_month)

st.metric(
    "Predicted Next Month Sales",
    f"${prediction[0]:,.0f}"
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=monthly_sales["MonthIndex"],
        y=monthly_sales["Sales"],
        mode="lines+markers",
        name="Historical"
    )
)

fig.add_trace(
    go.Scatter(
        x=[next_month[0][0]],
        y=[prediction[0]],
        mode="markers",
        name="Forecast"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)