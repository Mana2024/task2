import requests

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]["quantity"] += quantity
        else:
            self.portfolio[symbol] = {"quantity": quantity, "price": self.get_stock_price(symbol)}

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]["quantity"]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]["quantity"] -= quantity
        else:
            print(f"You don't own any {symbol} in your portfolio.")

    def get_stock_price(self, symbol):
        api_key = 'IM6S5QPLLZTOUZO7'
        endpoint = f'https://www.alphavantage.co/query'
        function = 'GLOBAL_QUOTE'
        params = {
            'function': function,
            'symbol': symbol,
            'apikey': api_key
        }

        try:
            response = requests.get(endpoint, params=params)
            data = response.json()
            return float(data['Global Quote']['05. price'])
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def track_portfolio_performance(self):
        total_value = 0.0
        print("Portfolio Performance:")
        print("{:<10} {:<10} {:<10} {:<10}".format("Symbol", "Quantity", "Price", "Value"))
        for symbol, details in self.portfolio.items():
            quantity = details["quantity"]
            price = details["price"]
            value = quantity * price
            total_value += value
            print("{:<10} {:<10} ${:<10} ${:<10}".format(symbol, quantity, price, value))
        print("Total Portfolio Value: ${:.2f}".format(total_value))


# Example usage:
portfolio_tracker = StockPortfolioTracker()

portfolio_tracker.add_stock("AAPL", 10)
portfolio_tracker.add_stock("GOOGL", 5)
portfolio_tracker.add_stock("MSFT", 8)

portfolio_tracker.track_portfolio_performance()

portfolio_tracker.remove_stock("AAPL", 5)

portfolio_tracker.track_portfolio_performance()
