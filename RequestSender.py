import requests
import time
import random
import numpy
from datetime import datetime
import subprocess

url = 'https://us-central1-torqatapizzageorge-374705.cloudfunctions.net/updatemypizzadb'
num_requests = 1000
start_id = 14
types = ['cheese', 'pepperoni', 'supreme', 'meat lover', 'veggie']
prices = [10.95, 11.99, 14.99, 14.99, 11.99]
# Source: https://medium.com/google-cloud/setup-and-invoke-cloud-functions-using-python-e801a8633096
token = '{}'.format(subprocess.Popen(args="gcloud auth print-identity-token", stdout=subprocess.PIPE, shell=True).communicate()[0])[2:-3]
# source: https://gist.github.com/rg3915/db907d7455a4949dbe69
def get_random_datetime(min_year=2021):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    end = datetime.now()
    result_datetime = start + (end - start) * random.random()
    return result_datetime.strftime("%Y-%m-%d %H:%M:%S+00")

for i in range(num_requests):
    type_chosen = random.randint(0,4)
    order_param = {
        "order_id": start_id+i,
        "customer_id": random.randint(0,999),
        "type": types[type_chosen],
        "qty": int(numpy.random.choice(numpy.arange(1, 6), p=[0.3, 0.35, 0.2, 0.1, 0.05])),
        "retail_price": prices[type_chosen],
        "order_date": get_random_datetime()
    }
    r = requests.post(url,json=order_param,headers={"Authorization":"bearer {}".format(token)})
    print(i)
    print(r.status_code)
    print(r.headers)
    time.sleep(0.5)