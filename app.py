from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go

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
            # dcc.RadioItems(
            #     id="graph-type",
            #     options=[
            #         {"label": i, "value": i}
            #         for i in ["Pop", "Density"]
            #     ],
            #     # value="Pop",
            #     inline=True
            # ),
            dcc.Dropdown(['Pop', 'Density'], id = 'graph-type')
        ], width=2)
    ])
])

@app.callback(
    Output("ct-map", "figure"),
    Input("graph-type", "value")
)
def update_Choropleth(gtype):

    df = SVI_data

    gdf_2020 = CT_data
    print(gtype)
    if gtype is None:
        fig = get_figure(
            df,
            gdf_2020,
            gtype
        )
        return fig
    

    elif gtype in ["Pop", "Density"]:
        df = df
    # else:
    #     df = df
        # df['FIPS'] = df['FIPS'].astype(str)
        # df = gdf_2020.merge(df, on="FIPS")
        
        # print(df)

    # elif gtype == "Density":
    #     df_



    
    
    
        fig = get_figure(
            df,
            gdf_2020,
            gtype
        )




    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)