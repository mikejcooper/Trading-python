import pandas as pd



class historic_data_csv:

    def __main__(self, stocks_a, sd, ed):
        stocks = stocks_a
        dataFrames = self.get_data(stocks)
        df = self.get_frame(stocks, dataFrames, 'Adj Close', sd, ed)
        self.get_date_range(dataFrames,sd,ed)
        self.filter_missing_values(df)
        try:
            df = self.normalise_data(df)
        except StandardError:
            print "ERROR: Possible date range out of bounds"
            exit();
        return df


    def filter_data_frames(self, data_frame):
        self.filter_missing_values(data_frame)
        try:
            df = self.normalise_data(data_frame)
        except StandardError:
            print "ERROR: Possible date range out of bounds"
            exit();
        return data_frame

    # Normalises data
    def normalise_data(self, df):
        return df / df.ix[0, :]

    # Uses forward THEN backwards methods to fill blanks in data
    def filter_missing_values(self, df):
        df.fillna(method="ffill", inplace="TRUE")
        df.fillna(method="bfill", inplace="TRUE")

    # create dataframe from cvs info with specific sd + ed
    def get_frame(self, stocks, data, column, sd, ed):
        dates = pd.date_range(sd, ed)
        # Create empty Data Frame
        df = pd.DataFrame(index=dates)
        for x in range(0, len(data)):
            dfTemp = self.get_date_range(data[x], sd, ed)
            dfTemp = self.get_column(dfTemp, column)
            dfTemp = dfTemp.rename(columns={column: stocks[x]})
            df = df.join(dfTemp)
            df = df.dropna()
        return df

    # Gets specific column in dataframe
    def get_column(self, df, column):
        return df[[column]]

    # Reduces a dataframe to specific time period
    def get_date_range(self, df, sd, ed):
        dates = pd.date_range(sd, ed)
        df1 = pd.DataFrame(index=dates)
        df1 = df1.join(df)
        df1 = df1.dropna()
        return df1

    # returns pandas data frame
    def cvs_to_array(self, name):
        return pd.read_csv("data/" + name + ".csv", index_col="Date", parse_dates=True, na_values=['nan'])

    # Gets stocks from csv files
    def get_data(self, stocks):
        dataframes = []
        for stock in stocks:
            df = self.cvs_to_array(stock)
            dataframes.append(df)
        return dataframes

