import requests

data=requests.get("http://api.open-notify.org/iss-now.json")

if data.status_code==200:
    print("connected successfully")
    print(data.json())
else:
    print("error has occured")