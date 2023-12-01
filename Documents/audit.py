# auditing of Group report

import pandas as pd

# Load the CSV file into a DataFrame
file_path = "i1 positive.csv"
data = pd.read_csv(file_path)

def check_balanced(data):
    # Specify the column name where you want to check for 0 or 1
    target_column = "Label"

    # Count the number of samples with 0 and 1 in the specified column
    count_0 = len(data[data[target_column] == 0])
    count_1 = len(data[data[target_column] == 1])

    # Check if the dataset is balanced
    total = count_0 + count_1
    percent_0 = count_0 / total
    percent_1 = count_1 / total

    if percent_0 < 0.1 or percent_1 < 0.1:
        return False
    return True

def check_missing_values(data):
    # Check for missing values in the dataset
    if data.isnull().sum().any():
        return True
    return False

def check_enough_samples(data):
    # Check if there are enough samples in the dataset
    num_features = data.shape[1]

    # Get the number of samples (rows)
    num_samples = data.shape[0]

    # Calculate the ratio (Must be 10X)
    ratio = num_samples / num_features

    if ratio>10:
        return True
    return False

def printing(data):
    if data:
        return ""
    return "not"

print(f"The database does {printing(check_missing_values(data))} have missing values")
print(f"The database does {printing(check_enough_samples(data))} have enough samples")
print(f"The database is{printing(check_balanced(data))} balanced")

