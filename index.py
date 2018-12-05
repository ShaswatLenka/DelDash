#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:52:06 2018

@author: jarvis
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import GLA,DVA,NTC,NEO,ALD,OVP

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/GLA':
         return GLA.layout
    elif pathname == '/apps/DVA':
         return DVA.layout
    elif pathname == '/apps/NTC':
         return NTC.layout
    elif pathname == '/apps/NEO':
         return NEO.layout
    elif pathname == '/apps/ALD':
         return ALD.layout
    elif pathname == '/apps/OVP':
         return DVA.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
