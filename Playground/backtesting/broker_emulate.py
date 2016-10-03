from datetime import datetime

import portfolio_database_emulate as database

import pandas as pd


class broker:

    TIME_POINT = pd.to_datetime('1970/01/01') # info about current time (specifically for backtesting)
    PRICE_POINT = 0 # info about current price (specifically for backtesting)
    # STOCK_POINT = 'NONE'  # info about current stock (specifically for backtesting)

    def update_time_point(self, latest_data):
        time_stamp = latest_data.name
        self.TIME_POINT = time_stamp
        print self.TIME_POINT

    def update_current_price(self, latest_data):
        current_price = latest_data.values[0]
        self.PRICE_POINT = current_price
        print self.PRICE_POINT

    # def update_current_stock(self, stock):
    #     self.STOCK_POINT = stock
    #     print self.STOCK_POINT

    def buy_long(self,stock, lot_size, stop_loss):
        # buy
        price = self.PRICE_POINT
        date = self.TIME_POINT
        # add to portfolio database
        database.portfolio.data_entry_Buy_Long(self,date,stock,price,lot_size,stop_loss)
        return 1

    def buy_short(self,stock, lot_size, stop_loss):
        # buy
        price = self.PRICE_POINT
        date = self.TIME_POINT
        # add to portfolio database
        database.portfolio.data_entry_Buy_Short(self,date,stock,price,lot_size,stop_loss)
        return 1

    def sell_long(self, stock):
        # date_buy, stock, price_buy, lot_size, stop_loss, long_or_short
        buy_transaction = database.portfolio.data_retreval_Current_Positions(self,stock,"LONG")

        date = self.TIME_POINT
        price_sell = self.PRICE_POINT
        lot_size_sell = buy_transaction[3] # Could vary
        price_buy = buy_transaction[2]
        lot_size_buy = buy_transaction[3]
        profit_loss = price_buy*lot_size_buy - price_sell*lot_size_sell

        database.portfolio.data_entry_Sell_Long(self,buy_transaction[0],date,stock,price_buy,price_sell,lot_size_sell,profit_loss)





    #
    # def exit_long(self,stock):
    #
    #
    # def short(self, stock):
    #
    #
    #
    # def exit_short(self, stock):




