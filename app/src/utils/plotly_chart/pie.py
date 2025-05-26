import pandas as pd
import plotly.express as px
import streamlit as st


def pie_chart1(
    df: pd.DataFrame,
    values: str,
    names: str,
    title: str = None,
    names_label: str = None,
    values_label: str = None,
):
    labels = {
        names: names_label if names_label else names,
        values: values_label if values_label else values,
    }

    pie_chart_view = px.pie(
        data_frame=df, values=values, names=names, title=title, labels=labels
    )

    st.plotly_chart(pie_chart_view)
