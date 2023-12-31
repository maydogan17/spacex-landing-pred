# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly_express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("falcon9_data.csv")
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()
sites = spacex_df['LaunchSite'].unique()
sites_dict = {}
sites_dict['default'] = 'All Sites'
for site in sites:
    sites_dict[site] = site
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown', options=sites_dict,
                                value = 'All Sites',
                                placeholder = 'Select a Launch Site here',
                                searchable = True),
                                html.Br(),
                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                min=0, max=10000, step=1000,
                                value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'All Sites':
        fig = px.pie(spacex_df, values='Class', 
        names='LaunchSite', 
        title='Total Succes Launches by Site')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        title = 'Total Succes Launches for Site ' + entered_site
        fig = px.pie(filtered_df, values=filtered_df['Class'].value_counts().values, 
        names=[0,1], 
        title=title)
        return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
            [Input(component_id='site-dropdown', component_property='value'),
            Input(component_id="payload-slider", component_property="value")])
def get_scatter_plot(entered_site, payload):
    if entered_site == 'All Sites':
        filtered_df = spacex_df
        low, high = payload
        mask = (filtered_df['PayloadMass'] > low) & (filtered_df['PayloadMass'] < high)
        fig = px.scatter(filtered_df[mask], x="PayloadMass", y="Class", color="LaunchSite")
        return fig
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        low, high = payload
        mask = (filtered_df['PayloadMass'] > low) & (filtered_df['PayloadMass'] < high)
        fig = px.scatter(filtered_df[mask], x="PayloadMass", y="Class", color="LaunchSite")
        return fig


# Run the app
if __name__ == '__main__':
    app.run_server()