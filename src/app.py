import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html, dash_table

# Load data into a Pandas DataFrame
df = pd.read_csv("../data/Centre_Details_Data.csv")

city_options = [
    {"label": "Chennai", "value": "Chennai"},
    {"label": "Bengaluru", "value": "Bengaluru"},
    {"label": "New Delhi", "value": "New Delhi"},
    {"label": "Kolkata", "value": "Kolkata"},
    {"label": "Patna", "value": "Patna"},
    {"label": "Pune", "value": "Pune"},
    {"label": "Trichy", "value": "Trichy"}
]

subject_options = [
    {"label": "Mathematics", "value": "Mathematics"},
    {"label": "English", "value": "English"},
    {"label": "Science", "value": "Science"},
    {"label": "Dance", "value": "Dance"},
    {"label": "Mentoring", "value": "MentoringPatna"},
    {"label": "Computers", "value": "Computers"}
]

# Create the app
app = dash.Dash(__name__)

server = app.server

# Define the layout
app.layout = html.Div(children = [ 
    html.Div(children = [
        html.Img(src = 'img/logo.jpeg',style={
                    'height': '50px',
                    'width': '50px',
                    'float': 'left',
                    'margin-right': '10px'
                 }),
    html.H1('Bhumi NGO'),
    html.H3("One of India's largest NGO volunteer organizations"),
    html.P("Bhumi was founded on August 15, 2006 by a group of friends, who believed that every underprivileged child deserves quality education. Since then, Bhumi has transformed this conviction into a volunteering opportunity"),
    html.P("for India’s youth, launching a snowball effect of nurturing talent on the path to an educated, poverty-free India."),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label="Center Details", children=[
            html.Div(children=[
                html.Label('Select a City to view the center location and project details ',style={'font-weight': 'bold',"margin-right": "10px"}),
                dcc.Dropdown(
                    id="city-dropdown",
                    options=city_options,
                    value=city_options[0]["value"],
                    style={"width": "150px","fontsize":"1px"}
                )
            ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px', 'margin-bottom': '10px'}),

            dcc.Graph(id='map-graph'),

            dcc.Graph(id='bar-graph')
        ]),

        dcc.Tab(label="About", children=[
            html.H1("About"),
            html.P("This is a Dash application that displays information about children centers in various cities."),
            html.P("The data for this application was sourced from the Centre_Details_Data.csv file."),
            html.P("The map and bar chart display information about the number of children available in each center and the subjects taught at each center."),
        ]),
         dcc.Tab(label="Datatable", children=[
            html.H1("Data"),
            html.P("This data is obtained from Bhumi NGO"),
            dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),

         ])
    ])
])
])

# Define the callbacks
@app.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value')]
)
def update_map(city):
    filtered_df = df[df['City'] == city]
    fig = px.scatter_mapbox(
        filtered_df, 
        lat='lat', 
        lon='long', 
        hover_name='Centre Name', 
        hover_data=['Children Available'],
        size='Children Available',
        color='Subject',
        zoom=10,
        title=f"Location of Centers in {city}"
    )
    fig.update_layout(mapbox_style="open-street-map")

    return fig

@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value')]
)
def update_bar(city):
    filtered_df = df[df['City'] == city]
    fig = px.bar(
        filtered_df, 
        x='Centre Name', 
        y='Children Available',
        color='Subject',
        title = f"Number of Children Available Centerwise in {city}"
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
