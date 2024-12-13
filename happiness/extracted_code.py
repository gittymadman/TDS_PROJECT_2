
import pandas as pd
import matplotlib.pyplot as plt

# File paths
csv_file_path = 'D:\\IITM-BSC\\TDS\\TDS_PROJECT_2\\happiness.csv'
output_directory = 'D:\\IITM-BSC\\TDS\\TDS_PROJECT_2\\happiness\\'

# Read the dataset using latin-1 encoding
data = pd.read_csv(csv_file_path, encoding='latin-1')

# Remove rows where important values are missing
data = data.dropna(subset=['Log GDP per capita', 'Life Ladder', 'Social support', 'Healthy life expectancy at birth'])

# 1. Life Ladder vs. Log GDP per capita
plt.figure(figsize=(10, 6))
plt.scatter(data['Log GDP per capita'], data['Life Ladder'], alpha=0.5)
plt.title('Life Ladder vs. Log GDP per Capita')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Life Ladder')
plt.grid()
plt.savefig(output_directory + 'Life_Ladder_vs_Log_GDP_per_Capita.png')
plt.close()

# 2. Average Life Ladder by Year
avg_life_ladder_by_year = data.groupby('year')['Life Ladder'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(avg_life_ladder_by_year['year'], avg_life_ladder_by_year['Life Ladder'], marker='o')
plt.title('Average Life Ladder by Year')
plt.xlabel('Year')
plt.ylabel('Average Life Ladder')
plt.xticks(range(2005, 2024))
plt.grid()
plt.savefig(output_directory + 'Average_Life_Ladder_by_Year.png')
plt.close()

# 3. Distribution of Social Support
plt.figure(figsize=(10, 6))
plt.hist(data['Social support'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Social Support')
plt.xlabel('Social Support')
plt.ylabel('Frequency')
plt.grid()
plt.savefig(output_directory + 'Distribution_of_Social_Support.png')
plt.close()
