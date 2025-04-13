import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vgchartz-2024.csv")
print(df.info())
print(df.isnull().sum())
for col in df.columns:
    if df[col].dtype == 'object':  # Categorical
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:  # Numerical
        df[col].fillna(df[col].median(), inplace=True)
ch = "N/A"
df["developer"] = df["developer"].fillna(ch)

df.drop_duplicates(inplace=True)

print(df.isnull().sum())
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

print("\nSummary Statistics:\n")
print(df.describe())
df.to_excel("clean_vgsales.xlsx")





