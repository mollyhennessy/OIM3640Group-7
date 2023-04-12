# pip install pandas-datareader
import yfinance as yf

import pandas_datareader as pdr
from time import sleep, time
import sys


def display_menu():
    print("""
    StockTracker Menu
    1. Track watchlist
    2. Add watchlist
    3. Edit watchlist
    4. Delete watchlist
    5. Exit

    """)


def track(watchlist):  # how to prepare for a list or a singular
    start_time = time()
    while True:
        for symbol in watchlist:
            try:
                print(f'{symbol:8}{pdr.get_quote_yahoo(symbol)["price"].values[0]}')
                # print(f"elapsed time: {time()- start_time}")
                sleep(1)
            except:
                print(f"{symbol} not found!")
        print(f'Elapsed time: {time() - start_time}')
        if time() - start_time >= 10:
            prompt = input("To continue press the enter key, q key to quit: ")
            if prompt == 'q':
                break


def add():
    added_symbols = input("Enter the symbols you want to add: ")
    new_symbols = added_symbols.split()
    for symbol in new_symbols:
        watchlist.append(symbol)
    print("You added: ", new_symbols)


def edit():
    pass


def delete():
    pass


# goog=yf.download("GOOG"
# goog=pdr.get_quote_yahoo("GOOG")
# print(goog.info())
# goog=pdr.get_quote_yahoo("GOOG")["price"].values
# print(goog)
options = {"1": track, "2": add, "3": edit, "4": delete}


def main():
    while True:
        display_menu()
        choice = input("enter your selection: ")
        if choice == '1':
            watchlist = "AMZN AAPL GOOG FB".split()
            options[choice](watchlist)
        elif choice in "234":
            options[choice]()
        elif choice == '5':
            print("GoodBye!")
            time.sleep(1)
            sys.exit()
        else:
            print("enter a valid selection")
            # serves as an entry point
    # allows us to separate logic from program flow
    #     symbol="GOOG"
    #     print(f'{symbol:8}{pdr.get_quote_yahoo("GOOG")["price"].values[0]}')


if __name__ == "__main__":
    main()