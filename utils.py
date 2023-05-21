import pandas as pd



def get_ct_pop_data():
    ct_tot_pop_data = pd.read_csv('/Users/jamesswank/Python_Projects/Situational_Awareness_v2/Data/Colorado_SVI_2020.csv')

    return ct_tot_pop_data