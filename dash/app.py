import os
import requests
import dash
from dash import dash_table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from pathlib import Path

from dash.dependencies import Output, Input, State
from pages import index

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../data/ra_datasource_ci_catalogue.xlsx')

xls = pd.ExcelFile(filename)
categories = xls.sheet_names
df = pd.DataFrame()
for sheet in categories:
    temp_df = pd.read_excel(xls, sheet)
    temp_df.insert(0,'Category',sheet)
    df=df.append(temp_df)
df = df.reset_index(drop=True)

app = dash.Dash(__name__,
                meta_tags=[{"name": "viewport",
                "content": "width=device-width, initial-scale=1"}],
                external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://pro.fontawesome.com/releases/v5.10.0/css/all.css'],
                suppress_callback_exceptions=True,
                update_title=None)
server = app.server
app.title = 'Data Catalogue'

app.layout = html.Div(children=[
        dcc.Location(id="url"),
        html.Div(id='sidebar', className='sidebar',children=index.create_sidebar(app,df)),
        html.Div(id='main', className='main', children='Updating ......'),
])

@app.callback(
    Output('main', 'children'),
    Output('results','children'),
    Input('search_filter','value'),
    Input('category_filter', 'value'),
    Input('sub_category_filter', 'value'),
    Input('org_filter', 'value'),
    Input('coverage_filter', 'value')
    )
def update_table(search_filter,category_filter, sub_category_filter, org_filter, coverage_filter):
    dff = df
    if search_filter != None:
        dff = dff[dff.apply(lambda row: row.astype(str).str.contains(
            search_filter, case=False).any(), axis=1)]
    if category_filter != []:
        dff = dff[dff['Category'].isin(category_filter)]
    if sub_category_filter != []:
        dff = dff[dff['Sub-category'].isin(sub_category_filter)]
    if org_filter != []:
        dff = dff[dff['Organisation'].isin(org_filter)]
    if coverage_filter != []:
        dff = dff[dff['Coverage'].isin(coverage_filter)]
    
    num_results = html.H2(str(len(dff)) + ' Results',className='text-right')
    table = index.create_catalogue_table(app,dff)
    return table, num_results



if __name__ == '__main__':
    app.run_server(debug=True)