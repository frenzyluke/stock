

import requests
import json
import csv



url_twse ='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170501&stockNo=2330&'
res = requests.get(url_twse)
s = json.loads(res.text)

for data in (s['data']):
    print (data)

outputfile = open(r'D:\stock\output.csv','w', newline='')
outputwriter = csv.writer(outputfile)
outputwriter.writerow(s['title'])
outputwriter.writerow(s['fields'])
for data in (s['data']):
    outputwriter.writerow(data)

outputfile.close()





