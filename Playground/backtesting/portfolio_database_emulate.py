import sqlite3

class portfolio:


    conn = sqlite3.connect('info.db')
    c = conn.cursor()

    def create_tabel(self):
        # Table Buy Long
        # Date Buy, Stock, Price, Lot size, Stop Loss, Target Price
        self.c.execute('CREATE TABLE IF NOT EXISTS BuyLong(date_buy TEXT, stock TEXT, price_buy REAL, lot_size REAL, stop_loss REAL')

        # Table Buy Short
        # Date Buy, Stock, Price, Lot size, Stop Loss, Target Price
        self.c.execute('CREATE TABLE IF NOT EXISTS BuyShort(date_buy TEXT, stock TEXT, price_buy REAL, lot_size REAL, stop_loss REAL)')

        # Table Sell Long
        # Date Buy, Date Sell, Stock, Price Buy, Price Sell, Lot size, P/L
        self.c.execute('CREATE TABLE IF NOT EXISTS SellLong(date_buy TEXT, date_sell TEXT, stock TEXT, price_buy REAL, price_sell REAL, lot_size REAL, profit_loss REAL)')

        # Table Sell Short
        # Date Buy, Date Sell, Stock, Price Buy, Price Sell, Lot size, P/L
        self.c.execute('CREATE TABLE IF NOT EXISTS SellShort(date_buy TEXT, date_sell TEXT, stock TEXT, price_buy REAL, price_sell REAL, lot_size REAL, profit_loss REAL)')

        # Table Current Positions
        # Date Buy, Stock, Price, Lot size, Stop Loss, Target Price, Long or Short
        self.c.execute('CREATE TABLE IF NOT EXISTS CurrentPositions(date_buy TEXT, stock TEXT, price_buy REAL, lot_size REAL, stop_loss REAL, target_price REAL, long_or_short TEXT)')

        # Table Profit/Loss History
        # Date Buy, Date Sell, Stock, Price Buy, Price Sell, Lot size, P/L
        self.c.execute('CREATE TABLE IF NOT EXISTS History(date_buy TEXT, date_sell TEXT, stock TEXT, price_buy REAL, price_sell REAL, lot_size REAL, profit_loss REAL)')


    # INSERT into database

    def data_entry_Buy_Long(self, date_buy, stock, price_buy, lot_size, stop_loss, target_price):
        # self.c.execute('INSERT INTO BuyLong VALUES ("2016-01-01", "EUR/USD", 101, 1, 100.5, 103 )')
        self.c.execute('INSERT INTO BuyLong VALUES (date_buy, stock, price_buy, lot_size, stop_loss)')
        self.conn.commit()

    def data_entry_Buy_Short(self, date_buy, stock, price_buy, lot_size, stop_loss, target_price):
        self.c.execute('INSERT INTO BuyShort VALUES (date_buy, stock, price_buy, lot_size, stop_loss)')
        self.conn.commit()

    def data_entry_Sell_Long(self, date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss):
        self.c.execute('INSERT INTO SellLong VALUES (date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss)')
        # self.data_entry_History(date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss)

        self.conn.commit()

    def data_entry_Sell_Short(self, date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss):
        self.c.execute('INSERT INTO SellShort VALUES (date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss)')
        # self.data_entry_History(date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss)
        self.conn.commit()


    def data_entry_Current_Positions(self, date_buy, stock, price_buy, lot_size, stop_loss, long_or_short):
        self.c.execute('INSERT INTO CurrentPositions VALUES (?, ?, ?, ?, ?, ?)', (date_buy, stock, price_buy, lot_size, stop_loss, long_or_short))
        self.conn.commit()


    def data_entry_History(self, date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss):
        self.c.execute('INSERT INTO History VALUES (date_buy, date_sell, stock, price_buy, price_sell, lot_size, profit_loss)')
        self.conn.commit()

    #     Function that converts closing of a stock to History?




    # SEARCH database

    def data_retreval_Current_Positions(self, this_stock, this_long_or_short):
        # self.c.execute('DELETE FROM CurrentPositions WHERE stock=this_stock')
        self.c.execute("SELECT * FROM CurrentPositions WHERE stock = '%s' AND long_or_short = '%s'" % (this_stock, this_long_or_short))
        # self.conn.commit()
        return self.c.fetchone()

    def data_retreval_Current_Positions(self, this_stock, this_long_or_short, this_date):
        # self.c.execute('DELETE FROM CurrentPositions WHERE stock=this_stock')
        self.c.execute("SELECT * FROM CurrentPositions WHERE stock = '%s' AND long_or_short = '%s'AND date_buy = '%s'" % (this_stock, this_long_or_short, this_date))
        # self.conn.commit()
        return self.c.fetchone()

    # REMOVE from database

    def data_removal_Current_Positions(self, this_stock, this_long_or_short, this_date):
        self.c.execute("DELETE FROM CurrentPositions WHERE stock = '%s' AND long_or_short = '%s' AND date_buy = '%s'" % (this_stock, this_long_or_short, this_date))
        self.conn.commit()
        return 1




    def data_entry(self):
        self.data_entry_Current_Positions('date','YHOO',1,1,1,2,'LONG')
        a= self.data_retreval_Current_Positions('YHOO','LONG')
        self.c.close()
        self.conn.close()



a = portfolio()
a.create_tabel()
a.data_entry()

