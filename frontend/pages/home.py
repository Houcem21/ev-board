import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
from data.fetch_data import load_yearly_trends

dash.register_page(__name__, path='/')

# Load data
yearly_df = load_yearly_trends()
years = sorted(yearly_df['year'].unique())

# Initial Figure (Set to First Year)
def create_figure(selected_year):
    filtered_df = yearly_df[yearly_df['year'] <= selected_year]  # Show bars up to selected year
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['year'], y=filtered_df['electric_car_sales_count'], marker_color='royalblue'))
    fig.update_layout(title="Electric Car Sales Growth (Last 10 Years)", xaxis_title="Year", yaxis_title="Sales Count")
    return fig

# Dear reader, when I tell you this is the most confusing part of the code, I'm not lying
# I have no idea what I'm doing
# May you know better
# Sincerely, the author (greatly assisted by chatgpt ngl)

def layout():
    return html.Div([
        html.H1("Electric Car Market Growth in Deutschland"),
        html.P("Electric vehicle adoption has surged over the past decade, increasing demand for charging infrastructure."),
        
        # Slider to Animate Data
        dcc.Slider(
            id='year-slider',
            min=min(years),
            max=max(years),
            step=1,
            marks={str(year): str(year) for year in years},
            value=min(years),
            tooltip={"placement": "bottom", "always_visible": True}
        ),

        # Animated Graph
        dcc.Graph(id='ev-growth-animation', figure=create_figure(min(years)))
    ], className="home-container")

# Callback to update figure when slider moves
@dash.callback(
    Output('ev-growth-animation', 'figure'),
    Input('year-slider', 'value')
)
def update_graph(selected_year):
    return create_figure(selected_year)


