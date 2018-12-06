#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:02:49 2018

@author: jarvis
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
        html.Div([
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
                dcc.Link('All Deliveries', href='/apps/ALD'),        
                        ],className = 'two columns'),
                html.Div([
                dcc.Link('Overall Performance', href='/apps/OVP'),        
                        ],className = 'two columns'),
                ],className = 'row'),

#layout-close
])