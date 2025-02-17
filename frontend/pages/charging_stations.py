import dash
from dash import dcc, html
import plotly.express as px
from data.fetch_data import load_charging_stations

df = load_charging_stations()

dash.register_page(__name__, path='/charging_stations')

# Some graphs here and there, refer to the docs for more info
# I really don't know what I'm doing
    
def layout():
    df_grouped = df.groupby('year', as_index=False).agg({'num_charging_points': 'sum'})
    return html.Div([
        dcc.Graph(id='station-distribution', figure=px.histogram(df, x='district_city', title='Stations by Region')),
        dcc.Graph(id='station-type', figure=px.pie(df, names='station_type', title='Distribution by Type')),
        dcc.Graph(id='yearly-evolution', figure=px.line(df_grouped, x='year', y='num_charging_points', title='Yearly Evolution'))
    ])