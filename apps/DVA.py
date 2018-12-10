#Deliveries and Vitals Analyser
import base64
import datetime
import io

import dash_table
from dash.dependencies import Input,State,Event,Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table_experiments as dt

from app import app

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}
text_style = {
        'color':'#7FDBFF',
        'text-align':'justify'
        }
params = [
    'Pulse Rate', 'B.P.', 'Body Temperature', 'WBC Count','weight(opt)',
    'Hb', 'Blood Sugar'
]

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
                        html.Br(),
                        dcc.Tabs(id="tabs", value='tab-1', children=[
                        dcc.Tab(label='Imminent Delivery', value='tab-1',style=tab_style, selected_style=tab_selected_style),
                        dcc.Tab(label='Non-Iminent Delivery', value='tab-2',style=tab_style, selected_style=tab_selected_style),
                        ]),
                        ],className='six columns'),
                html.Div([
                        dcc.Upload(
                        id='upload-data',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select Files')
                        ]),
                        style={
                            'width': '90%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px',
                            'color':colors['text']
                        },
                        # Allow multiple files to be uploaded
                        multiple=True
                    ),
                    html.Div(id='output-data-upload-vitals'),
                    #html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
                                        ],className='six columns')
                
                ],className='row'),
        html.Div([
                html.Div([
                        html.Div(id='tabs-content')
                        ],className='six columns')
                ],className='row'),
html.Br(),
#fourth row
        html.Div([
                dash_table.DataTable(
                        id='table-editing-simple',
                        columns=(
                            [{'id': 'Serial', 'name': 'Serial'}] +
                            [{'id': p, 'name': p} for p in params]
                        ),
                        data=[
                            dict(Model=i, **{param: 0 for param in params})
                            for i in range(1, 5)
                        ],
                        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                        style_cell={
                                'backgroundColor': 'rgb(50, 50, 50)',
                                'color': 'white'
                                },
                        editable=True
                    ),
                    dcc.Graph(id='table-editing-simple-output', style = {'height': 360})
                ],className='row')

#layout-close
])

#callbacks

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.P(
                    children = 'Give one dose of dexamethasone(6mg Intramuscular) and prepare for delivery and neonatal resuscitation.',
                    style = text_style
                    )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.P(
                    children = 'Give one pre-referral dose of dexamethasone(6mg Intramuscular) if the patient is to be referred otherwise complete the course. Check Vitals.',
                    style = text_style
                    )
        ])
            
@app.callback(
    Output('table-editing-simple-output', 'figure'),
    [Input('table-editing-simple', 'data'),
     Input('table-editing-simple', 'columns')])
                            
                            
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    return {
        'data': [{
            'type': 'parcoords',
            'dimensions': [{
                'label': col['name'],
                'values': df[col['id']]
            } for col in columns]
        }],
        'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
    }
                
                
#upload files callback and handler

if __name__ == '__main__':
    app.run_server(debug=True)