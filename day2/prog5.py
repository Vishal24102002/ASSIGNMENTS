import requests

req=requests.get("http://api.open-notify.org/iss-now.json")

if req.status_code==200:
    print("connected successfully")
    data=req.json()
    print("latitude :",data['iss_position']['latitude'])
    print("longitude :",data['iss_position']['longitude'])
    print("timestamp :",data['timestamp'])
