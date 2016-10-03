class strategy:

    def analyse(self, stock_history, latest_data):
        previous_day = stock_history.ix[-1]
        current_day = latest_data
        # print current_day

        if (current_day >= self.previous_n_days_avg(stock_history,5)).bool():
            self.exit_short()
            self.long()
        elif (current_day <= self.previous_n_days_avg(stock_history,5)).bool():
            self.exit_long()
            self.short()

        # if (current_day <= self.previous_n_days_avg(stock_history,5)).bool():
        #     self.short()
        # elif (current_day >= self.previous_n_days_avg(stock_history,5)).bool():
        #     self.exit_short()

    def previous_n_days_avg(self,data, n_days):
        if (n_days >= data.shape[0]):
            n_days = data.shape[0]

        return data.tail(n_days).mean(axis=0)


    # Default backtesting

    def long(self):
        self.broker.long(self.stock)

    def exit_long(self):
        self.broker.exit_long(self.stock)

    def short(self):
        self.broker.short(self.stock)

    def exit_short(self):
        self.broker.exit_short(self.stock)

    def __call__(self, stock_history, latest_data, stock, broker):
        self.stock = stock
        self.broker = broker
        self.analyse(stock_history,latest_data)
