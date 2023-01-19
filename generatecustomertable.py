import pandas as pd
import random

def generate_csv_table(state_lst, length):
    #format of each row: namei, addressi, cityi, [state_name], zipcodei
    name_lst = ['name' + str(i) for i in range(length)]
    address_lst = ['address' + str(i) for i in range(length)]
    city_lst = ['city' + str(i) for i in range(length)]
    state_lst = [random.choice(state_lst) for i in range(length)]
    zip_lst = ['zipcode' + str(i) for i in range(length)]

    out_df = pd.DataFrame({'name':name_lst,
                  'address':address_lst,
                  'city':city_lst,
                  'state':state_lst,
                  'zipcode':zip_lst})
    out_df.to_csv('result.csv',header=False)



df = pd.read_csv('state.csv')
states = df['state'].tolist()
generate_csv_table(states, 1000)