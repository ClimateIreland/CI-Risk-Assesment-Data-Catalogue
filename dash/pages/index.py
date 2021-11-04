from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd


def create_sidebar(app, df):

    def get_unique(series):
        series = series.dropna().sort_values()
        unique = series.unique()
        return unique

    category_filter = dbc.Form(
        [
            dbc.Label(
                'Category',
                className='filter-label'),
            dcc.Checklist(
                id="category_filter",
                options=[
                    {"label": "{0} ({1})".format(val, (df['Category'].values == val).sum()),
                     "value": val} for val in get_unique(df['Category'])
                ],
                value=[],
                labelStyle={'display': 'block', }
            ),
        ],
    )

    sub_category_filter = dbc.Form(
        [
            dbc.Label(
                'Sub-category',
                className='filter-label'),
            dcc.Checklist(
                id="sub_category_filter",
                options=[
                    {"label": "{0} ({1})".format(val, (df['Sub-category'].values == val).sum()),
                     "value": val} for val in get_unique(df['Sub-category'])
                ],
                value=[],
                labelStyle={'display': 'block', }
            ),
        ],
    )

    org_filter = dbc.Form(
        [
            dbc.Label(
                'Organisation',
                className='filter-label'),
            dcc.Checklist(
                id="org_filter",
                options=[
                    {"label": "{0} ({1})".format(val, (df['Organisation'].values == val).sum()),
                     "value": val} for val in get_unique(df['Organisation'])
                ],
                value=[],
                labelStyle={'display': 'block', }
            ),
        ],
    )

    coverage_filter = dbc.Form(
        [
            dbc.Label(
                'Coverage',
                className='filter-label'),
            dcc.Checklist(
                id="coverage_filter",
                options=[
                    {"label": "{0} ({1})".format(val, (df['Coverage'].values == val).sum()),
                     "value": val} for val in get_unique(df['Coverage'])
                ],
                value=[],
                labelStyle={'display': 'block', }
            ),
        ],
    )

    sidebar = html.Div(
        className='sidebar',
        children=[
            html.Div(id='results'),
            dbc.Input(
                id="search_filter",
                placeholder='Search'),
            category_filter,
            sub_category_filter,
            org_filter,
            coverage_filter
        ]
    )

    return sidebar

                  
def create_catalogue_table(app, df):
    catalogue_table = []
    for index, row in df.iterrows():
        dataset_item = dbc.Container(
            className='dataset-item',
            children=[
                dbc.Row(
                    className='dataset-header',
                    children=[
                        html.H2(
                            className='dataset-title-text',
                            children=html.A(
                                row['Title'],
                                href=row['URL'],
                                target='_blank'
                            )),
                        html.Div(
                            row['Organisation'],
                            className='dataset-organisation-text',
                        )
                    ]),
                dbc.Container(
                    className='dataset-content',
                    children=[
                        dbc.Row(
                            dbc.Col(
                                children=[
                                    dbc.Row(str(row['Access to Dataset'])),
                                    dbc.Row(str(row['Description']))

                                ]
                            )),
                        dbc.Row(

                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Row('Updated: ' + \
                                                str(row['Data Update'])),
                                        dbc.Row('Contact: ' + \
                                                str(row['Contact'])),
                                        dbc.Row('Resolution: ' + \
                                                str(row['Resolution'])),
                                    ]
                                ),
                                dbc.Col(
                                    className="text-right dataset-meta",
                                    children=[
                                        dbc.Row('Category: ' + \
                                                str(row['Category'])),
                                        dbc.Row('Sub-category: ' + \
                                                str(row['Sub-category'])),
                                        dbc.Row('Coverage: ' + \
                                                str(row['Coverage'])),
                                    ]
                                ), ]
                        ), ])
            ]
        )

        catalogue_table.append(dataset_item)

    return catalogue_table
