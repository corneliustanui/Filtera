# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash
from dash import dcc, html, Input, Output, callback
from app import app  # Import your Dash app instance
from pages import render_page_content  # Ensure this function is correctly imported

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

# Function to display the page content
def display_page(pathname):
    return render_page_content(pathname)


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
        return html.P("Content for Action genre.")
    elif button_id == "btn-fantasy":
        return html.P("Content for Fantasy genre.")
    elif button_id == "btn-drama":
        return html.P("Content for Drama genre.")
    elif button_id == "btn-sci-fi":
        return html.P("Content for Sci-Fi genre.")
    else:
        return html.P("Select a genre to see the content.")