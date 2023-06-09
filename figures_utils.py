import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd
from config import config as cfg

Arap_outline = gpd.read_file('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/us-county-boundaries')


def get_Choropleth(df, gdf_2020, arg, marker_opacity, marker_line_width, marker_line_color, fig=None):


    if fig is None:
        fig = go.Figure()

        # print(df.columns)

    df['FIPS'] = df['FIPS'].astype(str)
    df = gdf_2020.merge(df, on="FIPS")
    # print(df)
    # df['FIPS'] = df['FIPS'].astype(str)

    # gdf_2020 = gpd.read_file('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/Data/2020_CT')
    # print(gdf_2020)
    # geo_data = gdf_2020.merge(df, on='FIPS')
    # geo_data = geo_data.set_index('FIPS')
    # print(list(geo_data.columns))
    # print(arg)

    fig.add_trace(
        go.Choroplethmapbox(
            # geojson = eval(geo_data['geometry_x'].to_json()),
            geojson = eval(df['geometry'].to_json()),
            # geojson = geo_data,
            # locations = geo_data.index,
            locations = df.index,
            # featureidkey = "properties.name",
            # colorscale = arg['colorscale'],
            colorscale = "earth",
            # z = arg['z_vec'],
            # z = geo_data['E_TOTPOP'],
            z = arg["z_vec"],
            # zmin = arg['min_value'],
            # zmax = arg['max_value'],
            # text = arg['text_vec'],
            # hoverinfo="text",
            marker_opacity = marker_opacity,
            marker_line_width = marker_line_width,
            marker_line_color = marker_line_color,
            # # colorbar_title = arg['title'],
        )
    )
    return fig

# def get_outline_map():




def get_figure(df, gdf_2020, gtype, category):

    arg = dict()
    if gtype is None:
        fig = go.Figure(
            go.Scattermapbox()
        )
        # fig = get_Choropleth(df, gdf_2020, arg, gtype)
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

    elif gtype:
        if category == "SVI":
            # print(category)
            arg["z_vec"] = df[gtype]
            # print(arg)


        fig = get_Choropleth(df, gdf_2020, arg, marker_opacity=0.4,
                             marker_line_width=1, marker_line_color='#6666cc')
        

        # layer = [
        #     {
        #         "source": Arap_outline["geometry"].__geo_interface__,
        #         "type": "line",
        #         "color": "black"
        #     }
        # ]

        fig.update_layout(mapbox_style="carto-positron", 
                            mapbox_zoom=10.4,
                            # mapbox_layers=layer,
                            mapbox_center={"lat": 39.65, "lon": -104.8},
                            margin={"r":0,"t":0,"l":0,"b":0},
                            uirevision='constant')
        
        return fig