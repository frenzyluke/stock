
# coding: utf-8
import requests
import json
import csv
import time, datetime,os
from bs4 import BeautifulSoup as bs
dt = datetime.datetime.now()
# dt.year
# dt.month

id_list = ['2317'] #inout the stock IDs
now = datetime.datetime.now()
year_list = range (2020,now.year+1) #since 2007 to this year
month_list = range(1,13)  # 12 months


# In[15]:


# ###http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170605&stockNo=2330

# In[12]:

#standard web crawing process
def get_webmsg (year, month, stock_id):
    date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
    sid = str(stock_id)
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+sid

    page = ''
    time.sleep(10)
    while page == '':
        try:
            res = requests.post(url_twse)
            page=1
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(10)
            print("Was a nice sleep, now let me continue...")
            continue
    # res =requests.post(url_twse,)
    soup = bs(res.text , 'html.parser')
    smt = json.loads(soup.text)     #convert data into json
    return smt


# In[13]:

def write_csv(stock_id,directory,filename,smt) :
    writefile = directory + filename               #set output file name
    outputFile = open(writefile,'w',encoding='utf-8',newline='')
    outputWriter = csv.writer(outputFile)
    head = ''.join(smt['title'].split())
    a = [head,""]
    outputWriter.writerow(a)
    outputWriter.writerow(smt['fields'])
    for data in (smt['data']):
        outputWriter.writerow(data)

    outputFile.close()


# In[14]:

#create a directory in the current one doesn't exist
def makedirs (year, month, stock_id):
    sid = str(stock_id)
    yy      = str(year)
    mm       = str(month)
    directory = 'D:/stock'+'/'+sid +'/'+ yy
    if not os.path.isdir(directory):
        os.makedirs (directory)  # os.makedirs able to create multi folders


for stock_id in id_list:
    for year in year_list:
        for month in month_list:
            if (dt.year == year and month > dt.month): break  # break loop while month over current month
            sid = str(stock_id)
            yy = str(year)
            mm = month
            directory = 'D:/stock' + '/' + sid + '/' + yy + '/'  # setting directory
            filename = str(yy) + str("%02d" % mm) + '.csv'  # setting file name
            smt = get_webmsg(year, month, stock_id)  # put the data into smt
            makedirs(year, month, stock_id)  # create directory function
            write_csv(stock_id, directory, filename, smt)  # write files into CSV
            time.sleep(1)


