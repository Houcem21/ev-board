import dash
from dash import dcc, html
import plotly.graph_objects as go
from data.fetch_data import load_yearly_trends

yearly_df = load_yearly_trends()

dash.register_page(__name__, path='/connections_trends')

# Some more graphs here and there, refer to the docs for more info
# No clue what I'm doing

def layout():
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=yearly_df['year'], y=yearly_df['total_charging_points'], name="Total Charging Points", yaxis="y1"))
    fig1.add_trace(go.Line(x=yearly_df['year'], y=yearly_df['total_connection_power'], name="Total Connection Power", yaxis="y2"))

    fig1.update_layout(
        title="Evolution of Connection Power vs Charging Points",
        yaxis=dict(title="Total Charging Points", side="left", showgrid=False),
        yaxis2=dict(title="Total Connection Power (kW)", overlaying="y", side="right", showgrid=False),
        legend=dict(x=0.1, y=1.1),
    )

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=yearly_df['year'], y=yearly_df['electric_car_sales_count'], name="EV Sales", yaxis="y1"))
    fig2.add_trace(go.Line(x=yearly_df['year'], y=yearly_df['charging_station_count'], name="Charging Stations", yaxis="y2"))

    fig2.update_layout(
        title="Growth of EV Sales vs Charging Stations",
        yaxis=dict(title="Electric Car Sales", side="left", showgrid=False),
        yaxis2=dict(title="Charging Stations", overlaying="y", side="right", showgrid=False),
        legend=dict(x=0.1, y=1.1),
    )

    return html.Div([
        dcc.Graph(id='connection-power-vs-charging', figure=fig1),
        dcc.Graph(id='yearly-trends', figure=fig2),
    ])
