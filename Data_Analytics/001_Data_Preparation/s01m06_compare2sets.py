import pandas as pd

companies_1 = pd.read_csv("companies.csv")
companies_2 = pd.read_csv("organizations.csv")

# Check items in the columns
companies_1["Companies"].unique()
companies_2["Company"].unique()

# Convert to set to enable comparison between them

comp_1 = set(companies_1["Companies"].unique())
comp_2 = set(companies_2["Company"].unique())

# INTERSECTION: Companies in both comp_1 and comp_2
comp_intersect = comp_1.intersection(comp_2)
# Convert to list
comp_intersect = list(comp_intersect)
# Then to dataframe
comp_intersect = pd.DataFrame(comp_intersect,
                              columns=["Companies"])

# SYMMETRIC DIFFERENCE: Companies in either comp_1 and comp_2
# but not both
comp_symm = comp_1.symmetric_difference(comp_2)
# Convert to list, then sort
comp_symm = sorted(list(comp_symm))
# Then to dataframe
comp_symm = pd.DataFrame(comp_symm,
                         columns=["Companies"])

# DIFFERENCE: Companies only in comp_1 but not in comp_2
comp_diff = comp_1.difference(comp_2)
# Convert to list
comp_diff = list(comp_diff)
# Then to dataframe
comp_diff = pd.DataFrame(comp_diff,
                         columns=["Companies"])

# POP QUIZ: How about "companies only in comp_2
# but not in comp_1"?
