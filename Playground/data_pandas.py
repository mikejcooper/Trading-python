import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def play():
    # stocks = ["AAPL","YHOO"]
    stocks = ["AAPL","YHOO","GE","TSLA","GM","BCS"]
    dataFrames = get_data(stocks)
    df = get_frame(stocks,dataFrames,'Adj Close', "2012-02-26", "2013-03-29")
    filter_missing_values(df)
    try:
        df = normalise_data(df)
    except StandardError:
        print "ERROR: Possible date range out of bounds"
        exit();

    # daily_returns = get_daily_returns(df)
    # print get_correlation_matrix(df)
    #
    # plot_scatter(daily_returns,stocks)
    # # plot_data(daily_returns,"Daily Returns")
    #
    # plt.show()






def get_correlation_matrix(daily_returns):
    return daily_returns.corr(method='pearson')

# Plots comparison of two daily returns
def plot_scatter(df_daily_returns, stocks):
    df_daily_returns.plot(kind='scatter', x=stocks[0],y=stocks[1])
    # Slope using beta(m) and alpha(c) values (y=mx+c)
    beta_stock1,alpha_stock1 = np.polyfit(df_daily_returns[stocks[0]],df_daily_returns[stocks[1]],1)
    plt.plot(df_daily_returns[stocks[0]],beta_stock1*df_daily_returns[stocks[0]] + alpha_stock1, '-', color='r')

# Used to display a single stock's daily returns
def plot_histogram(df_daily_returns):
    plt.axvline(df_daily_returns.mean(),color='r',linestyle='dashed',linewidth=2)
    plt.axvline(df_daily_returns.mean() + df_daily_returns.std(),color='g',linestyle='dashed',linewidth=2)
    plt.axvline(df_daily_returns.mean() - df_daily_returns.std(),color='g',linestyle='dashed',linewidth=2)
    df_daily_returns.hist(bins=20)

# Overlays two histograms
def compare_two_hisograms(df_daily_returns,stocks):
    df_daily_returns[stocks[0]].hist(bins=20,label=stocks[0])
    df_daily_returns[stocks[1]].hist(bins=20,label=stocks[1])

# Calculate cumulative returns by price[x]/price[0] - 1
def get_cumulative_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[0].values) - 1
    daily_returns.ix[0] = 0
    return daily_returns

# Calculate daily returns by price[x]/price[x-1] - 1
def get_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0] = 0
    return daily_returns

# Uses SD and Rolling mean to calculate bands
def get_bollinger_bands(rolling_mean, rolling_std):
    upper_band = rolling_mean+2*rolling_std
    lower_band = rolling_mean-2*rolling_std
    return upper_band,lower_band

# Plots bollinger bands (2sd) above and below
def plot_bollinger_bands(df,stock):
    # set plot
    ax = df[stock].plot()
    # get BB data
    rolling_mean = pd.rolling_mean(df[stock], window = 20)
    rolling_std = pd.rolling_std(df[stock], window = 20)
    upper_bound,lower_bound = get_bollinger_bands(rolling_mean,rolling_std)
    # plot
    upper_bound.plot(label='Upper bound', ax = ax)
    lower_bound.plot(label='Lower bound', ax = ax)
    ax.set_ylabel("Date")
    ax.set_xlabel("Price")
    ax.legend(loc='upper left')

# Plotting function
def plot_data(df, title):
    df.plot(title = title)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(True)

# Normalises data
def normalise_data(df):
    return df/df.ix[0,:]

# Uses forward THEN backwards methods to fill blanks in data
def filter_missing_values(df):
    df.fillna(method="ffill", inplace = "TRUE")
    df.fillna(method="bfill", inplace = "TRUE")

# create dataframe from cvs info with specific sd + ed
def get_frame(stocks, data, column, sd, ed):
    dates = pd.date_range(sd, ed)
    # Create empty Data Frame
    df = pd.DataFrame(index=dates)
    for x in range(0, len(data)):
        dfTemp = get_date_range(data[x], sd, ed)
        dfTemp = get_column(dfTemp, column)
        dfTemp = dfTemp.rename(columns={column : stocks[x]})
        df = df.join(dfTemp)
        df = df.dropna()
    return df

# Gets specific column in dataframe
def get_column(df,column):
    return df[[column]]

# Reduces a dataframe to specific time period
def get_date_range(df,sd,ed):
    dates = pd.date_range(sd, ed)
    df1 = pd.DataFrame(index=dates)
    df1 = df1.join(df)
    df1 = df1.dropna()
    return df1

# returns pandas data frame
def cvs_to_array(name):
    return pd.read_csv("data/" + name + ".csv", index_col = "Date", parse_dates=True, na_values = ['nan'])

# Gets stocks from csv files
def get_data(stocks):
    dataframes = []
    for stock in stocks:
        df = cvs_to_array(stock)
        dataframes.append(df)
    return dataframes










if __name__ == "__main__":
    play()
