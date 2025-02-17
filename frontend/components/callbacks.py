from dash import Input, Output
import pandas as pd
import plotly.express as px
from data.fetch_data import get_yearly_trends, get_car_data


# We need callbacks to update the dropdowns and charts based on user input
# I really have no clue how this works
def register_callbacks(app):

    @app.callback(
        Output("year-dropdown", "options"),
        Output("make-dropdown", "options"),
        Input("year-dropdown", "value"),
    )
    def update_dropdowns(selected_year):
        df = get_car_data()
        years = sorted(df["year"].unique())
        makes = sorted(df["make"].unique())

        return [{"label": str(y), "value": y} for y in years], [{"label": m, "value": m} for m in makes]

    @app.callback(
        Output("yearly-sales-graph", "figure"),
        Input("year-dropdown", "value")
    )
    def update_sales_chart(selected_year):
        df = get_yearly_trends()
        if selected_year:
            df = df[df["year"] == selected_year]

        fig = px.line(df, x="year", y="electric_car_sales_count", title="Electric Car Sales Over Time")
        return fig

    @app.callback(
        Output("charging-station-graph", "figure"),
        Input("year-dropdown", "value")
    )
    def update_charging_chart(selected_year):
        df = get_yearly_trends()
        if selected_year:
            df = df[df["year"] == selected_year]

        fig = px.bar(df, x="year", y="charging_station_count", title="Charging Stations Over Time")
        return fig
