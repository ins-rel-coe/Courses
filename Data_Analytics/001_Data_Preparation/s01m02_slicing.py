import pandas as pd

# Load dataset file to a dataframe
dataset = pd.read_csv("dataset.csv",
                      sep=",")

# Select a column and assign it to a variable
select1 = dataset["Zone"]
# Select columns except specified one
select1a = dataset[dataset.columns.difference(["Zone"])]

# Select more than one column and assign it to a variable
ref1 = ["Account Number:.", "Zone"]
select2 = dataset[ref1]
# Select columns except specified multiple
ref2 = ["Zone", "Account Tenure"]
select2a = dataset[dataset.columns.difference(ref2)]

# Select rows matching a column value
select3 = dataset.loc[dataset["Zone"] == "SNA"]

# Select rows matching a column with multiple values
ref3 = ["SNA", "GEA"]
select4 = dataset.loc[dataset["Zone"].isin(ref3)]

# Select rows matching multiple columns
# with single values each
select5 = dataset.loc[
        (dataset["Zone"] == "SNA") & (dataset["Status"] == "Undecided")
        ]

# Select rows matching multiple columns
# with single & multiple values each
select6 = dataset.loc[
        (dataset["Zone"].isin(ref3)) & (dataset["Status"] == "Undecided")
        ]

# Select rows where any column is null
select8 = dataset[dataset.isnull().any(axis=1)]

# Select rows where a specific column has a null value
select9 = dataset[dataset["Account Number:."].isnull()]

# Select rows where specific column values has a null value
ref5 = ["Account Number:.", "Delay Reason:"]
select10 = dataset[dataset[ref5].isnull().any(axis=1)]
