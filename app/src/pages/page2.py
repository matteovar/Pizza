import streamlit as st
from src.main import df
from src.utils.plotly_chart.maps import mapa
from src.utils.title import title


def mapas():
    title("Pizza Orders by State")
    order_maps = df.groupby(["State"])["Order ID"].count().reset_index()

    mapa(
        order_maps,
        location="State",  # Usar códigos de estado
        locationmode="USA-states",  # Modo específico para estados dos EUA
        color="Order ID",
        hover_name="State",
        hover_data=["Order ID"],
        color_continuous_scale="Viridis",
    )
