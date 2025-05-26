import pandas as pd
import streamlit as st
from src.main import df
from src.utils.plotly_chart.bar_chart import bar_chart1
from src.utils.plotly_chart.pie import pie_chart1
from src.utils.title import title


def logistic():

    title("Consumer Trends")

    cols = st.columns(2)
    with cols[0]:
        size_counts = df["Pizza Size"].value_counts().reset_index()
        size_counts.columns = ["Pizza Size", "Count"]
        bar_chart1(
            size_counts, x="Pizza Size", y="Count", title="Best Selling Pizza Sizes"
        )

    with cols[1]:

        payment = df["Payment Method"].value_counts().reset_index()
        payment.columns = ["Payment Method", "Count"]

        pie_chart1(
            payment, values="Count", names="Payment Method", title="Payment Methods"
        )

    payment_grouped = (
        df.groupby(["Payment Method", "Payment Category"])
        .size()
        .reset_index(name="Count")
    )

    # Gráfico
    bar_chart1(
        payment_grouped,
        x="Payment Method",
        y="Count",
        color="Payment Category",  # separa por Online/Offline
        title="Pagamentos por Método e Tipo de Pedido",
    )
