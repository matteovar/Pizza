import streamlit as st
from src.main import df
from src.utils.plotly_chart.bar_chart import bar_chart1
from src.utils.plotly_chart.line import line
from src.utils.title import title


def visual():
    title(
        "General Informations",
        "Principais métricas do sistema de entregas para entender o comportamento geral das vendas.",
    )

    cols = st.columns(4)
    with cols[0]:
        # Total of Orders
        total_orders = df.shape[0]
        st.metric(label="Total of Orders", value=total_orders, delta=None, border=True)
    with cols[1]:
        # Day with Most Orders
        day_most_orders = df["Day"].value_counts().idxmax()
        st.metric(label="Day with Most Orders", value=day_most_orders, border=True)

    with cols[2]:
        # Median of Delivery Time
        median_delivery_time = df["Delivery Duration (min)"].mean()
        st.metric(
            label="Median of Delivery Time",
            value=f"{median_delivery_time:.0f} minutes",
            border=True,
        )
    with cols[3]:
        # Resurant with Most Orders
        restaurant_most_orders = (
            df.groupby("Restaurant Name")["Order ID"]
            .count()
            .reset_index()
            .sort_values(by="Order ID", ascending=False)
            .iloc[0]
        )
        st.metric(
            label="Restaurant with Most Orders",
            value=restaurant_most_orders["Restaurant Name"],
            border=True,
        )

    cols = st.columns(2)
    with cols[0]:
        orders_time = df.groupby("Time of Order")["Order ID"].count().reset_index()
        line(
            orders_time,
            x="Time of Order",
            y="Order ID",
            title="Orders by Time of Order",
            x_label="Time of Order",
            y_label="Number of Orders",
        )
    with cols[1]:
        orders_day = df.groupby("Day")["Order ID"].count().reset_index()
        bar_chart1(
            orders_day,
            x="Day",
            y="Order ID",
            title="Orders by Day",
            x_label="Day",
            y_label="Number of Orders",
        )
