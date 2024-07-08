#python
import pandas as pd
import requests
import datetime
from datetime import timedelta

header={
    "Accept": "*/*",
    "Cookie": "_ga=GA1.1.1282503254.1719805213; __gads=ID=45d630d2b943f9bc:T=1719805228:RT=1719902479:S=ALNI_MaAD2o9JWQaFDb0QneBoeoy5hkdbw; __eoi=ID=842058df14249fc4:T=1719805228:RT=1719902479:S=AA-AfjZxz1ZQIgdLTckaaP6NkyyH; JSESSIONID=20F3E325699A599D181B00E47EBF06D0; _ga_2RYZG7Y4NC=GS1.1.1719902475.3.1.1719902531.0.0.0; FCNEC=%5B%5B%22AKsRol8Nw6bvFpLTs5vwj6KbtY_IW5MFPuc3-sGvLJEFDQWTVR5IfW1IOqPY3-Wc1dKIuY19UyEZbJYiQSLUihPmkzJjtjanQ6tueJDGNdhmISSQ8uiSufgXWRY7bilOLym79Qk-Lr3p4-WvGpL2qUK2ZbSZ-rrDyQ%3D%3D%22%5D%5D",
    "Host": "vegetablemarketprice.com",
    "Referer": "https://vegetablemarketprice.com/market/haryana/today",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


start_date=datetime.datetime(2024,5,1)
end_date=datetime.datetime(2024,5,30)
arr = []
while start_date <= end_date:
    start_date_w = start_date.strftime("%Y-%m-%d")
    print(start_date_w)
    url="https://vegetablemarketprice.com/api/dataapi/market/haryana/daywisedata?date="+str(start_date_w)+""

    data=requests.get(url,header)

    data=data.json()

    for api in data["data"]:
        """name.append(api["vegetablename"])
        wholesale.append(api['price'])
        retail.append(api['retailprice'])
        mall.append(api["shopingmallprice"])"""


        dic2={
            "date":start_date,
            "name":str(api["vegetablename"]),
            "wholesale":str(api["price"]),
            "retail":str(api["retailprice"]),
            "mall":str(api["shopingmallprice"])
        }
        arr.append(dic2)
    start_date = start_date + timedelta(days=1)
        #print(start_date)
#print(dic2)
df=pd.DataFrame(arr)
df.to_csv("out.csv")
# print(df)