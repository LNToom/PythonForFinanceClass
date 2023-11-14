import random

import math

import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns


class Stock:
    def __init__(self, name, price, dividend):
        self.name = name
        self.price = price
        self.dividend = dividend

    def yield_dividend(self):
        return self.dividend / self.price


apple_stock = Stock('Apple', 150, 0.82)
amazon_stock = Stock('Amazon', 1000, 4.65)
print('Apple yield is', apple_stock.yield_dividend())
print('Amazon yield is', amazon_stock.yield_dividend())


class Portfolio:
    def __init__(self):
        self.instruments = {}

    def add_instrument(self, name, price):
        self.instruments[name] = price

    def total_value(self):
        total = 0
        for price in self.instruments.values():
            total += price
        return total


my_portfolio = Portfolio()

my_portfolio.add_instrument('Apple', 150)
my_portfolio.add_instrument('Meta', 450)
my_portfolio.add_instrument('Nvidia', 250)

total_value = my_portfolio.total_value()
print(f"Total Portfolio Value: ${total_value}")


class CurrencyConverter:
    def __init__(self):
        self.rates = {}

    def add_conversion_rate(self, source_currency, target_currency, rate):
        self.rates[(source_currency, target_currency)] = rate

    def convert(self, amount, source_currency, target_currency):
        if (source_currency, target_currency) in self.rates:
            rate = self.rates[(source_currency, target_currency)]
        else:
            if (target_currency, source_currency) in self.rates:
                rate = 1 / self.rates[(target_currency, source_currency)]
            else:
                return f"Conversion rate not available for {source_currency} to {target_currency}"

        converted_amount = amount * rate
        return converted_amount


converter = CurrencyConverter()

converter.add_conversion_rate("USD", "EUR", 0.90)
converter.add_conversion_rate("EUR", "GBP", 1.20)


usd_amount = 100
eur_amount = converter.convert(usd_amount, "USD", "EUR")
print(f"{usd_amount} USD is equivalent to {eur_amount:.2f} EUR")
eur_amount = 100
gbp_amount = converter.convert(eur_amount, source_currency="EUR", target_currency="GBP")
print(f"{eur_amount} EUR is equivalent to {gbp_amount:.2f} GBP")

eur_amount = 1
gbp_amount = 1


random.seed(0)

mean_return = 0.001
std_deviation = 0.02
daily_return = random.normalvariate(mean_return, std_deviation)

initial_price = 100.0

stock_price = initial_price * (1 + daily_return)

print("Stock price after one day:", stock_price)

sigma1 = 0.1
sigma2 = 0.2
rho12 = 0.5
w1 = 0.6
w2 = 0.4

portfolio_variance = (w1**2 * sigma1**2) + (w2**2 * sigma2**2) + (2 * w1 * w2 * rho12 * sigma1 * sigma2)

print(f"Portfolio Variance: {portfolio_variance:.6f}")

return_A = 0.10
volatility_A = 0.20
return_B = 0.15
volatility_B = 0.30

weights = np.linspace(0, 1, 11)

for w_A in weights:
    w_B = 1-w_A
    portfolio_return = w_A * return_A + w_B * return_B

    portfolio_volatility = math.sqrt((w_A**2 * volatility_A**2) + (w_B**2 * volatility_B**2) + (2 * w_A * w_B * volatility_A * volatility_B))

    print(f"Weight A: {w_A:.2f}, Weight B: {w_B: .2f} ", f"Portfolio Return: {portfolio_return:.2%}", f"Portfolio Volatility: {portfolio_volatility:.2%}")

# Data Visualisation Do Not Work


stock_prices = [100, 102, 104, 103, 105, 107, 108]
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
plt.figure(figsize=(10, 6))
sns.lineplot(stock_prices)
plt.title('Stock Price Over a Week')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()


returns = [0.05, -0.02, 0.03, -0.01, 0.02, 0.03, -0.03, 0.01, 0.04, -0.01]

sns.histplot(returns, bins=5, kde=False)
plt.title('Distribution of Stock Returns')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()

returns = [0.05, -0.02, 0.03, -0.01, 0.02, 0.03, -0.03, 0.01, 0.04, -0.01]

sns.histplot(returns, bins=5, kde=True)
plt.title('Distribution of Stock Returns')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()
