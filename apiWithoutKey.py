#Importing python modules#
import requests as req   #for using request object
import pprintpp as pp    #for formatted display of JSON output

#calling the requests.get() method
response = req.get("https://api.publicapis.org/entries")
#code to check if connection status is okay
if response.status_code >= 400 :
    print("bad connection, error code:"+str(response.status_code ))
else:
    print("good connection")
#get the data back in json format
resp = response.json()
#print the result in formatted JSON
pp.pprint(resp)