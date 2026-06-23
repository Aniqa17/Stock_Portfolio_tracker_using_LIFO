# Stock Portfolio Tracker (LIFO)

A simple Python script that simulates a **stock trading strategy** using a **Last‑In, First‑Out (LIFO) stack** to track buy/sell decisions. It downloads real historical price data for a specific stock (HBL – Habib Bank Limited) from the Pakistan Stock Exchange (PSX) and evaluates profit/loss over a one‑month period.

## Features

- Fetches **daily closing prices** for `HBL.KA` using `yfinance`.
- Implements a **LIFO stack** to hold purchase prices.
- **Buys** whenever the price drops compared to the previous day.
- **Sells** whenever the price rises (only if stocks are held).
- Tracks:
  - Number of buy/sell actions
  - Total profit and total loss
  - Net result
  - Remaining unsold stocks (if any)
- Clean summary output with a final verdict (Profit / Loss / Break‑even).
