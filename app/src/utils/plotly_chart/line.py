import pandas as pd
import plotly.express as px
import streamlit as st

def line(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Gráfico",
    x_label: str = None,
    y_label: str = None,
):
    labels = {x: x_label if x_label else x, y: y_label if y_label else y}
    line_chart_view = px.line(data_frame=df, x=x, y=y, title=title, labels=labels)

    st.plotly_chart(line_chart_view)