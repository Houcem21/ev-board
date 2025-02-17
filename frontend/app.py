import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

from pages import electric_sales, charging_stations, connections_trends, home

# I see skies are blue
# red roses too
# I see them bloom
# for me and you
# And I think to myself
# what a wonderful world

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Home", href="/", className="nav-link", id="nav-home")),
            dbc.NavItem(dcc.Link("Electric Sales", href="/electric_sales", className="nav-link", id="nav-sales")),
            dbc.NavItem(dcc.Link("Charging Stations", href="/charging_stations", className="nav-link", id="nav-stations")),
            dbc.NavItem(dcc.Link("Connections & Trends", href="/connections_trends", className="nav-link", id="nav-trends")),
        ],
        brand="EC.de Dashboard",
        color="primary",
        dark=True,
    ),
    dash.page_container
])

# Callback to update active link styles
@app.callback(
    Output("nav-home", "className"),
    Output("nav-sales", "className"),
    Output("nav-stations", "className"),
    Output("nav-trends", "className"),
    Input("url", "pathname"),
)
def update_navbar_active(pathname):
    return [
        "nav-link active-link" if pathname == "/" else "nav-link",
        "nav-link active-link" if pathname == "/electric_sales" else "nav-link",
        "nav-link active-link" if pathname == "/charging_stations" else "nav-link",
        "nav-link active-link" if pathname == "/connections_trends" else "nav-link",
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
