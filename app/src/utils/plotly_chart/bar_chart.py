import streamlit as st
import pandas as pd
import plotly.express as px


def bar_chart1(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Gráfico",
    color=None,
    orientation="v",
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
):
    labels = {x: x_label if x_label else x, y: y_label if y_label else y}
    if color and color_label:
        labels[color] = color_label
    bar_chart_view = px.bar(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        color=color,
        orientation=orientation,
        labels=labels,
    )
    st.plotly_chart(bar_chart_view)