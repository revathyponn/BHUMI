import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html, dash_table
import dash_bootstrap_components as dbc

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
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
# Define the style for the tabs
tab_style = {
    'height': '30px',
    'padding': '8px',
}

# Define the style for the selected tab
selected_tab_style = {
    'height': '30px',
    'padding': '3px',
    'borderTop': '2px solid #f5f5f5',
    'borderBottom': '2px solid #f5f5f5',
    'backgroundColor': '#119DFF',
    'color': 'white',
}

app.layout = html.Div(children=[
    html.Div(children=[
        html.H2('Bhumi NGO', style={'color': 'white','background-color': 'black','padding': '5px'}),
        # html.P("One of India's largest NGO volunteer organizations"),
        # html.P("Bhumi was founded on August 15, 2006 by a group of friends, who believed that every underprivileged child deserves quality education. Since then, Bhumi has transformed this conviction into a volunteering opportunity"),
        # html.P("for India’s youth, launching a snowball effect of nurturing talent on the path to an educated, poverty-free India."),
    ], style={'padding': '0.05px'}),

    html.Div(children=[
        dcc.Tabs(id="tabs", value = 'Center Details',children=[
            
            dcc.Tab(label="About", style=tab_style, selected_style=selected_tab_style, children=[
                html.H1("About"),
                html.P('''Bhumi is a non-profit organization that aims to empower underprivileged children and youth in India through education. Founded in 2006, Bhumi works towards providing quality education to children who come from marginalized backgrounds and lack access to basic educational facilities. With a vision of creating an equal society, Bhumi operates across multiple states in India and engages with over 25,000 volunteers to drive social change.
                       Bhumi offers a range of programs that focus on areas such as education, skill development, and environmental sustainability. Their flagship program, the Ignite Program, focuses on providing education and life skills to children from orphanages, shelters, and slum communities. Additionally, Bhumi also conducts several other programs such as the Career Development Program, which aims to provide career guidance and mentorship to underprivileged youth, and the Green Bhumi Program, which focuses on promoting environmental sustainability. Through their various initiatives, Bhumi has impacted the lives of thousands of children and youth, providing them with opportunities to realize their full potential and lead a better life.'''),
                html.P('''Though Bhumi is one of the largest volunteering organisations in India, when they approach new shelter homes to explain what they are doing, what they have achieved, what is their strength and how they have been doing, they need a tool to showcase their capabilities. They conduct orientation session to individuals to register themselves as volunteers. Bhumi people need to explain to individuals about the location of the centers in the city, number of the kids in the center and the existing number of volunteers in that particular shelter home and the number of volunteers they are in need of. Is there an application, where we can access alll these information about Bhumi to approach Shelter homes and prospective volunteers? This is the question that our application `Bhumi` aims to address.'''),

html.P('''Sriram is a 20-year old student and is interested in volunteering in Bhumi in one of the shelter home in Chennai, India. He would like to volunteer for the center which is in dire need of volunteer and is also near to his place where he resides. Further, though Bhumi has been teaching various subjects to the kids, he has specific favourite subject mathematics that he wants to teach to the kids. With these conditions in mind, he can use the application Bhumi to see the location of all the centers where Bhumi is involved to identify the nearest one to his residence. He can also compare the children available and the volunteer available for each center which will make him understand which center is in immediate need of volunteers. Sriram can use application `Bhumi` in order to make a choice that matches his conditions. Through the `Bhumi` application, Sriram will be able to interactively select those centers teaching Maths in Chennai and compare distance, volunteer count and children count in those center to take decision for the volunteering in that particular center.'''),

html.P('''Mabu is a head of the shelter home and has been hearing a lot about the Bhumi which has been sending their volunteers to educate the children in shelter homes. Before approaching Bhumi he would like to understand where are the centers which are being benefitted by Bhumi located and the number of kids in those center. Also, the number of volunteers that are taking classes in every center. He would like to know the subjects that are taught by Bhumi Volunteers in other centers and if kids in his center would require assistance for those subjects such as computer science.  He would like to understand the overall performance of the Bhumi in India, so that he can approach his management to make them understand the performance of Bhumi and how the kids in his center will be benefitted if Bhumi Volunteers educate the kids in his center.'''),

html.P('''The data on which the application `Bhumi` is based on India with specific as a reference point, therefore, the target market for our application is any individual living in those cities and Shelter homes located in those cities. The `Bhumi` will guide them in making a more informed decision about the center they wish to volunteer.'''),
            ]),
            dcc.Tab(label="Center Details", value = 'Center Details', style=tab_style, selected_style=selected_tab_style, children=[
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
                    dcc.Graph(id='map-graph', style={'width': '50%','height':'500px', 'display': 'inline-block','border': '2px solid #ccc',
        'border-radius': '5px',
        'padding': '10px'}),
                    dcc.Graph(id='bar-graph', style={'width': '50%', 'height':'500px','display': 'inline-block','border': '2px solid #ccc',
        'border-radius': '5px',
        'padding': '10px'}),
                    #dcc.Graph(id='ratio-graph', style={'width': '50%', 'display': 'inline-block'})
                ])
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
    [dash.dependencies.Input('city-dropdown', 'value')]
)
def update_map(city):
    filtered_df = df[(df['City'] == city)]
    fig = px.scatter_mapbox(
        filtered_df,
        lat='lat',
        lon='long',
        hover_name='Centre Name',
        hover_data=['Children Available','Volunteer count','Subject'],
        opacity=0.7,
        zoom=10,
        mapbox_style='open-street-map',
       color_discrete_sequence=['black']
        
    )
    fig.update_layout(autosize=True,title=dict(
            text='Map of Children Centers in {}'.format(city),
            y=0.99,
            x=0.5,
            pad=dict(t=20, b=20, l=20, r=20),
            # bgcolor= 'rgba(0,0,0,0)',
            xanchor='right',
            yanchor='top'
        ),
        margin=dict(l=0, r=0, t=0, b=0))
    return fig
@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value')]
)

def update_bar(city):
    filtered_df = df[(df['City'] == city)]
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
