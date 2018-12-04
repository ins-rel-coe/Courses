import pandas as pd

transactions = pd.read_csv("transactions.csv")
cat = pd.read_csv("ref.csv")

# Leave the default dataset as is
transactions_add = transactions

# Select reference column and merging column(s)
ref = cat[["Trans", "Category"]]  # Add more as applicable

# Matching columns of the 2 dataframes should have the same column name
ref = ref.rename(
        columns={
                "Trans": "Transaction"
                }
        )

# Match and merge columns from ref

transactions_add = transactions_add.merge(ref,
                                          on="Transaction",
                                          how="left")

# Or match and replace
transactions_rep = transactions
transactions_rep["Transaction"] = transactions_rep["Transaction"].map(
                                  ref.set_index("Transaction")["Category"]
                                  )

