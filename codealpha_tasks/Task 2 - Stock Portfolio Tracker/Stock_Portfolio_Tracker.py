# ==========================================
# Stock Portfolio Tracker
# CodeAlpha Python Internship Project
# Author: Priya
# ==========================================

# Predefined stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "WIPRO": 280,
    "RELIANCE": 1500,
    "HCL": 1800,
    "TECHM": 1700,
    "SBIN": 800
}


# Function to display available stocks
def display_stocks():
    print("\n📈 Available Stocks")
    print("-" * 35)
    print(f"{'Stock':<15}{'Price'}")
    print("-" * 35)

    for stock, price in stock_prices.items():
        print(f"{stock:<15}₹{price}")

    print("-" * 35)


# Function to create and calculate portfolio
def calculate_portfolio():
    portfolio = {}
    total_value = 0

    display_stocks()

    # Input validation for number of stocks
    while True:
        try:
            n = int(input("\nHow many different stocks do you own? "))

            if n <= 0:
                print("❌ Please enter a number greater than 0.")
            else:
                break

        except ValueError:
            print("❌ Please enter a valid number.")

    # Take stock details from user
    for i in range(n):
        print(f"\nStock {i + 1}")

        stock_name = input("Enter stock name: ").upper()

        # Check stock availability
        if stock_name not in stock_prices:
            print("❌ Stock not available in database.")
            continue

        # Input validation for quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("❌ Quantity must be greater than 0.")
                else:
                    break

            except ValueError:
                print("❌ Please enter a valid quantity.")

        # Handle duplicate stocks
        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

    # Display portfolio summary
    print("\n📊 YOUR PORTFOLIO")
    print("-" * 55)
    print(f"{'Stock':<15}{'Quantity':<15}{'Price':<10}{'Value'}")
    print("-" * 55)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value

        print(f"{stock:<15}{quantity:<15}₹{price:<9}₹{value}")

    print("-" * 55)
    print(f"💰 Total Portfolio Value: ₹{total_value}")


# Main Program
print("======================================")
print("   STOCK PORTFOLIO TRACKER")
print("======================================")

while True:
    calculate_portfolio()

    choice = input(
        "\nDo you want to calculate another portfolio? (yes/no): "
    ).lower()

    if choice != "yes":
        break

print("\nThank you for using Stock Portfolio Tracker!")
