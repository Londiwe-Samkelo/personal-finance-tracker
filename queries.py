import sqlite3
import pandas as pd

conn = sqlite3.connect('finance.db')

print("=== Financial Insights ===\n")

# 1) Total spending 
total = pd.read_sql_query("SELECT SUM(amount) as total FROM transactions", conn)
print(f"Total spent: R{total['total'][0]:.2f}\n")

# 2) Average transaction amount
avg = pd.read_sql_query("SELECT AVG(amount) as average FROM transactions", conn)
print(f"Average transaction: R{avg['average'][0]:.2f}\n")

# 3) Spending by category (highest to lowest)
print("Spending by category:")
by_category = pd.read_sql_query('''
        SELECT category, SUM(amount) as total, COUNT(*) as num_transactions
        FROM transactions
        GROUP BY category
        ORDER BY total DESC
''', conn)
print(by_category)
print()

# 4) Top biggest single expenses
print("Top 3 biggest expenses:")
top3 = pd.read_sql_query('''
    SELECT description, amount, category
    FROM transactions
    ORDER BY amount DESC
    LIMIT 3
''', conn)
print(top3)
print()

# 5) Number of transactions per category
print("Transaction count per category:")
counts = pd.read_sql_query('''
    SELECT category, COUNT(*) as count
    FROM transactions
    GROUP BY category
    ORDER BY count DESC
''', conn)
print(counts)

conn.close()

