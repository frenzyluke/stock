import pandas as pd
import requests

url = "https://api.finmindtrade.com/api/v3/data"
stock_id = "2317"
date = "2019-01-01"
end_date = "2019-12-31"
dataset="TaiwanStockPER"

parameter = {
    "dataset": dataset,
    "stock_id": stock_id,
    "date": date,
    "end_date": end_date,
    "user_id": "dick82101@gmail.com",
    "password": "happydog82101"

}
resp = requests.get(url, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])
data.to_csv('data/' + stock_id + "/" + date[:4]+ "_" + dataset + ".csv")
print(data.head())

dataset="InstitutionalInvestorsBuySell"
parameter = {
    "dataset": "InstitutionalInvestorsBuySell",
    "stock_id": "2317",
    "date": "2020-10-05",
}
data = requests.get(url, params=parameter)
data = data.json()
data = pd.DataFrame(data['data'])
data.to_csv('data/' + stock_id + "/" + date[:4]+ "_" + dataset + ".csv")
print(data.head())