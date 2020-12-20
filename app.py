# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:57:30 2020

@author: Mohamed Sabri
"""

#pip install dash --force-reinstall --user
#pip install dash-renderer 
#pip install dash-html-components
#pip install dash-core-components  
#pip install plotly --upgrade

#https://dash-gallery.plotly.host/dash-oil-and-gas/

#https://github.com/plotly/dash-sample-apps/blob/master/apps/dash-oil-and-gas/app.py

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import Flask
import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

os.environ["OPENAI_CONFIG"] = 'openai.cfg'

bully_main = pd.read_csv(r'\assets\bully_main.csv')

bullying = bully_main[bully_main['Decision']=='This is probably a bullying situation']

not_bullying = bully_main[bully_main['Decision']=='No bullying detected, note that it can be something else (adult content, spammer, sexual harassment, etc)']

bully1 = [7,8,9,10,11,12,13,14,15]

nobully1 = [0,1,2,3,4,5,6]

from api import GPT, Example

gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
for j in range(0,1):
    for i in range(len(bully1)):
        gpt.add_example(Example(bully_main['Tweets'][bully1[i]],'This is probably a bullying situation'))
    
for i in range(len(nobully1)):
    gpt.add_example(Example(bully_main['Tweets'][nobully1[i]],'No bullying detected, note that it can be something else (adult content, spammer, sexual harassment, etc)'))
    
external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "https://cdn.rawgit.com/plotly/dash-app-stylesheets/5047eb29e4afe01b45b27b1d2f7deda2a942311a/goldman-sachs-report.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]
    
server = Flask(__name__)

app = dash.Dash(server=server, external_stylesheets=external_css)

for css in external_css:
    app.css.append_css({ "external_url": css })

external_js = [ "https://code.jquery.com/jquery-3.2.1.min.js",
        "https://cdn.rawgit.com/plotly/dash-app-stylesheets/a3401de132a6d0b652ba11548736b1d1e80aa10d/dash-goldman-sachs-report-js.js" ]

for js in external_js:
    app.scripts.append_script({ "external_url": js })
    
app.layout = html.Div([
    html.H1(children='Cyberbullying detection', className = "gs-header gs-text-header padded"),
    html.Br(),
    html.Br(),
    html.Div([
            html.H2(children='Cyberbullying Examples'),
            html.P('your nasty crooked deformed titties sent my penis into hibernation.', className = 'blue-text'),
            html.P('You fucking retard ! you are nothing', className = 'blue-text'),
            html.P('Idiot ! you are so stupid', className = 'blue-text'),
            html.P('Fucking cunt ! you are nothing to me', className = 'blue-text')
            ]),
    html.Div([
    html.H2(children='''
        Please enter a sentence to test if it contains bullying.
    '''),
    html.Br(),
    html.Div(["Input: ",
              dcc.Input(id='my-input', type='text')]),
    html.Br(),
    html.Button('Submit', id='submit', type='submit'),
    html.Br(),
    html.H3(html.Div(id='my-output')),

])
    ], style={'width':'75%', 'margin':25, 'textAlign': 'center'})


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input('submit', 'n_clicks')],
    [State('my-input', 'value')])

def update_output_div(n_clicks,value):
    if n_clicks:
        out1 = gpt.get_top_reply(value)
        return 'Output: {}'.format(out1)


if __name__ == '__main__':
    app.run_server(debug=True)
