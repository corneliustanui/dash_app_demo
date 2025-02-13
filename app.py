import dash
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("My First Dash App!"),
    html.P("This is a basic Dash app."),
])

# This line is crucial for Gunicorn (deplooyment on Render)
server = app.server

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
