import pandas as pd
import plotly
import plotly.express as px

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output,State

app = dash.Dash(__name__)

df = pd.read_excel("C:\\Users\\Aditi\\Downloads\\Salary and Months.xlsx")

app.layout = html.Div([

        html.Div([
            html.Pre(children= "Expenditure of Ozibook Ltd",
            style={"text-align": "center", "font-size":"125%", "color":"black"})
        ]),

html.Div([
            html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Position', 'value': 'Position'}

                ],
                value='Position',
                style={"width": "50%"}
            ),
        ]),

html.Div([
            html.Br(),
            html.Label(['Y-axis values to compare:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                         {'label': 'Month 1', 'value': 'Month 1'},
                         {'label': 'Month 6', 'value': 'Month 6'},
                         {'label': 'Month 12', 'value': 'Month 12'},
                         {'label': 'Month 18', 'value': 'Month 18'},
                         {'label': 'Month 24', 'value': 'Month 24'},
                         {'label': 'Total Expenditure in Two years', 'value': 'Total Expenditure in two years'}

                ],
                value='Month 1',
                style={"width": "50%"}
            ),
        ]),

html.Div([
        dcc.Graph(id='the_graph')
    ]),

])

#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)

def update_graph(x_axis, y_axis, barmode="group"):

    dff = df
    # print(dff[[x_axis,y_axis]][:1])

    barchart=px.bar(
            data_frame=dff,
            x=x_axis,
            y=y_axis,
            title=y_axis+': by '+x_axis,
            color="Position",
            barmode="group"
            )

    barchart.update_layout(xaxis={'categoryorder':'total descending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

    return (barchart)

if __name__ == '__main__':
    app.run_server(debug=True)