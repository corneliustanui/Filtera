# Author:  Cornelius Tanui
# Email: kiplimocornelius at gmail.com
# Description: A web app for aggregating film and literature.
# Date: 25 Feb 2025
# Version: 1.0
# Deployment: gunicorn app:server (on Render.com)
# URL: https://filtera.onrender.com

# Import required libraries
import dash
from dash import html

# Register the page
dash.register_page(__name__, path="/")

# Define the page layout
layout = html.Div(
    [
        html.H3("About Filtera"),
        html.P(["Welcome to ", html.B("Filtera"), ", the ultimate hub for ", html.B("fil"), "m and li", html.B("tera"), "ture enthusiasts!"]),
        html.P("Whether you're a movie buff or a bookworm, Filtera's got you covered with the latest analytics and insights."),
        html.P("Dive into our extensive collection of data on your favorite movies and books, and discover new gems to add to your watchlist or reading list."),
        html.P("You are a passionate fan, or you wouldn't be here, so let's explore the fascinating world of film and literature together!"),
        html.P("Happy exploring! 🎬📚")
    ],

    style={
                "border": "1px solid rgb(34, 34, 34)",  # Black border with 1px width
                "padding": "20px",  # Padding inside the box
                "border-radius": "0px",  # Unrounded corners
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)"  # A shadow for better visual effect
            }
)