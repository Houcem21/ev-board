from dash import dcc, html
import dash_bootstrap_components as dbc

# Simple layout for the Market Dashboard, allowing user to input year and car make
# This needs callbacks, which are defined in frontend/components/callbacks.py; 
# Help
def create_layout(app):
    return dbc.Container([
        html.H1("Market Dashboard", className="text-center mt-4"),

        # Dropdowns for user selection
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id="year-dropdown",
                    options=[],  # Options will be set dynamically (inshallah)
                    placeholder="Select Year",
                )
            ], width=4),
            dbc.Col([
                dcc.Dropdown(
                    id="make-dropdown",
                    options=[],  # Options will be set dynamically (inshallah)
                    placeholder="Select Car Make",
                )
            ], width=4),
        ], className="mb-4"),

        # Graphs
        dbc.Row([
            dbc.Col(dcc.Graph(id="yearly-sales-graph"), width=6),
            dbc.Col(dcc.Graph(id="charging-station-graph"), width=6)
        ]),

    ], fluid=True)
