import pandas as pd
import geopandas as gpd



# def get_ct_pop_data():
#     ct_tot_pop_data = pd.read_csv('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/Data/Colorado_SVI_2020.csv')

#     return ct_tot_pop_data


def get_SVI_data():
    SVI_data = pd.read_csv('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/Data/Colorado_SVI_2020.csv')

    return SVI_data

def get_CT_data():
    gdf_2020 = gpd.read_file('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/Data/2020_CT/ArapahoeCT.shp')
    

    return gdf_2020