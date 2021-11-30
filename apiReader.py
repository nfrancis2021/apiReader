import requests as req
import pandas as pd
from sqlalchemy import create_engine
import time
import sys
import pywin32

#apiendpoint = sys.argv[0]
servername = sys.argv[1]

#calling request.get()
response = req.get("https://api.publicapis.org/entries")
#get the data back in json format
resp = response.json()
#assigining a list of dicts into a variable
data = resp["entries"]

#reading a list of dictionaries into a dataframe
df = pd.DataFrame.from_dict(data)

# #record start time
start = time.time()

# inserting data into database
server = servername
database = '<Databasename>'
driver = 'ODBC Driver 17 for SQL Server'
dbconnection = f'mssql://@{server}/{database}?driver={driver}'
engine = create_engine(dbconnection, fast_executemany=True)
df.to_sql('<Table Name>', engine, schema='<Schema Name>', if_exists='append', index=False)

# #record end time
end = time.time()
print("Time of Execution:", end - start)
