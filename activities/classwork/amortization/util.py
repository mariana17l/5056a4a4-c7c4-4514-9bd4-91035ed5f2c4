import pandas as pd
import matplotlib.pyplot as plt


class Amortization(object):

    def __init__(self, amount, interest, n):
        self.amount = amount
        self.interest = interest
        self.n = n

    @property
    def annuity(self):
        annuity = self.interest * self.amount / (1-(1+self.interest)**(-self.n))
        return annuity

    def get_table(self):

        rows = []
        payment = self.annuity
        loan_value = self.amount
        for i in range(self.n):
            interest_value = loan_value * self.interest
            principal = payment - interest_value
            loan_value = loan_value - principal
            rows.append({
                "Interest ": interest_value,
                "Payment": payment,
                "principal": principal,
                "loan_value": loan_value
            })
        return pd.DataFrame(rows).rename_axis("Period").reset_index()

    def get_plot(self):
        df = self.get_table()
        plot = df.plot.bar(x="period", y=["Principal", "Interest"], stacked = True)
        fig = plot.get_figure()
        plt.show()
        return fig
