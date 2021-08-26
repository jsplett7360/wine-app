# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sklearn
import pandas as pd
#import scikit-learn

# Imports from this application
from app import app
from joblib import load
pipeline = load("assets/pipeline.joblib")

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Elevation', 'value'), Input('Continent', 'value')],
)

def predict(year, continent):
    df = pd.DataFrame(
        columns = ['year', 'continent'],
        data = [[year, continent]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} years'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
        html.H2('Predicted IMBD Rating', className = 'mb-5'),
        html.Div(id = 'prediction-content', className = 'lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className = 'mb-5'),
        dcc.Markdown('#### Alcohol'),
        dcc.Slider(
            id='Alcohol',
            min=8,
            max=15,
            step=.5,
            value=10,
            marks={n: str(n) for n in range(8,15,50)},
            className='mb-5',
        ),
        dcc.Markdown('#### Alcohol'),
        dcc.Dropdown(
            id='Alcohol',
            options = [
                {'label': '15', 'value': '15'},
                {'label': '13', 'value': '13'},
                {'label': '11', 'value': '11'},
                {'label': '9', 'value': '9'},
            ],
            value = '9',
            className='mb-5',
        ),

    ],
)

layout = dbc.Row([column1, column2])
