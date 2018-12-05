import pandas as pd
import time

# Time start
t_start = time.time()

##############################START CODE###############################

# Specify needed columns
myColumns = ["Call Date:",
             "Account Number:.",
             "Account Tenure",
             "Amount:",
             "Delay Reason:",
             "Zone",
             "Status"
        ]

# Function that tests if a string is numeric
def test_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Load dataset file to a dataframe, only loading specified columns
dataset = pd.read_csv("dataset.csv",
                      sep=",",
                      usecols=myColumns)

dataset = dataset.rename(columns={
        "Call Date:": "Call_Date",
        "Account Number:.": "AcctNum",
        "Account Tenure": "AcctTen",
        "Amount:": "Amt",
        "Delay Reason:": "Reason"
        }
        )

# Check duplicates
dataset.duplicated()  # Consider all rows
num_duplicates = (
        len(dataset.duplicated())
        - len(dataset.drop_duplicates(keep="first"))
        )
dataset = dataset.drop_duplicates(keep="first")  # Drop duplicate rows

# Note: keep="first" or keep="last" is case-to-case basis

# Create a snapshot of the default row sequence
dataset.insert(0, column="idx", value=dataset.index)

# Create an empty dataframe to hold items (rows) for review
review = pd.DataFrame()

# Check null entries (Note: Case-to-case basis)
# Scan
dataset.columns[dataset.isnull().any()]  # Columns with null entries
# Inspect
dataset[dataset["AcctNum"].isnull()]
# Isolate
review = review.append(dataset[dataset["AcctNum"].isnull()])
# Drop
dataset = dataset[~dataset["AcctNum"].isnull()]

# Standardize date format
dataset["Call_Date"] = pd.to_datetime(dataset["Call_Date"])
dataset["Call_Date"] = dataset["Call_Date"].dt.strftime("%Y-%m-%d")

# Correct typing in Tenure
# Scan
dataset["AcctTen"].unique()
# Correct
dataset["AcctTen"] = dataset["AcctTen"].str.replace("&", "and")
# Scan
dataset["AcctTen"].unique()

# Check errors in numeric values
# Scan
dataset[~dataset["Amt"].apply(lambda x: test_numeric(x))]
# Inspect
dataset["Amt"][~dataset["Amt"].apply(lambda x: test_numeric(x))]

# Correct typing in Amt
dataset["Amt"][dataset["Amt"].str.contains(r"\d+\.\.\d{0,2}", regex=True)]
# Correct
dataset["Amt"] = dataset["Amt"].str.replace(r"\.\.", ".", regex=True)
# Scan
dataset["Amt"][dataset["Amt"].str.contains(r"\d+\.\.\d{0,2}", regex=True)]

# Scan
dataset["Amt"][dataset["Amt"].str.contains(r"\d+\.\d{3}", regex=True)]
# Isolate
review = review.append(dataset[dataset["Amt"].str.contains(r"\d+\.\d{3}",
                               regex=True)])
# Drop
dataset = dataset[~dataset["Amt"].str.contains(r"\d+\.\d{3}", regex=True)]

# Scan
dataset["Amt"][dataset["Amt"].str.contains(" ")]
# Correct
dataset["Amt"] = dataset["Amt"].str.replace(" ", "")
# Scan
dataset["Amt"][dataset["Amt"].str.contains(" ")]

# Scan
dataset["Amt"][dataset["Amt"].str.contains(",")]
# Inspect
dataset["Amt"][dataset["Amt"].str.contains(r"^\d{4}\,\d{2}$", regex=True)]
# Correct
dataset["Amt"] = dataset["Amt"].str.replace(r"^(\d{4})\,(\d{2})$",
       r"\1.\2", regex=True)
dataset["Amt"] = dataset["Amt"].str.replace(r"(.)\,$", r"\1", regex=True)
dataset["Amt"] = dataset["Amt"].str.replace(",", "")
# Scan
dataset["Amt"][dataset["Amt"].str.contains(",")]

# Any more remaining?
"""
dataset[~dataset["Amt"].apply(lambda x: test_numeric(x))]
dataset["Amt"][~dataset["Amt"].apply(lambda x: test_numeric(x))]
"""

# One more left!
# Scan
dataset["Amt"][dataset["Amt"].str.contains(r"^\d{2}\.\d{2}\.\d$",
                                           regex=True)]
# Correct
dataset["Amt"] = dataset["Amt"].str.replace(r"^(\d{2})\.(\d{2}\.\d)$",
                                            r"\1\2",
                                            regex=True)
# Scan
dataset["Amt"][dataset["Amt"].str.contains(r"^\d{2}\.\d{2}\.\d$",
                                           regex=True)]
# Test again!
dataset[~dataset["Amt"].apply(lambda x: test_numeric(x))]  # No more left
dataset["Amt"] = dataset["Amt"].astype("float64")

# Correct typing in Reason
# Scan
dataset["Reason"].unique()
# Inspect
dataset["Reason"][dataset["Reason"].isnull()]
dataset[["Status", "Reason"]][dataset["Reason"].isnull()]
# Correct
dataset["Reason"] = dataset["Reason"].fillna("Z")
# Scan
dataset["Reason"].unique()

# Correct typing in Zone
# Scan
dataset["Zone"].unique()
# Isolate
review = review.append(dataset[dataset["Zone"].str.contains("`")])
# Drop
dataset = dataset[~dataset["Zone"].str.contains("`")]

# Correct typing in Status
# Scan
dataset["Status"].unique()
# Correct
dataset["Status"] = dataset["Status"].str.replace(r"^ Will", "Will",
                                                  regex=True)
dataset["Status"] = dataset["Status"].str.replace(r"^Contacted -  Will",
                                                  "Contacted - Will",
                                                  regex=True)
# Scan
dataset["Status"].unique()

# Convert amount to USD
"""
dataset["Amt"] = dataset["Amt"] / 54
"""

# Save to an excel file
dataset.to_excel("output.xlsx", sheet_name="Sheet1", header=True,
                 index=False)
review.to_excel("review.xlsx", sheet_name="Sheet1", header=True,
                 index=False)

###############################END CODE################################

# Time end
t_end = time.time()
print("\n\nExecution completed in "
      + "{0:.2f}".format(t_end-t_start)
	  + " second(s).\n\n")
