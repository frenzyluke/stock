import owldata
import pandas
import csv
# 輸入數據貓頭鷹會員 AppID & 應用程式密鑰
appid = '20201002131221236'
appsecret = 'd986ab40046d11eba3fa000c2932e359'

# 引用函數取得資料
owlapp = owldata.OwlData(appid, appsecret)
# stock_price = owlapp.ssp("2317", "20190801", "20200801")
colist = ['日期', '股票名稱', '開盤價', '最高價', '最低價', '收盤價', '成交量', '買賣超合計', '外資買賣超', '投信買賣超', '自營商買賣超', 'K(9)', 'D(9)', 'RSI(5)',  'RSI(10)', "DIF", "MACD", "DIF-MACD"]
owlapp.ssp("2317", "20190801", "20200801", colist)
