from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go
import random

from utils import (
    get_SVI_data,
    get_CT_data
)
from figures_utils import (
    get_figure
)


app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color
# colors = {"background": "#1F2630", "text": "#7FDBFF"}

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

SVI_data = get_SVI_data()
CT_data = get_CT_data()

col_list = list(SVI_data)
# print(col_list)
# print(CT_data.columns)
tracts = CT_data["TRACTCE"].values
initial_tract = random.choice(tracts)
intitial_geo_tract = CT_data.loc[CT_data["TRACTCE"] == initial_tract]
# print(tracts)
# print(initial_tract)

def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }

app.layout = dbc.Container([
    header,
    dbc.Row(dcc.Graph(id='ct-map', figure=blank_fig(500))),
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                id="map-category",
                options=[
                    {"label": i, "value": i}
                    for i in ["SVI", "Facilities"]
                ],
                value="SVI",
                inline=True
            ),
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id="tracts",
                options=[
                    {"label": i, "value": i}
                    for i in tracts
                ],
                # value="SVI",
            ),
            dcc.Dropdown(id='graph-type')
        ], width=2)
    ])
])

@app.callback(
        Output('graph-type', 'options'),
        Input('map-category', 'value'))
def category_options(selected_value):
    # print(col_list)
    if selected_value == "SVI":
        variables = [{'label': i, 'value': i} for i in col_list]

        return variables 

@app.callback(
    Output("ct-map", "figure"),
    Input("map-category", "value"),
    Input("graph-type", "value"),
    Input("tract", "value")
)
def update_Choropleth(category, gtype, tracts):
    # print(category)
    df = SVI_data

    gdf_2020 = CT_data
    # print(gtype)
    if gtype is None:
        fig = get_figure(
            df,
            gdf_2020,
            gtype,
            category,
        )
        return fig
    

    elif gtype:
        df = df
        # print(df)
    # else:
        # df = df
        # df['FIPS'] = df['FIPS'].astype(str)
        # df = gdf_2020.merge(df, on="FIPS")
        
        # print(df)

    # elif gtype == "Density":
    #     df_
        changed_id = ctx.triggered_id
        print(changed_id)
        geo_tracts = dict()

        print(CT_data)

        # for k in CT_data["TRACTCE"].keys():
        # if k != "features":
        #     geo_tracts[k] = CT_data["TRACTCE"][k]
        # else:
        #     geo_tracts[k] = [
        #         CT_data["TRACTCE"][tract]
        #         for tract in tracts
        #             # if tract in CT_data["TRACTCE"]
        #         ]
        
        # print(changed_id)


    
    
    
        fig = get_figure(
            df,
            gdf_2020,
            gtype,
            category,
        )




        return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)