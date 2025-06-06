import pandas as pd

# Read the CSV file
df = pd.read_csv('f1.csv')  # Replace with your actual file path

# Calculate and print the average of a numeric column
average = df['age'].mean()  # Replace 'column_name' with your actual column name
print(f"The average is: {average}")
