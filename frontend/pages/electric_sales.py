import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from data.fetch_data import load_electric_sales

df = load_electric_sales()

dash.register_page(__name__, path='/electric_sales')

# I need to see the docs for how to write graphs
# sobbing...

def layout():
    return html.Div([
        dcc.Dropdown(
            id='make-dropdown',
            options=[{'label': make, 'value': make} for make in df['make'].unique()],
            value=df['make'].unique()[0]
        ),
        dcc.Graph(id='price-evolution'),
        dcc.Graph(id='make-distribution')
    ])

@dash.callback(
    Output('price-evolution', 'figure'),
    Output('make-distribution', 'figure'),
    Input('make-dropdown', 'value')
)
def update_graphs(selected_make):
    filtered_df = df[df['make'] == selected_make]
    price_fig = px.line(filtered_df.groupby('year', as_index=False)['price'].mean(), x='year', y='price', title='Price Evolution')
    dist_fig = px.histogram(filtered_df, x='year', title='Distribution by Year')
    return price_fig, dist_fig