import base64
import io

import plotly.graph_objs as go
from dash.dependencies import Input,State,Event,Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd

from app import app

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
                ],className = 'row')
                , html.Br(),
#third row
    html.Div([
            html.Div([
                dcc.Upload(
                        id='datatable-upload',
                        children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Files')
                                ]),
            style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed',
            'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px','color':colors['text']
                    },
                ),
           
                    ],className='six columns'),
            html.Div([
                     dcc.Upload(
                        id='upload-image',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select Files')
                        ]),
                        style={
                            'width': '95%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px',
                            'color': colors['text']
                        },
                        # Allow multiple files to be uploaded
                        multiple=True
                    )
                    ],className='six columns')
            ],className='row'),html.Br(),
#fourth row
    html.Div([
            html.Div([
                       dash_table.DataTable(id='datatable-upload-container-1'),
                       html.Div(id='datatable-upload-graph-1'),
                       dash_table.DataTable(id='datatable-upload-container-2'),
                       html.Div(id='datatable-upload-graph-2')
                    ],className='six columns'),
            html.Div([
                 html.Div(id='output-image-upload'),
                    ],className='six columns')
            ],className='row'),html.Br()
#layout-close
])

#image
def parse_contents_img(contents, filename, date):
    return html.Div([
        html.Img(src=contents),
  
    ])


@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents')],
              [State('upload-image', 'filename'),
               State('upload-image', 'last_modified')])
def update_output_image(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents_img(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

#output graph
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file
        return pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an excel file
        return pd.read_excel(io.BytesIO(decoded))


@app.callback(Output('datatable-upload-container-1', 'data'),
              [Input('datatable-upload', 'contents')],
              [State('datatable-upload', 'filename')])
def update_output_one(contents, filename):
    if contents is None:
        return [{}]
    df = parse_contents(contents, filename)
    return df.to_dict('rows')


@app.callback(Output('datatable-upload-graph-1', 'children'),
              [Input('datatable-upload-container-1', 'data')])
def display_graph_one(rows):
    df = pd.DataFrame(rows)
    return dcc.Graph(
                     figure = go.Figure(
                                     data = [
                                             go.Scatter(
                                                     x= df[df.columns[0]],
                                                     y = df[df.columns[1]],
                                                     name='Hbg',
                                                     line = dict(
                                                        color = (colors['text']),
                                                        width = 4
                                                        )
                                                     ),
                                             go.Scatter(
                                                     x= df[df.columns[0]],
                                                     y = df[df.columns[3]],
                                                     name='WBC',
                                                     line = dict(
                                                        color = ('orange'),
                                                        width = 4
                                                        )
                                                     )
                                             ],
                                    layout = go.Layout(
                                            title='Vitals Timeline',
                                            plot_bgcolor = colors['background'],
                                            paper_bgcolor = colors['background'],
                                            font = dict(
                                            color = colors['text']
                                            )
                                        )
                                     ),
                        style={
                             'height':500,
                             'width':700,
                             },
   )
