# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


df = pd.read_csv('data/d_gold.csv')

#fig = px.line(df, x="date", y="America")

app.layout = html.Div(children=[
    html.H1(children=''),

    html.Div(children='''
        This grpahs shows the gold/dolar
    '''),
    dcc.Dropdown(
        id='dropdown_1',
        options=[
            {'label': 'America', 'value': 'America'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'China', 'value': 'China'},
            {'label': 'Korea', 'value': 'Korea'}
        ],
        value='America'
    ),
    dcc.Graph(
        id='graph_1'
    )
])

@app.callback(Output('graph_1', 'figure'), [Input('dropdown_1', 'value')])
def update_graph(selected_dropdown_value):
    print(selected_dropdown_value)
    
    return {
        'data': [{
            'x': df['date'],
            'y': df[selected_dropdown_value]
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)