import pandas as pd ## import pandas for general file types 
import xlrd

#section 1
print("Section One")
df = pd.read_excel('data/Workbook1.xls') ## read xls file
df
## get tab names in xlsx file
xls = xlrd.open_workbook('data/Workbook1.xls', on_demand=True)
print(xls.sheet_names())
tab1 = pd.read_excel('data/Workbook1.xls', sheet_name='Sheet1')
tab2 = pd.read_excel('data/Workbook1.xls', sheet_name='Sheet2')
print(tab1)
print(tab2)
print("\n\n\n")

# Section 2
#-----------

#Is this all?
import requests 
import json
print("Section Two")
data = requests.get('https://data.cms.gov/data-api/v1/dataset/b35c77ac-26e2-4320-91e1-ba71c4d7ff2c/data')
apiDataset = data.json() 
print(apiDataset)
print("\n\n\n")

#section 3
#from google.cloud import bigquery ## import bigquery for bigquery files
### BIGQUERY
print("Section Three")
## first need to load api key that you created based on readme instructions
# connect to bigquery, be sure to update the name of your file, this is currently mine
#client = bigquery.Client.from_service_account_json('Users/amyliu/documents/HHA-507/amy-507-844555269e89.json') ## create bigquery client
## query public dataset
#query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_open_data` LIMIT 100") ## query public dataset
## get results
#results = query_job.result() ## get results
## putresults into dataframe
#df = pd.DataFrame(results.to_dataframe()) ## put results into dataframe