ticker1 = "AAPL"
opening_price1 = 142.7
closing_price1 = 143.2
volume1 = 1200000

ticker2 = "LVMH"
opening_price2 = 1721.2
closing_price2 = 1724.4
volume2 = 1300000

print(ticker1, opening_price1, closing_price1, volume1)
print(ticker2, opening_price2, closing_price2, volume2)

currencypair = "EUR/USD"
buyingrate = 1.1825
sellingrate = 1.1830

print(currencypair, buyingrate, sellingrate)

stocks1 = ["AAPL", "MSFT", "GOOGL"]
stocks1.append("IBM")
print(stocks1)

stocks2 = ["TSLA", "AMZN", "FB", ]
stocks2.extend(["AMD", "NVDA"])
print(stocks2)

stock_details = {
    "Ticker": "AAPL",
    "Opening Price": 142.7,
    "Closing Price": 143.2,
    "Volume": 1200000
}
print(stock_details)

bond_details = {
    "Issuer": "FED",
    "Maturity Date": 2030,
    "Coupon Rate": "5%",
    "Face Value": 1000
}
print(bond_details)

stock_prices = [105, 107, 104, 106, 103]

daily_returns = [(stock_prices[i] - stock_prices[i - 1]) / stock_prices[i - 1] for i in range(1, len(stock_prices))]

for daily_return in daily_returns:
    print("Daily Return:", daily_return)

average_return = sum(daily_returns) / len(daily_returns)
print("Average Return:", average_return)

principal = 1000
rate = 0.05
years = 0

while principal < 2000:
    principal *= (1 + rate)
    years += 1

print("It takes", years, "years for the principal to reach $2000.")

principal = 500
rate = 0.07
years = 0

while principal < 1000:
    principal *= (1 + rate)
    years += 1

print("It takes", years, "years for the principal to reach $1000.")
