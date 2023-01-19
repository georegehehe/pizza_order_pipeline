# Upload US Population Data onto Google Cloud SQL
import pandas as pd

def df_to_dict(df_in):
    key_lst = df_in['State'].tolist()
    num_lst = df_in['Total'].tolist()
    # every 13th elements corresponds to a state name
    state_keys = [key_lst[i*13] for i in range(len(key_lst) // 13)]
    #every 13th element starting at the 3rd row corresponds to the total adult population
    #each element needs to be changed from string format (with comma) to int
    pop_lst = [int(num_lst[i*13 + 2].replace(',','')) for i in range(len(num_lst) // 13)]
    return {'state': state_keys, 'population':pop_lst}


df = pd.read_excel('us_adultpop_by_state_2021.xlsx')
pd.DataFrame(df_to_dict(df)).to_csv('state.csv',index=False, header=False)