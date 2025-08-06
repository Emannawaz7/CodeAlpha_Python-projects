#  stock prices
stock_prices = {
    "HBL": 10,
    "UBL": 200,
    "ABL": 352,
    "ITL": 500,
    "DIR": 60
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' when finished.\n")

# Collect user input
while True:
    stock = input("Enter stock symbol (e.g., HBL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Invalid stock symbol. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print(" Quantity must be a number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate and display result
print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_value += investment
    print(f"🔹 {stock}: {qty} shares × ${price} = ${investment}")

print(f"\n Total Investment Value: ${total_value}")

#  Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(" Portfolio saved to 'portfolio_summary.txt'")
