from calendar import month
from datetime import date, timedelta
from turtle import ondrag
import urllib.request

tday = date.today()
oneday = timedelta(days=1)
sday = tday - timedelta(weeks=12)

cday = sday

house_urlpt1 = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/transaction_report_for_"
house_urlpt3 = ".json"

sen_urlpt1 = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/data/transaction_report_for_"
sen_urlpt3 = ".json"

while not (cday > tday):
    cday_str = "{:02d}".format(cday.month) + "_" + "{:02d}".format(cday.day) + "_" + "{:04d}".format(cday.year)
    
    try:
        with urllib.request.urlopen(house_urlpt1 + cday_str + house_urlpt3) as resp:
            house_transaction_resp = resp.read().decode()
    except:
        print("The house transaction reports for the day of " + cday_str + " could not be found.")
    else:
        f = open("reports/house_" + cday_str + ".json", "w")
        f.write(house_transaction_resp)

    try:
        with urllib.request.urlopen(sen_urlpt1 + cday_str + sen_urlpt3) as resp:
            sen_transaction_resp = resp.read().decode()
    except:
        print("The senate transaction reports for the day of " + cday_str + " could not be found")
    else:
        f = open("reports/sen_" + cday_str + ".json", "w")
        f.write(sen_transaction_resp)
    finally:
        cday += oneday


