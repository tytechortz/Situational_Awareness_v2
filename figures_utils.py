import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd
from config import config as cfg

Arap_outline = gpd.read_file('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/us-county-boundaries')


def get_Choropleth(df, fig=None):

    if fig is None:
        fig = go.Figure()

    df['FIPS'] = df['FIPS'].astype(str)

    gdf_2020 = gpd.read_file('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/Data/2020_CT')
    print(gdf_2020)
    geo_data = gdf_2020.merge(df, on='FIPS')
    geo_data = geo_data.set_index('FIPS')
    print(geo_data)

    fig.add_trace(
        go.Choroplethmapbox(
            geojson = eval(geo_data['geometry'].to_json()),
            locations = geo_data.index,
            # featureidkey = "properties.name",
            # colorscale = arg['colorscale'],
            colorscale = "earth",
            # z = arg['z_vec'],
            z = geo_data['E_TOTPOP'],
            # zmin = arg['min_value'],
            # zmax = arg['max_value'],
            # text = arg['text_vec'],
            # hoverinfo="text",
            # marker_opacity = marker_opacity,
            # marker_line_width = marker_line_width,
            # marker_line_color = marker_line_color,
            # # colorbar_title = arg['title'],
        )
    )
    return fig



def get_figure(df):

    fig = get_Choropleth(df)
    

    layer = [
        {
            "source": Arap_outline["geometry"].__geo_interface__,
            "type": "line",
            "color": "black"
        }
    ]

    fig.update_layout(mapbox_style="carto-positron", 
                        mapbox_zoom=10.4,
                        mapbox_layers=layer,
                        mapbox_center={"lat": 39.65, "lon": -104.8},
                        margin={"r":0,"t":0,"l":0,"b":0},
                        uirevision='constant')
    
    return fig