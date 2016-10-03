import numpy as np

import data_pandas as d_util

def play():
    stocks = ["AAPL","YHOO"]
    allocations = [0.4,0.6]
    capital = 1000
    dpv = daily_portfolio_value(stocks,allocations,"2010-02-26", "2010-03-25",capital)
    print sharpe_ratio_daily(dpv,capital,0)


# Returns 1d array containing per day portfolio value
def daily_portfolio_value(stocks,allocations,sd,ed,capital):
    # Get data prices
    data = d_util.get_data(stocks)
    df = d_util.get_frame(stocks,data,'Adj Close',sd,ed)
    # Normalise data about 1
    df_norm = df/df.ix[0,:]
    # Allocations per stock per day
    df_alloced = df_norm*allocations
    # Position values - Cash allocated to each asset
    df_pos_vals = df_alloced*capital
    # Sum of stock values in portfolio per day
    df_port_val = df_pos_vals.sum(axis = 1)
    return df_port_val


# Note, that to make the numbers make 'sense' use the to_percentage function

def daily_returns(portfolio_values, capital):
    portfolio_values[1:] =  portfolio_values[1:].values - portfolio_values[0:-1]
    portfolio_values.ix[0] = portfolio_values[0] - capital
    return portfolio_values

def cumulative_returns(portfolio_values):
    return portfolio_values.cumsum()

def average_daily_returns(portfolio_values):
    return portfolio_values.sum(axis=0)/portfolio_values.shape[0]

# Standard deviation of daily return
def std_daily_return(portfolio_values):
    return portfolio_values.values.std()

def to_percentage(portfolio_values,capital):
    return (portfolio_values/capital)*100

# Risk-adjusted return - Time difference matter ( daily (1/252), weekly (1/52), monthly (1/12) )
def sharpe_ratio_daily(portfolio_values,capital,RFR):
    # Convert annual Risk Free Rate to daily.
    RFRDaily = np.power(RFR+1,1/252)
    # mean(daily returns - daily RFR) - mean portfolio return
    a = (daily_returns(portfolio_values,capital) - RFRDaily).mean()
    # std(daily returns - daily RFR) -
    b = std_daily_return(portfolio_values)
    return a/b





if __name__ == "__main__":
    play()


