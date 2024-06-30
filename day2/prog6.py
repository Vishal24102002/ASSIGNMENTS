import pandas as pd
import requests

def write_csv():
    dic={
        "latitude":latitude,
        "longitude":longitude,
        "timestamp":timestamp
    }
    df=pd.DataFrame(dic)
    df.to_csv("ISS Location.csv")

longitude=[]
latitude=[]
timestamp=[]

for i in range(0,100):
    req=requests.get("http://api.open-notify.org/iss-now.json")
    if req.status_code==200:
        data=req.json()
        latitude.append(data['iss_position']['latitude'])
        longitude.append(data['iss_position']['longitude'])
        timestamp.append(data['timestamp'])
    else:
        i=i-1
        continue
write_csv()