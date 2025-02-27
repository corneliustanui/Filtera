# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc  # Import Dash Bootstrap Components
import datetime
from pages.action import layout as action_layout

# Register the page
dash.register_page(__name__, path="/film")

# Define the page layout and content
layout = html.Div([
    dbc.Row([
        # Sidebar
        dbc.Col([
            html.H4("Genres"),
            dbc.ButtonGroup(
                [
                    dbc.Button("Action", color="primary", id="btn-action", n_clicks=0),  # Remove href and use id
                    dbc.Button("Fantasy", color="primary", id="btn-fantasy", n_clicks=0),
                    dbc.Button("Drama", color="primary", id="btn-drama", n_clicks=0),
                    dbc.Button("Sci-Fi", color="primary", id="btn-sci-fi", n_clicks=0),
                ],
                vertical=True,
                className="me-2"
            ),
        ], width=2, style={"border-right": "1px solid rgb(34, 34, 34)", "padding": "20px"}),

        # Main content
        dbc.Col([
            html.Div(id="content-area")  # Placeholder for dynamic content
        ], width=10)
    ])
],

# Styling the content region
style={
        "border": "1px solid rgb(34, 34, 34)",  # Black border with 1px width
        "padding": "20px",  # Padding inside the box
        "border-radius": "0px",  # Unrounded corners
        "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)"  # A shadow for better visual effect
    }
)

# Define the callback to update the content based on the button clicked
@dash.callback(
    Output("content-area", "children"),
    [Input("btn-action", "n_clicks"),
     Input("btn-fantasy", "n_clicks"),
     Input("btn-drama", "n_clicks"),
     Input("btn-sci-fi", "n_clicks")]
)
def update_content(btn_action, btn_fantasy, btn_drama, btn_sci_fi):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "btn-action"  # Default to Action content
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "btn-action":
        return action_layout
    elif button_id == "btn-fantasy":
        return html.P("Content for Fantasy genre.")
    elif button_id == "btn-drama":
        return html.P("Content for Drama genre.")
    elif button_id == "btn-sci-fi":
        return html.P("Content for Sci-Fi genre.")
    else:
        return html.P("Select a genre to see the content.")
