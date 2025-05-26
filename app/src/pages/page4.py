import pandas as pd
import streamlit as st
from src.main import df
from src.utils.plotly_chart.bar_chart import bar_chart1
from src.utils.plotly_chart.maps import mapa
from src.utils.title import title


def porce_map():
    title("Pizza Orders by State")

    agrupado = (
        df.groupby("State")
        .agg(
            total_pedidos=("Is Delayed", "count"),
            pedidos_atrasados=("Is Delayed", "sum"),  # True é contado como 1
        )
        .reset_index()
    )

    # Calcula a porcentagem de atrasos
    agrupado["% Atrasos"] = (
        agrupado["pedidos_atrasados"] / agrupado["total_pedidos"]
    ) * 100

    mapa(
        agrupado,
        location="State",
        locationmode="USA-states",
        color="% Atrasos",
        hover_name="State",
        hover_data=["% Atrasos"],
        color_continuous_scale="Reds",
        title="Porcentagem de Pedidos Atrasados por Estado",
    )

    delayed_impact = (
        df["Traffic Impact"]
        .value_counts()
        .reset_index()
        .sort_values(by="Traffic Impact", ascending=True)
    )

    delayed_impact.columns = ["Traffic Impact", "Count"]

    bar_chart1(
        delayed_impact,
        y="Count",
        x="Traffic Impact",
        color="Traffic Impact",
        title="Quantity of Traffic Impact",
    )
