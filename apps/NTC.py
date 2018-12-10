#NTSV C-Sections
import dash_table
import pandas as pd

import plotly.graph_objs as go
from dash.dependencies import Input,State,Event,Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

from app import app

df = pd.read_csv('apps/test/test-dataset/EMR.csv')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#first row
    html.Div([
        html.H2(
        children='DelDash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
        )
        ],className='row'),
#second row
                 html.Div([
                html.Div([
                        
                        ],className='one columns'),
                html.Div([
                dcc.Link('General & Labor', href='/apps/GLA'),        
                        ],className = 'two columns'),
                
                html.Div([
                dcc.Link('Delivery & Vitals', href='/apps/DVA'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('Timeline', href='/apps/TIM'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('NTSV-C Section', href='/apps/NTC'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('Performance Metrics', href='/apps/OVP'),        
                        ],className = 'two columns'),
                html.Div([
                        
                        ],className='one columns'),
                ],className = 'row'),
                html.Br(),
#third row
    html.Div([
            
            html.Div([
                    
                    ],className='one columns'),

            html.Div([
                    dcc.Upload(
                        id='datatable-upload-NTSV',
                        children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Files')
                                ]),
            style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed',
            'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px','color':colors['text']
                    },
                )
                    ],className = 'eleven columns')
            
            ],className='row'),html.Br(),
#fourth row
    html.Div([
            
            dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
            },
            ) 
            ],className='row'),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br()
                      
        

#layout-close
 ])