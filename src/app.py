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

# Create the app
app = dash.Dash(__name__)

server = app.server
# Define the style for the tabs
tab_style = {
    'height': '30px',
    'padding': '8px',
}

# Define the style for the selected tab
selected_tab_style = {
    'height': '30px',
    'padding': '10px',
    'borderTop': '2px solid #f5f5f5',
    'borderBottom': '2px solid #f5f5f5',
    'backgroundColor': '#119DFF',
    'color': 'white',
}

app.layout = html.Div(children=[
    html.Div(children=[
        html.H2('Bhumi NGO', style={'color': 'white','background-color': 'black','padding': '5px'}),
        html.P("One of India's largest NGO volunteer organizations"),
        html.P("Bhumi was founded on August 15, 2006 by a group of friends, who believed that every underprivileged child deserves quality education. Since then, Bhumi has transformed this conviction into a volunteering opportunity"),
        html.P("for India’s youth, launching a snowball effect of nurturing talent on the path to an educated, poverty-free India."),
    ], style={'padding': '0.05px'}),

    html.Div(children=[
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label="Center Details",  style=tab_style, selected_style=selected_tab_style, children=[
                html.Div(children=[
                    html.Label('Select a City to view the center location and project details ', style={'font-weight': 'bold', "margin-right": "10px"}),
                    dcc.Dropdown(
                        id="city-dropdown",
                        options=city_options,
                        value=city_options[0]["value"],
                        style={"width": "150px", "fontsize": "1px"}
                    ),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px', 'margin-bottom': '10px'}),
                html.Div(children=[
                    dcc.Slider(
                        id='children-slider',
                        min=0,
                        max=70,
                        step=10,
                        value=0,
                        marks={0: {'label': '0', 'style': {'color': '#77b0b1'}},
                            10: {'label': '10'},
                            20: {'label': '20'},
                            30: {'label': '30'},
                            40: {'label': '40'},
                            50: {'label': '50'},
                            60: {'label': '60'},
                            70: {'label': '70'}
                            })
              
                ], style = {'height': '12px','padding':'25px'}),

                html.Div(children=[
                    dcc.Graph(id='map-graph', style={'width': '50%','height':'500px', 'display': 'inline-block'}),
                    dcc.Graph(id='bar-graph', style={'width': '50%', 'height':'500px','display': 'inline-block'}),
                    #dcc.Graph(id='ratio-graph', style={'width': '50%', 'display': 'inline-block'})
                ])
            ]),

            dcc.Tab(label="About", style=tab_style, selected_style=selected_tab_style, children=[
                html.H1("About"),
                html.P("This is a Dash application that displays information about children centers in various cities."),
                html.P("The data for this application was sourced from the Centre_Details_Data.csv file."),
                html.P("The map and bar chart display information about the number of children available in each center and the subjects taught at each center."),
            ]),
            dcc.Tab(label="Datatable",  style=tab_style, selected_style=selected_tab_style,children=[
                html.H1("Data"),
                html.P("This data is obtained from Bhumi NGO"),
                html.Div([dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], id='tbl'),

            ], style={'height': '400px', 'overflow': 'auto'})
            ])
        ])
    ], style={'padding': '20px', 'background-color': '#F8F8FF',
            'fontSize': '16px'})
])

# Define the callbacks
@app.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value'),
     dash.dependencies.Input('children-slider', 'value')]
)
def update_map(city, children_range):
    filtered_df = df[(df['City'] == city) & (df['Children Available'].between(0,70))]
    fig = px.scatter_mapbox(
        filtered_df,
        lat='lat',
        lon='long',
        hover_name='Centre Name',
        hover_data=['Children Available'],
        opacity=0.7,
        zoom=10,
        mapbox_style='open-street-map'
    )
    fig.update_layout(autosize=True,
                      margin=dict(l=0, r=0, t=0, b=0))
    return fig

@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value'),
     dash.dependencies.Input('children-slider', 'value')]
)

def update_bar(city, children_range):
    filtered_df = df[(df['City'] == city) & (df['Children Available'].between(0, 70))]
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
