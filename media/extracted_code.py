
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = r'D:\IITM-BSC\TDS\TDS_PROJECT_2\media.csv'
media_data = pd.read_csv(file_path, encoding='latin-1')

# Histogram for Overall Ratings Distribution
plt.figure(figsize=(10, 6))
plt.hist(media_data['overall'], bins=range(1, 7), edgecolor='black', alpha=0.7)
plt.title('Distribution of Overall Ratings')
plt.xlabel('Overall Rating')
plt.ylabel('Frequency')
plt.xticks(range(1, 6))
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\media\overall_ratings_distribution.png')
plt.close()

# Box Plot for Quality Ratings
plt.figure(figsize=(10, 6))
plt.boxplot(media_data['quality'], vert=False)
plt.title('Box Plot of Quality Ratings')
plt.xlabel('Quality Rating')
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\media\quality_ratings_boxplot.png')
plt.close()

# Bar Chart for Repeatability Count by Quality
repeatability_counts = media_data.groupby('quality')['repeatability'].value_counts().unstack().fillna(0)
repeatability_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Repeatability Count by Quality')
plt.xlabel('Quality Rating')
plt.ylabel('Count')
plt.legend(title='Repeatability Rating')
plt.savefig(r'D:\IITM-BSC\TDS\TDS_PROJECT_2\media\repeatability_count_by_quality.png')
plt.close()
