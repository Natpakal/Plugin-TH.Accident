import requests
import json
import pandas as pd

with open("provid.json") as f:
    data = json.load(f)
json_amp = {}
# print(data)
n = 0
amp = []
ampid = []
prov = []
provid = []

for i in data:
    # json_amp[i['CHANGWATSHORTNAME']] = []

    headers = {
    'Cookie': 'ASP.NET_SessionId=oov5ql4gsnzzzb2us1qzrltk; Language=th; _cbclose=1; _cbclose33476=1; verify=test; _ga=GA1.2.1801234116.1614745958; _gid=GA1.2.704903125.1614745958; _uid33476=D1A5AC52.5; visit_time=2954; ASP.NET_SessionId=42xumvhbn5qgkg3ib1gzyii4; Language=th',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.thairsc.com',
    'Origin': 'http://www.thairsc.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", "http://www.thairsc.com/Home/GetJsonAmphurId?provid="+ i['CHANGWATSHORTNAME'], headers=headers)

    data2 = response.json()
    for i2 in data2['AM']:
        
        if i2['AMPHURNAME'] != '' :
            prov.append(i['CHANGWATNAME'])
            provid.append(i2['CHANGWATSHORTNAME'])
            amp.append(i2['AMPHURNAME'])
            ampid.append(i2['AMPHURID'])
        
df = pd.DataFrame({'prov':prov,'provid':provid,'amp':amp,'ampid':ampid})
print(df)
# df.to_csv("prov_amp.csv", encoding="utf-8")
