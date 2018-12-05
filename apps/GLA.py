#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:32:27 2018

@author: Shaswat Lenka

A medical dashboard for accessing and visualizing the antenatal parameters and recommending
Corticosteroid administration in case of preterm labor
"""
import plotly.graph_objs as go
from dash.dependencies import Input,State,Event,Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

from app import app

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#first row
    html.Div([
        html.H2(
        children='iDelDash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
        )
        ],className='row'),
#second row
        html.Div([
                html.Div([
                dcc.Link('General & Labor', href='/apps/GLA'),        
                        ],className = 'two columns'),
                
                html.Div([
                dcc.Link('Delivery & Vitals', href='/apps/DVA'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('NTSV-C Section', href='/apps/NTC'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('Neonatal', href='/apps/NEO'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('All Deliveries', href='/apps/ALD'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('Overall Performance', href='/apps/OVP'),        
                        ],className = 'two columns'),
                ],className = 'row'),
html.Br(),
#third row
    html.Div([
            html.Div([
            html.Div([
                    html.H4(
                            children = '    General Information',
                            style = {
                                    'color':'#FF2A9C'
                                }
                            ),
                    html.H6(
                            children='Patient ID',
                            style={
                                    'color':colors['text']
                                    }
                            ),
                    dcc.Input(
                            placeholder='Enter ID',
                            type='text',
                            value='',
                            style={'width': '100%'}
                            )
                    ],className='four columns'),
            html.Div([
                    html.Label(
                            children='Gestational Age (in weeks)',
                            style={
                                   'textAlign':'center',
                                   'color':colors['text']
                                  }
                            ),
                    dcc.Slider(
                    id = 'Age-Slider',
                    min=24,
                    max=34,
                    step=0.5,
                    marks={i: '{}'.format(i) if i == 24 else str(i) for i in range(24, 35)},
                    value=34,
                    )
                    ],  className='four columns'),
            html.Div([
                    
                    html.Label(
                            children='Date:(YY/MM/DD)',
                            style={
                                   'color':colors['text']
                                  }
                            ),
                    dcc.DatePickerSingle(
                                        id='date-picker-single',
                                        date=dt(1997, 5, 10),
                                        )   
                    ],className='four columns')
            ],className='row'),

    html.Div([
            html.Div([
                   
                    html.H4(
                            children = 'Labor Information',
                            style = {
                                    'color':'#FF2A9C'
                                }
                            ),
                    html.H6(
                            children='Onset of Labor pain (in 24Hrs Format)',
                            style={
                                   'color':colors['text']
                                  }
                            ),
                    dcc.Input(id='laborFreq', value='',type='text',style={'width': '100%'}),
                    #html.Br(),
                    html.Button(id='timeSubmit', type='submit', children='TimePlot',),
                    html.Button(id='freqSubmit', type='submit', children='FreqPlot'),
                    html.H4(
                            children='Select Symptoms',
                            style={
                                   'color':'#FF2A9C'
                                  }
                            ),
                    dcc.Dropdown(id = 'pieIn',
                    options=[
                        {'label': 'CVD', 'value':2.1},
                        {'label': 'LBP', 'value':0.3},
                        {'label': 'ABP','value': 0.2},
                        {'label': 'PIT','value': 0.7},
                        {'label': 'SWP','value': 0.7},
                    ],
                    multi=True,
                    value="MTL"
                    ),
                    html.Button(id='sympSubmit', type='submit', children='GO!',), 
                    ],className='four columns',style = {'color':colors['text']}
                    ),
                    html.Div(id='laborFreqOut',className='four columns'),
                    html.Div(id='laborSpectroOut', className='four columns'),
            ],className='row'),

    html.Div([
            html.Div([
                    
                    html.H4(
                            children = 'Additional Symptoms/Comments',
                            style = {
                                    'color':'#FF2A9C'
                                }
                            ),
                            dcc.Textarea(
                            placeholder='Additional Symptoms/Comments',
                            value='',
                            style={'width': '100%'}
                        ),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                           
                    ],className='four columns'),
                            
            html.Div([
                     html.Div(id='pieOut'),
                    ],className='five columns'),
                    
            html.Div([
                    
                    ],className='three columns')
            ], className='row'),
                    
                
            ])
    
        

])           
#callback for symptoms multiselect
@app.callback(Output('pieOut', 'children'),[],[State('pieIn', 'value')],[Event('sympSubmit', 'click')])

def update_output(value):
    labels = ['True labor','False Labor']
    values = [sum(value),4-sum(value)]
    return dcc.Graph(
            figure = go.Figure(
                    data = [
                            go.Pie(labels=labels, values=values)
                            ],
                        layout=go.Layout(
                        title='Predictions based on inputs',
                        plot_bgcolor = colors['background'],
                        paper_bgcolor = colors['background'],
                            font = dict(
                            color = colors['text']
                            ),
                        )
                    ),
                        style={'height':260}
            )


@app.callback(Output('laborFreqOut', 'children'), [], [State('laborFreq', 'value')], [Event('timeSubmit', 'click')])


def update_time_out(input_value):
    #x = np.linspace(0,24,25)
    x = input_value.split()
    return dcc.Graph(
        id='Labor Chart',
        style = {
                'height': 300
                },
                
        figure={
            'data': [
                {
                    'x': x,
                    'y': ['labor onset' for x in range(0, len(x))] ,
                    'name': 'Onset of pain',
                    'mode': 'markers',
                    'marker': {'size': 12,
                               'color':'rgb(238, 125, 51)'
                               }
                }
            ],
            'layout': {
                'title': 'Time domain analysis of labor onset',
                'xlabel': 'time in 24HRS format',
                'ylabel': 'Pain Onset',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
@app.callback(Output('laborSpectroOut', 'children'),[], [State('laborFreq', 'value')], [Event('freqSubmit', 'click')])

def update_frequency_out(input_value):
    y = []
    x = []
    ctr=0
    n = input_value.split()
    n = [ float(y) for y in n ]
    print(n)
    for i in range(len(n)-1):
        if(n[i+1]-n[i] < 1):
            ctr = ctr+1
            if(int(n[i+1])!=int(n[i])):
                x.append(int(n[i]))
                y.append(ctr)
                ctr = 0
        elif(n[i+1]-n[i] >= 1):
            if(int(n[i+1])!=int(n[i])):
                x.append(int(n[i]))
                y.append(ctr)
                ctr = 0
    return dcc.Graph(
    figure=go.Figure(
        data=[
            go.Bar(
                x=x,
                y=y,
                name='Frequency data',
                marker=go.bar.Marker(
                    color='rgb(238, 125, 51)'
                )
            ),
        ],
        layout=go.Layout(
            title='Frequency domain analyais of labor onset',
            plot_bgcolor = colors['background'],
            paper_bgcolor = colors['background'],
            font = dict(
                    color = colors['text']
                    ),
            yaxis=dict(
            title='<i>Frequency</i>'
            ),
            xaxis=dict(
            title='<i>time(nth hour)</i>'
            )
        )
    ),
    style={'height': 300}
)