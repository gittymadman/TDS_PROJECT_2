
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads.csv"
df = pd.read_csv(file_path, encoding='latin-1')

# Visualization 1: Average Rating by Language
avg_rating_lang = df.groupby('language_code')['average_rating'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_rating_lang.plot(kind='bar', color='skyblue')
plt.title('Average Rating by Language')
plt.xlabel('Language Code')
plt.ylabel('Average Rating')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\avg_rating_by_language.png")
plt.clf()

# Visualization 2: Distribution of Original Publication Year
plt.figure(figsize=(10, 6))
df['original_publication_year'].dropna().hist(bins=50, color='lightgreen')
plt.title('Distribution of Original Publication Year')
plt.xlabel('Year')
plt.ylabel('Number of Books')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(r"D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\publication_year_distribution.png")
plt.clf()

# Visualization 3: Top 5 Authors by Ratings Count
top_authors = df.groupby('authors')['ratings_count'].sum().nlargest(5)
plt.figure(figsize=(10, 6))
top_authors.plot(kind='bar', color='lightcoral')
plt.title('Top 5 Authors by Ratings Count')
plt.xlabel('Authors')
plt.ylabel('Total Ratings Count')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\top_5_authors_by_ratings.png")
plt.clf()
