from Backtesting  import backtest
from trading_strategies import strategy_A
import get_data


class trade:

    def go(self):

        strategy_X = strategy_A.strategy()
        stock_data = self.get_stock_data()
        print stock_data
        backtestA = backtest.backtest().__main__(strategy_X.__call__, stock_data[['YHOO']])


    def get_stock_data(self):
        stocks = ["AAPL",'YHOO']
        sd = "2012-02-26"
        ed = "2013-03-29"
        data_frames = get_data.historic_data_csv().get_data(stocks)
        data_frames = get_data.historic_data_csv().get_frame(stocks, data_frames,'Adj Close', sd,ed)
        data_frames = get_data.historic_data_csv().filter_data_frames(data_frames)
        return data_frames




if __name__ == "__main__":
    tradeOb = trade()
    tradeOb.go()


