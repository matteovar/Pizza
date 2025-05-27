import pandas as pd
import plotly.express as px
import streamlit as st


def mapa(
    df: pd.DataFrame,
    location: str,
    locationmode: str,
    color: str,
    hover_name: str,
    hover_data: str,
    color_continuous_scale: str,
    title: str = None,
):
    fig = px.choropleth(
        data_frame=df,
        locations=location,
        locationmode=locationmode,
        color=color,
        hover_name=hover_name,
        hover_data=hover_data,
        color_continuous_scale=color_continuous_scale,
        title=title,
    )
    fig.update_layout(
        geo=dict(
            scope="usa",  # Foca no mapa dos EUA
            showframe=False,
            showcoastlines=True,
        ),
        width=500,
        height=800,
    )
    st.plotly_chart(fig)
