import psycopg2
import requests
import json



#public ip address of pizza order database
host_name = "34.132.147.228"
#database details
db_name = "torqatapizzaorders"
db_username = "root"
db_pw = "***HIDDEN***"
table_name = 'orders'
table_field ='order_id,customer_id,type,quantity,price,order_time,state'

#REST api data
headers = {
    "API-Key": "api_token",
    "API-Host": "api_host"
}
api_url = "https://api.torqatapizza.com/orders"
def json_to_value_str(json_input, state):

  # values to be inserted into the orders table
   out_str = "{},{},'{}',{},{},'{}','{}'".format(json_input['order_id'],
                                            json_input['customer_id'],
                                            json_input['type'],
                                            json_input['qty'],
                                            round(json_input['retail_price'], 2),
                                            json_input['order_date'],
                                            state)
   return out_str



def insert(event, context):

    try:
        response = requests.request("GET", api_url, headers=headers)

        request_json_list = json.loads(response.text)

        # create a connect object using psycopg2
        conn = psycopg2.connect(host='/cloudsql/torqatapizzageorge-374705:us-central1:mypizzaorders',
                            database=db_name,
                            user=db_username,
                            password=db_pw)
        conn.autocommit = True

        cursor = conn.cursor()
        # process every incoming requests.
        for request_json in request_json_list:
            #find the state that the customer is in based on the customer_id
            find_statement = 'SELECT state FROM customer WHERE customer_id = {}'.format(request_json['customer_id'])

            cursor.execute(find_statement)
            # the first result should be the correct one
            first_row = cursor.fetchone()
            state_name = first_row[0]

            value = json_to_value_str(request_json,state_name)
            # insert new data into db and making sure that no duplicate orders are taken
            insert_statement = 'INSERT INTO {} ({}) values ({}) ON CONFLICT(order_id) DO NOTHING'.format(table_name, table_field, value)
            cursor.execute(insert_statement)

        conn.close()

    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'success'