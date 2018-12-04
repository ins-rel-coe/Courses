import pandas as pd

# Create a simple list
myList = ["a", "b", "c"]  # a list of strings
myList_int = [1, 2, 3]  # a list of integers
myList_flo = [1.0, 1.5, 2.0]  # list of floats

# Create an empty dataframe
empty_df = pd.DataFrame()

# Create a dataframe from a list
integer_df = pd.DataFrame(myList_int,
                          columns=["Integers"])

# Create a dataframe from multiple lists
mixed_df = pd.DataFrame(
        {
                "Letters": myList,
                "Floats": myList_flo
        }
        )

# Load dataset file to a dataframe
dataset = pd.read_csv("dataset.csv",
                      sep=",")
ExcelDataset = pd.read_excel("dataset.xlsx",
                             sheet_name="Sheet1",
                             header=0)

# View top 10 contents of a dataframe
dataset.head(10)

# View bottom 10 contents of a dataframe
ExcelDataset.tail(10)
