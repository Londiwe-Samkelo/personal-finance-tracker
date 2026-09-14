import sqlite3
import pandas as pd

def create_database():
    #connect to database (creates it if it doesn't exist)
    connect = sqlite3.connect('finance.db')
    cursor = connect.cursor()

    #create transactions table
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                   data TEXT NOT NULL,
                   description TEXT NOT NULL,
                   amount REAL NOT NULL,
                   categogy TEXT NOT NULL
                   )
    ''')

    
    connect.commit()
    print("Database created successfully!")
    return connect


def load_to_database(df, connect):
    #load dataframe into database
    df.to_sql('transactions', connect, if_exists = 'replace', index = False)
    print (f"Loaded {len(df)} transactions into database!")

def query_database(connect):
    print("\n--- Qyerying Database ---")

    #Total spent per category
    query = '''
        SELECT category, SUM(amount) as total
        FROM transactions
        GROUP BY category
        ORDER BY total DESC
    '''

    results = pd.read_sql_query(query, connect)
    print("\nSpending by category:")
    print(results)

    #Most expensive transaction
    query2 = '''
        SELECT description, amount, category
        FROM transactions
        ORDER BY amount DESC 
        LIMIT 1
    '''

if __name__ == "__main__":
    #Read the CSV
    df = pd.read_csv("data/transactions.csv")
    df['date'] = pd.to_datetime(df["date"])

    #Create database and load data 
    connect = create_database()
    load_to_database(df, connect)
    query_database(connect)

    connect.close()
    print("\nDone!")
