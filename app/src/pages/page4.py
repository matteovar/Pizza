import pandas as pd
import streamlit as st
from src.main import df
from src.utils.info import info
from src.utils.plotly_chart.bar_chart import bar_chart1
from src.utils.plotly_chart.maps import mapa
from src.utils.title import title


def porce_map():
    title(
        "Logistics and Delays",
        "Monitorar atrasos ajuda a identificar gargalos logísticos",
    )
    delay = df["Delay (min)"].mean()
    info(f"Tempo médio de atraso: {delay:.0f} minutes")

    agrupado = (
        df.groupby("State")
        .agg(
            total_pedidos=("Is Delayed", "count"),
            pedidos_atrasados=("Is Delayed", "sum"),
        )
        .reset_index()
    )

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

    # Mova o elemento de info para cima e centralize

    st.write("")  # Espaçamento

    delayed_impact = (
        df["Traffic Impact"]
        .value_counts()
        .reset_index()
        .sort_values(by="Traffic Impact", ascending=True)
    )
    delayed_impact.columns = ["Traffic Impact", "Count"]

    # Gráfico ocupando toda a largura
    bar_chart1(
        delayed_impact,
        y="Count",
        x="Traffic Impact",
        color="Traffic Impact",
        title="Quantity of Traffic Impact",
    )
