import requests as req
import pandas as pd

#calling request.get()
response = req.get("https://api.publicapis.org/entries")
#get the data back in json format
resp = response.json()
#assigining a list of dicts into a variable
data = resp["entries"]

#reading a list of dictionaries into a dataframe
df = pd.DataFrame.from_dict(data)
#display option setting for pandas dataframe
pd.set_option('display.max_columns', None)
print(df)