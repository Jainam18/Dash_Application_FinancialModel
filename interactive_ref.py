# importing necessary libraries.
import pandas as pd
import datetime as dt
import plotly
import plotly.express as px
import dash_bootstrap_components as dbc

from dash import html, Dash, dcc

from dash.dependencies import Input, Output, State

# Additional Libraries
from string import Template
import plotly         
import plotly.express as px
import plotly.io as pio

app = Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP])

# -----------------------------------------------------------------------

# df = pd.read_excel("CombinedData.xlsx")
# print(df.head())

# -----------------------------------------------------------------------

app.layout = html.Div(style={'backgroundColor': "#11F6E1"}, children=[
    html.H1('DEPARTMENT WISE SALARY',
        style={
            'textAlign': 'center',
            'color': '#114FF6',
            'font_size':50
        }
    ),
 # INCOMPLETE 
    dbc.Container([
    dbc.Row([
            dbc.Col([
               html.Div(style={'width':"60%",'backgroundColor': 'green',"margin-left":"259px"}, children=[
                        html.P(
                            children='Expenditure For Positions in Creatives and HR Department',
                            style={
                    'textAlign': 'center',
                    'color': 'pink',
                    'font_size':20,
                    'backgroundColor': '#d7ffcd'
                }), 
                html.Br(),
                html.Label(['Select Department'],style={'font-weight': 'bold', "text-align": "center"}),
                dcc.Dropdown(options=['HR','CombinedData','Creatives'], value='CombinedData', clearable=True, id='Department'),
                html.Label(['Select Positions'],style={'font-weight': 'bold', "text-align": "center"}),
                dcc.Dropdown(id='Positions',
                    options=[
                            {'label': 'Manager', 'value': 'Manager'},
                            {'label': 'Video editor', 'value': 'Video editor'},
                            {'label': 'Video editor(Interns)', 'value': 'Video editor(Interns)'},
                            {'label': 'Contingency team(Video Editing)	', 'value': 'Contingency team(Video Editing)	'},
                            {'label': 'Content designer', 'value': 'Content designer'},
                            {'label': 'Content designer(Intern)', 'value': 'Content designer(Intern)'},
                            {'label': 'Contingency team(Content Designing)', 'value': 'Contingency team(Content Designing)'},
                            {'label': 'Content writer', 'value': 'Content writer'},
                            {'label': 'Content writer(Intern)', 'value': 'Content writer(Intern)'},
                            {'label': 'Contingency team(Content writing)', 'value': 'Contingency team(Content writing)'},
                            {'label': 'HR manager', 'value': 'HR manager'},
                            {'label': 'Recruiter', 'value': 'Recruiter'}

                    ],
                    optionHeight=35,                    
                    value='Manager',                  
                    disabled=False,                    
                    multi=False,                       
                    searchable=True,                    
                    search_value='',                    
                    placeholder='Please select...',     
                    clearable=True,                     
                    style={'width':"100%"},             
                    ), 
                html.Br(),
                html.Label(['Enter the number of Employees'],style={'font-weight': 'bold', "text-align": "left"}), 
                dcc.Input(id='no_of_emp',type='number',placeholder='',style={'display':'inline-block'}),
                html.Br(), 
                html.Label(['Calculator :'],style={'font-weight': 'bold', "text-align": "center"}),
                html.Div(id='output_container', children=[
                    html.Plaintext(id='text'),
                    html.Plaintext(id='text1'),
                    html.Plaintext(id='text2')
                ]),
                html.Br()   
            
    ])
        
        ,
        html.Div(style={'backgroundColor': "#11F6E1",
        'width' : 10, 'height': 20, 'padding-left': '500px'}, children=[
            dbc.Col([dcc.Graph(id='Graph-1')])
        ])
        
    ])
    ]),

    dbc.Row([
        html.Div(style={
        'width' : 10, 'height': 20, 'padding-top': '350px'}, children=[
            dbc.Col([
            html.H3("FREQUENCY VS SALARIES",style={
                'textAlign' : 'center',
                'color' : '#114FF6',
                'font_size' : 10
            }),
            dcc.Graph(id='Graph-2')
        ], )
    ]),
]),
    ])  
])



# INCOMPLETE
# dcc.Dropdown(options=['HR','CombinedData','Creatives'], value='CombinedData', clearable=True, id='Department'),
#                 html.Br(),
#                 dcc.Dropdown(options=[1,2,3], value=1, clearable=True, id='no_of_employees') ,
#                 html.Br()
# -----------------------------------------------------------------------

@app.callback(
    [Output('Graph-1','figure'),
    Output('Graph-2','figure')],
    [Input('Department','value')]
)

def graphs(Department):
    df = pd.read_excel(f"{Department}.xlsx")
    # Piechart Creation
    piechart = px.pie(
        data_frame=df,
        values='Salary/month/employee',
        names='Position',
        color='Position',                      
        
        hover_name='Salary/month',                     
        
        hole=0.1
        )
    piechart.update_traces(textinfo='value+label', opacity=1, rotation=190)

    # Bar graph
    barchart1 = px.bar(
    data_frame=df,
    x="Salary/month",
    y="Number of employees",
    color="Position",              
    opacity=0.8,                  
    orientation="v",             
    barmode='relative',        
    
    text='Number of employees',            
    hover_name='Position',
    title="Creatives Table",
    template='plotly_white',

    labels={"Salary/year":"Salary per year", "Salary/month":"Salary per month"}
)
    return piechart,barchart1

@app.callback(
    [Output('text','value'),
    Output('text2','value'),
    Output('text3','value')],
    [Input('no_of_emp','value'),
    Input('Position','value')]
)

def calculator_output(no_of_emp,Position,Department):
    df = pd.read_excel(f"{Department}.xlsx")
    dff=df[df['Position'] == Position]
    text = dff['Salary/month/employee']*no_of_emp
    text1 = dff['Salary/month']
    text2 = dff['Salary/year/employee']*no_of_emp
    return text,text1,text2


#-------------------------------------------------------------------------

if __name__=='__main__':
    app.run(port=8004)

    