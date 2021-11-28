import requests as req
import pandas as pd

response = req.get("https://api.publicapis.org/entries")
resp = response.json()

#declaring an empty dataframe
df = pd.DataFrame()
print(df.empty) #check to see if df is empty

#appending data to the dataframe
for num in resp["entries"]:
    df1 = pd.DataFrame(num,index=[0])
    df = pd.concat([df,df1])

#display option setting for pandas dataframe
pd.set_option('display.max_columns', None)
print(df)