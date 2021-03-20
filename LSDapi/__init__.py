import requests
from bs4 import BeautifulSoup


def get_price(ticker,num):
    params = {'p': ticker}
    r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?', params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    r_find = soup.find_all(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].get_text()
    if num == 0:
         return "Price : " + r_find
    elif num == 1:
         return float(r_find.replace(",", ""))

def get_close(ticker,num):
    params = {'p': ticker}
    r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?', params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    r_find = soup.find(attrs={'data-test':'PREV_CLOSE-value'}).get_text()
    if num == 0:
         return "Previous close : " + r_find
    elif num == 1 :
         return float(r_find.replace(",", ""))

def get_evol(ticker,num):
    price = get_price(ticker, 1)
    close = get_close(ticker, 1)
    res = ((price/close)-1)*100
    if num == 0:
        if res > 0:
         return f"Evolution : + {res:.2f} % "
        elif res < 0:
         return f"Evolution : {res:.2f} % "
    elif num == 1:
         return float(res)

def get_open(ticker,num):
    params = {'p': ticker}
    r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?', params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    r_find = soup.find(attrs={'data-test':'OPEN-value'}).get_text()
    if num == 0:
         return "Open : " + r_find
    elif num == 1 :
         return float(r_find.replace(",", ""))

def get_volume(ticker,num):
    params = {'p': ticker}
    r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?', params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    r_find = soup.find(attrs={'data-test':'TD_VOLUME-value'}).get_text()
    if num == 0:
         return "Volume: " + r_find
    elif num == 1 :
         return int(r_find.replace(",", ""))

def get_avg_volume(ticker,num):
    params = {'p': ticker}
    r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?', params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    r_find = soup.find(attrs={'data-test':'AVERAGE_VOLUME_3MONTH-value'}).get_text()
    if num == 0:
         return "Average 3 Months volume : " + r_find
    elif num == 1 :
         return int(r_find.replace(",", ""))

def get_beta(ticker,num):
    params = {'p': ticker}
    r = requests.get('https://finance.yahoo.com/quote/' + ticker + '?', params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    r_find = soup.find(attrs={'data-test':'BETA_5Y-value'}).get_text()
    if num == 0:
         return "Beta 5Y: " + r_find
    elif num == 1 :
         return float(r_find.replace(",", ""))
