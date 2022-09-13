global live_stock_price
global user_stock
global y

def Scraper(stock):
    '''get_ipython().system('pip install requests')
    get_ipython().system('pip install bs4') 
    get_ipython().system('pip install html5lib') '''

    # Importing the Libraries
    import requests
    from bs4 import BeautifulSoup
    
    #stock=input("Enter the Name of The Stock")
    url = 'https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/'+stock+'/'
    # print(url)
    response = requests.get(url)
    # print(response)

    # Obtaining the soup
    global day_high, day_low, Strengths, Weakness, Opportunities, Threats
    soup = BeautifulSoup(response.text, 'html.parser')
    x = int(input("1.BSE \n2.NSE\nEnter your choice:\n"))

    # Obtaining the Data based on User Requirements
    if(x == 1):
        data_array_bse = soup.find(id="bsecp").getText().strip()
        # print(data_array_bse)
        data_array = data_array_bse
    if(x == 2):
        data_array_nse = soup.find(id="nsecp").getText().strip()
        # print(data_array_nse)
        data_array = data_array_nse

    # Splitting the Array and entering the data in to the list
    list1 = list(data_array.split(" "))
    # print(list1[0])

    # Lowest Price of The Day
    day_low = soup.find(id="sp_low").getText().strip()

    # Highest Price of The Day
    day_high = soup.find(id="sp_high").getText().strip()

    # SWOT analysis of the stock
    Strengths = soup.find(id="swot_ls").getText().strip()
    Weakness = soup.find(id="swot_lw").getText().strip()
    Opportunities = soup.find(id="swot_lo").getText().strip()
    Threats = soup.find(id="swot_lt").getText().strip()

    # Converting the strings in the list to Float Datatype

    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    locale_num = locale.atof(list1[0])
    # print(locale_num)

    # Alternative method to convert string to float
    '''float1=[float(item) for item in list1]
    print(float1)'''
    global y
    y = locale_num
    return y


def simulator(live_stock_price, user_purchase_price):
    global profit, profit_percent
    profit = live_stock_price-user_purchase_price
    profit_percent = (profit/user_purchase_price)*100


def user_input():


    user_stock = input("Enter Stock purchased: ")
    Scraper(user_stock)
    print("Live Stock price of ", user_stock, "=  ₹", y)
    live_stock_price = y
    user_purchase_price = float(
    input("Enter the price at which the "+user_stock+" stock was purchased:"))
    simulator(live_stock_price, user_purchase_price)

    print("P/L per share  ₹", profit)
    print("Profit Percent ", profit_percent, "%")
    print("Lowest price today ₹", day_low)
    print("Highest price today ₹", day_high)


    def GRAPH_SWOT(Strengths, Weakness, Opportunities, Threats):

        print(Strengths)

        print(Weakness)

        print(Opportunities)

        print(Threats+'\n')

        import pandas as pd
        import datetime
        import numpy as np
        import matplotlib.pyplot as plt
        from pandas.plotting import scatter_matrix
        import yfinance as yf
        start = "2011-01-01"
        end = '2022-1-01'

        x = yf.download(user_stock+'.NS',start,end)

        x['Open'].plot(label = user_stock,figsize=(15,8))

        x['Open'].plot(label = user_stock)
        plt.legend(loc='right')
    
        plt.title('Stock Prices of '+user_stock)
        plt.show()
    GRAPH_SWOT(Strengths, Weakness, Opportunities, Threats)
    
    
        
        
while True:
    print("**Menu**")
    print("\n1.Stock Analysis")
    print("\n2.Exit")

    choice = int(input("\nEnter your choice:"))
    if choice == 1:
        user_input()
    elif choice == 2:
        break
    else:
        print("Wrong Choice")