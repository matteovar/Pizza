import pandas as pd
import plotly.express as px
import streamlit as st


def box(
    df: pd.DataFrame,
    x: str,
    y: str,
    color: str = None,
):
    box_chart_view = px.box(data_frame=df, x=x, y=y, color=color)
    st.plotly_chart(box_chart_view)
