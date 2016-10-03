import threading

import broker_emulate

class backtest:

    def __main__(self, strategy_X, stocks):
        broker = broker_emulate.broker()

        # for stock in stocks:
        stock = stocks.columns.values[0]
        entries_length = stocks.shape[0]
        broker.update_current_stock(stock)
        for x in range(0, entries_length - 1):
            previous_data = stocks[:-entries_length + x + 1]
            latest_data = stocks.ix[x+1]
            broker.update_time_point(latest_data) # set correct time point in broker emulator
            broker.update_current_price(latest_data)
            strategy_X(previous_data,latest_data, stock, broker)



