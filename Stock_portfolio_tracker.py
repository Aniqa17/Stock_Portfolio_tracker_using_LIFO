import yfinance as yf

# Stock Portfolio Tracker using Stack (LIFO)

# Download real HBL stock data from PSX (last 1 month, daily)
ticker = "HBL.KA"
data = yf.download(ticker, period="1mo", interval="1d")

# Extract closing prices as a list
prices = data['Close'].squeeze().tolist()

# Stack to hold buy prices (LIFO)
portfolio_stack = []

# Track total profit and loss separately
total_profit = 0
total_loss = 0
buy_count = 0
sell_count = 0

print("STOCK PORTFOLIO TRACKER (LIFO)")
print(f"Stock  : {ticker}")
print(f"Period : Last 1 Month (Daily)")
print(f"Days   : {len(prices)}")

# Go through each day one by one
for i in range(1, len(prices)):
    current_price = round(prices[i], 2)
    previous_price = round(prices[i-1], 2)

    # --- BUY ---
    # If price dropped from yesterday, buy (push onto stack)
    if current_price < previous_price:
        portfolio_stack.append(current_price)
        buy_count += 1
        print(f"\n[BUY]  Bought at: PKR {current_price}")
        print(f"       Stack: {portfolio_stack}")

    # --- SELL ---
    # If price rose from yesterday, sell (pop from stack)
    elif current_price > previous_price:

        # Only sell if portfolio has stocks
        if portfolio_stack:
            # Pop the most recently bought price (LIFO)
            buy_price = portfolio_stack.pop()
            difference = round(current_price - buy_price, 2)
            sell_count += 1

            # Check if profit or loss
            if difference >= 0:
                total_profit += difference
                print(f"\n[SELL] Sold at: PKR {current_price} | Bought at: PKR {buy_price} | Profit: +PKR {difference}")
            else:
                total_loss += abs(difference)
                print(f"\n[SELL] Sold at: PKR {current_price} | Bought at: PKR {buy_price} | Loss: -PKR {abs(difference)}")

            print(f"       Stack: {portfolio_stack}")

        else:
            # Can't sell if no stocks are held
            print("\n[SELL] Attempted but portfolio is empty — skipped!")

# ---- Final Summary ----
net = round(total_profit - total_loss, 2)

print("           FINAL SUMMARY")
print(f"  Total Buy Actions  : {buy_count}")
print(f"  Total Sell Actions : {sell_count}")
print(f"  Total Profit       : +PKR {round(total_profit, 2)}")
print(f"  Total Loss         : -PKR {round(total_loss, 2)}")
print(f"  Net Result         :  PKR {net}")

if net > 0:
    print("  Overall : PROFITABLE ✓")
elif net < 0:
    print("  Overall : IN LOSS ✗")
else:
    print("  Overall : BREAK EVEN")

if portfolio_stack:
    print(f"\n  Unsold stocks still in portfolio: {len(portfolio_stack)} shares")
    print(f"  Held at prices: {portfolio_stack}")
