import matplotlib.pyplot as plt


import yfinance as yf


dates = ("1st January", "2nd January", "3rd January")
stock_prices = (150, 152, 151)

for date, price in zip(dates, stock_prices):
    print(f"{date}: ${price}")

dates = ("4th January", "5th January", "6th January")
stock_prices = (155, 156, 153)


def calculate_average(stock_prices):
    return sum(stock_prices)/len(stock_prices)


average_price = calculate_average(stock_prices)


print(f"Average Stock Price: ${average_price}")


def find_day_with_highest_price(dates, prices):
    max_price = max(prices)
    max_price_index = prices.index(max_price)
    return dates[max_price_index]


# Times Value Of Money

def present_value(fv, r, n):
    return fv / (1+r)**n


FV = 120
r = 0.05
n = 2

PV0 = present_value(FV, r, n)
print(f"The Present Value is: ${PV0:.2f}")

FV = 500
r = 0.06
n = 2

PV1 = present_value(FV, r, n)
print(f"The Present Value 1 is: ${PV1:.2f}")

FV = 1000
r = 0.04
n = 5

PV2 = present_value(FV, r, n)
print(f"The Present Value 2 is: ${PV2:.2f}")


def future_value(pv, r, n):
    return pv * (1 + r) ** n


pv = 90
r = 0.07
n = 1

FV = future_value(pv, r, n)
print(f"The Future Value is: ${FV:.2f}")

PV1 = 200
r = 0.03
n = 2

FV1 = future_value(PV1, r, n)
print(f"The Future Value 1 is: ${FV1:.2f}")

PV2 = 150
r = 0.05
n = 3

FV2 = future_value(PV2, r, n)
print(f"The Future Value 2 is: ${FV2:.2f}")

# Discounting and Compounding


def compound(pv, r):
    return pv * (1 + r)


PV = 80
r = 0.09

FV = compound(PV, r)
print(f"After one year with a 9% interest rate, you'll have: ${FV:.2f}")


def discount(fv, r):
    return fv / (1 + r)


FV = 115
r = 0.08

PV = discount(FV, r)
print(f"PV at 8% interest rate, is : ${PV:.2f}")


def discount(fv, r):
    return fv / (1 + r)


FV = 500
r = 0.06

PV = discount(FV, r)
print(f" You need to invest : ${PV:.2f} to get 500$ in 2 years at 6%")


def discount(fv, r):
    return fv / (1 + r)


FV = 180
r = 0.10

PV = discount(FV, r)
print(f" PV is : ${PV:.2f} ")


def discount(fv, r):
    return fv / (1 + r)


FV = 1000
r = 0.07

PV = discount(FV, r)
print(f" We need to invest : ${PV:.2f} ")

# Download Apple stock data
apple_data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")

# Display the first few rows of the data
print(apple_data.head())


apple_data['200-day MA'] = apple_data['Close'].rolling(window=50).mean()

apple_data[['Close', '200-day MA']].plot(figsize=(10, 5))
plt.title('Apple Stock Prices with 200-day Moving Average')
plt.ylabel('Price (in $)')
plt.xlabel('Date')
plt.show()

weekly_data = apple_data['Close'].resample('W').mean()

weekly_data.plot(figsize=(10, 5))
plt.title('Apple Stock Weekly Closing Prices')
plt.ylabel('Price (in $)')
plt.xlabel('Date')
plt.show()

