# EDA for clean_vgsales.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style='whitegrid', palette='muted')
plt.rcParams['figure.figsize'] = (12, 6)


df = pd.read_excel('clean_vgsales.xlsx')

rename_dict = {}
if 'pal_sales' in df.columns:
    rename_dict['pal_sales'] = 'eu_sales'
if 'global_sales' in df.columns:
    rename_dict['global_sales'] = 'total_sales'

df.rename(columns=rename_dict, inplace=True)


numerical_features = ['critic_score', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'total_sales']

# Distribution plots
for feature in numerical_features:
    if feature in df.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[feature], bins=30, kde=True, color='skyblue')
        plt.title(f"Distribution of {feature}", fontsize=16)
        plt.xlabel(feature, fontsize=14)
        plt.ylabel('Count')
        plt.show()

#  Correlation heatmap
plt.figure(figsize=(10, 8))
corr = df[numerical_features].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap', fontsize=18)
plt.show()

#  Total Sales by Genre
if 'genre' in df.columns and 'total_sales' in df.columns:
    genre_sales = df.groupby('genre')['total_sales'].sum().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=genre_sales, x='genre', y='total_sales', hue='genre', palette="viridis", dodge=False, legend=False)
    plt.xticks(rotation=45)
    plt.title('Total Sales by Genre', fontsize=18)
    plt.ylabel('Total Sales (millions)')
    plt.xlabel('Genre')
    plt.show()

#  Top 10 Publishers
if 'publisher' in df.columns and 'total_sales' in df.columns:
    publisher_sales = df.groupby('publisher')['total_sales'].sum().sort_values(ascending=False).reset_index().head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=publisher_sales, y='publisher', x='total_sales', hue='publisher', palette='magma', dodge=False, legend=False)
    plt.title('Top 10 Publishers by Total Sales', fontsize=18)
    plt.xlabel('Total Sales (millions)')
    plt.ylabel('Publisher')
    plt.show()

#  Top 10 Platforms
if 'platform' in df.columns and 'total_sales' in df.columns:
    platform_sales = df.groupby('platform')['total_sales'].sum().sort_values(ascending=False).reset_index().head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=platform_sales, x='platform', y='total_sales', hue='platform', palette="Set2", dodge=False, legend=False)
    plt.title('Top 10 Platforms by Total Sales', fontsize=18)
    plt.ylabel('Total Sales (millions)')
    plt.xlabel('Platform')
    plt.show()

#  Critic Score vs Total Sales
if 'critic_score' in df.columns and 'total_sales' in df.columns:
    plt.figure(figsize=(10, 6))
    if 'platform' in df.columns:
        sns.scatterplot(data=df, x='critic_score', y='total_sales', hue='platform', palette='tab10', alpha=0.7)
    else:
        sns.scatterplot(data=df, x='critic_score', y='total_sales', color='tab:blue', alpha=0.7)
    plt.title('Critic Score vs Total Sales', fontsize=18)
    plt.xlabel('Critic Score')
    plt.ylabel('Total Sales (millions)')
    if 'platform' in df.columns:
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
    plt.show()

#  Total Sales Over Years
if 'year' in df.columns:
    df['year'] = pd.to_numeric(df['year'], errors='coerce')

    yearly_sales = df.groupby('year')['total_sales'].sum().reset_index()

    plt.figure(figsize=(14, 6))
    sns.lineplot(data=yearly_sales, x='year', y='total_sales', marker='o')
    plt.title('Total Sales Over Years', fontsize=18)
    plt.ylabel('Total Sales (millions)')
    plt.xlabel('Year')
    plt.grid(True)
    plt.show()
