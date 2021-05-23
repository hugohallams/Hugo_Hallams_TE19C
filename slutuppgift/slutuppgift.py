from dash_core_components.Dropdown import Dropdown
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as HTML
from dash.dependencies import Input, Output
import plotly.express as px 
import plotly.subplots as sp

app = dash.Dash(__name__)

#Varibler för datastrukturer
df = pd.read_csv("Gender_Data.csv")
df_reg = pd.read_csv("Regional_Totals_Data.csv")


app.layout = HTML.Div(children=[ 

    #Dropdown med två alternativ.
    dcc.Dropdown(
        id="drop1",
        options=[dict(label="Statistik om antal fall", value="Total_Cases"), dict(
            label="Statistik om antal dödsfall", value="Total_Deaths")],
        value="Total_Cases"
    ),
    
    dcc.Graph(
        id="Graph1",
    ),

    dcc.Graph(
        id="Graph2",
    ),
])
#Gör så att det visas det crikeldagram som man väljer i dropdown
@app.callback(
    Output("Graph1", "figure"),
    [Input("drop1", "value")]
)
#Skapar ett cirkeldiagram av datan från Gender_Data
def update_figure(value):
    fig = px.pie(df, names='Gender', values=value)
    fig.update_layout(transition_duration=500)
    return fig

#Gör så att det visas det stapeldiagram man väljer i dropdown
@app.callback(
    Output("Graph2", "figure"),
    [Input("drop1", "value")]
)
#Gör stapeldiagram från Regional_Totals_Data
def update_figure2(value):
    fig = px.bar(df_reg, x="Region", y=value)
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

