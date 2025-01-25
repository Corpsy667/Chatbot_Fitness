import pandas as pd

# Load the dataset
data = pd.read_csv('megaGymDataset.csv', index_col=0)
data = data.drop(columns=["Rating", "RatingDesc"])

print(data.head())
print(data["Type"].unique())