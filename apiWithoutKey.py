#Importing python modules#
import requests as req   #for using request object
import pprintpp as pp    #for formatted display of JSON output

#
response = req.get("https://api.publicapis.org/entries")
#code to check if connection status is okay
if response.status_code >= 400 :
    print("bad connection, error code:"+str(response.status_code ))
else:
    print("good connection")

resp = response.json()
pp.pprint(resp)