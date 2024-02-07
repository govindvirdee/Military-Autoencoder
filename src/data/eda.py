# Imports 
import warnings
warnings.filterwarnings('ignore')
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import os
import joblib

file_path = '../../data/raw/KDDTrain+.csv'

# Load the CSV file
data = pd.read_csv(file_path)

# Convert to a pandas DataFrame
df = pd.DataFrame(data)
df.columns = df.columns.str.strip("'")

#print(df.head())

# Define the mapping
class_mapping = {'normal': 0, 'anomaly': 1}

# Create a new column with binary values
df['class_binary'] = df["class"].map(class_mapping)

# Selecting only numerical variables
numerical_df = df.select_dtypes(include=['float64', 'int64'])
# Selecting categorical variables
categorical_df = df.select_dtypes(include=['object', 'category'])


# Compute the correlation matrix
corr = numerical_df.corr()
# Generate a heatmap
plt.figure(figsize=(30, 30))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Numerical Variables')
plt.savefig("../../reports/figures/correlations.png")
print("Plot saved to reports/figures/correlations.png")

# Note - this takes a long time  
# sns.pairplot(numerical_df)
# plt.savefig("../../reports/figures/pairplot.png")
# print("Plot saved to reports/figures/pairplot.png")


# Plot bar charts for each categorical variable
for column in categorical_df:
    plt.figure(figsize=(10, 4))
    sns.countplot(x=column, data=categorical_df)
    plt.title(f'Bar Chart for {column}')
    plt.xticks(rotation=45)
    plt.savefig("../../reports/figures/{}.png".format(column))
    print("Plot saved to reports/figures/{}.png".format(column))

