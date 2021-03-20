README
-------------
Author/Developer: Mehdi GHAOUTI / Eliptix
contact: ghaouti.mehdi@gmail.com

What Is This?
-------------

This is a very simple package that retrieves LIVE stocks data from Yahoo finance, such as price, previous close, evolution, open, volume and average volume.
Those features are really intended in the creation of a trading bot/algorithm and to back-test strategies for quants.

Installation
-------------

1. Run `pip install LSDyf` to install dependencies
2. Make sure packages requests and bs4 are installed

How to use it
-------------

1. from LSDyf import *
2. Use as follow:
ticker = "GE"    #For general electic in this example. A full list with all yahoo finance tickers is provided
num = "0"        # If num is 0 then you'll have the results displayed with extra info like a text that specifies the output. If num is 1 , you'll get the raw data without any extra info, usually if calculation is engaged.

myPrice = get_price(ticker,num)
print(myPrice)
# Output >>>  Price : 13.22
# Note that the output would have been >>> 13.22    if num was = 1

Functions list to be used such as above:
    get_price(ticker,num)
    get_evol(ticker, num)
    get_close(ticker, num)
    get_open(ticker, num)
    get_volume(ticker, num)
    get_avg_volume(ticker, num)
    get_beta(ticker, num) 


Development
-----------

If you want to work on this package and add more features , you can either contact me or dive into the methods used and add your very own stuff !

