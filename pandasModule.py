import requests as req
import pandas as pd


response = req.get("https://api.publicapis.org/entries")
resp = response.json()
data = resp["entries"]

#reading a list of dictionaries into a dataframe
df = pd.DataFrame.from_dict(data)
#display option setting for pandas dataframe
pd.set_option('display.max_columns', None)
print(df)