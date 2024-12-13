
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'D:\IITM-BSC\TDS\TDS_PROJECT_2\happiness.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Set the path for saving images
save_path = r'D:\IITM-BSC\TDS\TDS_PROJECT_2\happiness'

# 1. Distribution of Life Ladder Scores
plt.figure(figsize=(10, 6))
plt.hist(data['Life Ladder'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Life Ladder Scores')
plt.xlabel('Life Ladder Score')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig(f"{save_path}\\life_ladder_distribution.png")
plt.close()

# 2. Correlation Between Log GDP per Capita and Life Ladder
plt.figure(figsize=(10, 6))
plt.scatter(data['Log GDP per capita'], data['Life Ladder'], alpha=0.5)
plt.title('Log GDP per Capita vs Life Ladder')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Life Ladder Score')
plt.grid()
plt.savefig(f"{save_path}\\gdp_vs_life_ladder.png")
plt.close()

# 3. Box Plot of Life Ladder by Country
plt.figure(figsize=(15, 8))
data.boxplot(column='Life Ladder', by='Country name', rot=90)
plt.title('Life Ladder Scores by Country')
plt.suptitle('')
plt.xlabel('Country')
plt.ylabel('Life Ladder Score')
plt.grid(axis='y', alpha=0.75)
plt.savefig(f"{save_path}\\life_ladder_by_country.png")
plt.close()
