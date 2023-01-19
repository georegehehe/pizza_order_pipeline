# Torqata Pizza Order Cloud-based Data Pipeline

This repo contains the source codes for a GCP implementation of an end-to-end data pipeline.
The pipeline channels new pizza order information from a RESTful endpoint into a database; The data are then aggregated into statistics such as 
gross sales and gross sales per capita. The final result is a exportable BigQuery View containing the top 3 types of best-selling pizza in each state
over the last 12 months.

# Requirements
This project is impleneted in Python 3.10. Libraries include:
* psycopg2
* pandas
* requests
* NumPy

# Data Flow Chart
![alt text](./Project%20DataFlow.jpeg?raw=true)

# KFiles
* RequestHandler.py
  * Cloud Function implementation that respond to Pub/Sub trigger; fetch current order json payloads from RESTful endpoint and parse them into Cloud SQL
* requesthandler2.py
  * The testable version of the code above: A cloud Function implementation that can be triggered by http request for testing purposes.
* RequestSender.py
  * Script to send mock order request to Cloud Function (via HTTP) for testing purposes.
* generate_state_table.py
  * Convert raw data on U.S. Population into a csv file with popuation by state; output can be directly imported onto Cloud SQL
* generatecustomertable.py
  * Generate csv file that contains 1000 mock customer information; output can be directly imported onto Cloud SQL
* creat_table.sql
  * Initializing/defining tables for Cloud SQL Database
* intermediate_query.sql
  * BigQuery script that aggregate Cloud SQL data into a table that summarizes sales statistics per state per pizza type over the last 12 months.
* final_query.sql
  * BigQuery script that reports the top-3-selling pizza per state by taking in result from the query above.
* top3_pizza_category_by_state_12mon(sample%20export).xlsx
  * Output from the last query in excel format; final output of the pipeline.

# Details
https://docs.google.com/presentation/d/14K5Qrx6yC8P1fk90yq8BL9cyEouXPwVU6a_s1MB_Okk/edit?usp=sharing
