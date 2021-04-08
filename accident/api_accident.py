import requests
import pandas as pd
import json,os

os.chdir(os.path.dirname(__file__))
path = os.getcwd()
def api_accident(provid,ampid,years):
    response = requests.request("POST", "http://www.thairsc.com/services/GetAmphurTopThreeList?provid="+provid+"&ampid="+ampid+"&years="+years)

    print(response.text)

def provide():
    with open(path + "/provid.json") as f:
        data = json.load(f)
    # print(data)
    full = []
    dots = []
    for i in data:
        # full.append()
        full.append(i['CHANGWATNAME'])
        dots.append(i['CHANGWATSHORTNAME'])
    df = pd.DataFrame({"provname":full,"provid":dots})
    # print(df)
    return df
# aa = provide()
# print(aa)
# api_accident(provid="กท",ampid="15",years="2012")


