import pandas as pd

# Extract - read the CSV file
def extract(filepath):
    print("Extracting data...")
    df = pd.read_csv(filepath)
    print(f"Loading {len(df)} transactions")
    return df

# Transform - clean the data
def transform(df):
    print("Transforming data...")
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])
    df = df.dropna()
    print("Data cleaned successfully")
    return df

# Load - display the data
def load(df):
    print("\n--- Transaction Summary ---")
    print(f"Total transactions: {len(df)}")
    print(f"Total spent: R{df['amount'].sum():.2f}")
    print("\nSpending by category:")
    print(df.groupby('category')['amount'].sum().sort_values(ascending=False))

# Run the pipeline  
if __name__ == "__main__":
    df = extract("data/transactions.csv")
    df = transform(df)
    load(df)