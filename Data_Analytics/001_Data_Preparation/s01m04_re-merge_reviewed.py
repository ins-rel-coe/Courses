import pandas as pd

dataset = pd.read_excel("output.xlsx",
                        sheet_name="Sheet1",
                        header=0)

# Extra: What if the column headers/names are not in the first row?
"""
dataset_skip = pd.read_excel("dataset_skip.xlsx",
                             sheet_name="Sheet1",
                             skiprows=[0, 1, 2])  # Col names are in Row 3
"""

reviewed = pd.read_csv("reviewed.csv")

# Append and sort
dataset = dataset.append(reviewed)

updated = dataset.sort_values("idx")

updated.to_excel("updated.xlsx", sheet_name="Sheet1", header=True,
                 index=False)
