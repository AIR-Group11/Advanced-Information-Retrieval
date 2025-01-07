import os
import pandas as pd

# Define the folder containing the datasets
folder_path = os.path.join(os.getcwd(), "datasets")

# List to store dataframes
dataframes = []

# Iterate over each file in the folder
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        # Read the CSV file into a dataframe
        df = pd.read_csv(file_path)
        # Optionally add a column to track the original file name
        df['Source'] = file
        dataframes.append(df)

# Concatenate all dataframes into a single dataframe
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged dataframe to a new CSV file
output_file = os.path.join(folder_path, "dataset.csv")
merged_df.to_csv(output_file, index=False)

print(f"Merged dataset saved to {output_file}")
