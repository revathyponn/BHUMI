import dash
import dash_html_components as html
import dash_leaflet as dl

# Create the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dl.Map(center=[45.5236, -122.6750], zoom=10, children=[
        dl.TileLayer(),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
