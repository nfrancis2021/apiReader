import requests as req
import pandas as pd
import pyodbc as pcon
import time

response = req.get("https://api.publicapis.org/entries")
resp = response.json()

#declaring an empty dataframe
df = pd.DataFrame()

#appending data to the dataframe
for num in resp["entries"]:
    df1 = pd.DataFrame(num,index=[0])
    df = pd.concat([df,df1])

#record start time
start = time.time()
#inserting data into database with SQL authentication
server = '<Server Name>'
database = '<Database Name>'
username = '<SQL Account Username>'
password = '<Password>'
cnxn = pcon.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
for index, row in df.iterrows():
    cursor.execute("INSERT INTO dbo.APIEntries (API, Description, Auth, HTTPS, Cors, Link, Category) values(?,?,?,?,?,?,?)"
                   , row.API, row.Description, row.Auth, row.HTTPS, row.Cors, row.Link, row.Category)
cnxn.commit()
cursor.close()

#record end time
end = time.time()
print("Time of Execution:", end - start)

#connecting to database with Windows authentication
# server = '<Server Name>'
# database = '<Database Name>'
# cnxn = pcon.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)