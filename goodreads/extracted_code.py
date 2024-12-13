
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads.csv'
df = pd.read_csv(file_path, encoding='latin-1')

# Visualization 1: Histogram of Average Ratings
plt.figure(figsize=(10, 6))
plt.hist(df['average_rating'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Average Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Number of Books')
plt.grid(axis='y', alpha=0.75)
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\average_rating_distribution.png')
plt.close()

# Visualization 2: Bar Chart of Book Counts by Original Publication Year
publication_year_counts = df['original_publication_year'].dropna().value_counts().sort_index()
plt.figure(figsize=(12, 6))
publication_year_counts.plot(kind='bar', color='orange')
plt.title('Number of Books Published by Year')
plt.xlabel('Publication Year')
plt.ylabel('Number of Books')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\books_by_year.png')
plt.close()

# Visualization 3: Box Plot of Ratings Count
plt.figure(figsize=(10, 6))
plt.boxplot(df['ratings_count'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Box Plot of Ratings Count')
plt.xlabel('Ratings Count')
plt.grid(axis='x', alpha=0.75)
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\ratings_count_boxplot.png')
plt.close()
