import requests
import json
import pandas as pd

# for i in range(10,22):
# print(i)


def getdata(year):
    limit = 1
    for _ in range(2):
        url = "http://bhs.doh.go.th//accident/search/data.json?year="+year+"&limit="+str(limit)
        # print(url)
        response = requests.get(url)
        if response.status_code == 200:
            cut = str(response.text).replace("<br>"," ").replace("<br />"," ")
            # print(response.text)

            data = json.loads(cut, strict=False)
            # print(data)

            limit = data['meta']['total_records']
            print(limit)
    if response.status_code == 200:
        num = []
        datetime = []
        lat = []
        lng = []
        title = []
        detail = []
        for i in data['data']:
            num.append(i['id'])
            lat.append(i['point'][0])
            lng.append(i['point'][1])
            datetime.append(i['datetime'])
            title.append(i['title'])
            detail.append(i['detail'])
        return [num,datetime,lat,lng,title,detail]
    else:
        return "Error"


def get_val(coll, prov, amp):
    import requests
    url = "https://v2k-dev.vallarismaps.com/core/api/1.0/collections/" + coll + "/items?api_key=ypSMTg6baXQJvgrEegbkunhi410eWHQsW4gwhRp7kc77AYRQMigbdKHfznen28AE&pv_tn="+prov
    # +"&ap_tn="+amp
    for i in amp:
        print(i.text())
        url = url + "&ap_tn="+i.text()
    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"

#Run
# getdata(2020)
