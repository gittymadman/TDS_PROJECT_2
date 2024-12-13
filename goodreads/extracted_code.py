
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
file_path = r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Remove rows where original_publication_year is null
data = data[data['original_publication_year'].notnull()]

# Group by original_publication_year and calculate the average rating
avg_rating_by_year = data.groupby('original_publication_year')['average_rating'].mean().reset_index()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(avg_rating_by_year['original_publication_year'], avg_rating_by_year['average_rating'], marker='o')
plt.title('Average Ratings by Original Publication Year')
plt.xlabel('Original Publication Year')
plt.ylabel('Average Rating')
plt.grid()
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\average_ratings_by_year.png')
plt.show()


# Plotting Distribution of Ratings Count
plt.figure(figsize=(12, 6))
plt.hist(data['ratings_count'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Ratings Count')
plt.xlabel('Ratings Count')
plt.ylabel('Frequency')
plt.xlim(0, data['ratings_count'].quantile(0.95))  # Limit to 95th percentile for better visualization
plt.grid()
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\distribution_of_ratings_count.png')
plt.show()


# Group by authors and calculate average ratings, then sort to find top authors
top_authors = data.groupby('authors')['average_rating'].mean().reset_index()
top_authors = top_authors.sort_values(by='average_rating', ascending=False).head(10)

# Plotting Top Authors by Average Ratings
plt.figure(figsize=(12, 6))
plt.barh(top_authors['authors'], top_authors['average_rating'], color='lightgreen')
plt.title('Top 10 Authors by Average Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Authors')
plt.grid()
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\goodreads\top_authors_by_average_ratings.png')
plt.show()
