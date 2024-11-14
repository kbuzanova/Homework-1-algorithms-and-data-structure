def average(shares, min_price=None, max_price=None):
    prices = [
        share["price"] for share in shares
        if share["price"] is not None and
           (min_price is None or share["price"] >= min_price) and
           (max_price is None or share["price"] <= max_price)
    ]
    if prices:
        return sum(prices) / len(prices)
    else:
        return None

shares = [
    {"name": "AAPL", "price": 150},
    {"name": "GOOGL", "price": 2800},
    {"name": "TSLA", "price": 700},
    {"name": "AMZN", "price": None},
    {"name": "MSFT", "price": 350},
    {"name": "NFLX", "price": 500},
]

print(average(shares))
print(average(shares, min_price=300, max_price=800))
print(average(shares, min_price=1000))
print(average(shares, max_price=200))
