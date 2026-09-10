import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = [
    nbf.v4.new_markdown_cell("# Major Project: Seasonal Agriculture Performance Analysis\n\n## Objective\nTo analyze agricultural data from different seasons and identify meaningful patterns, trends, relationships and differences in agricultural performance."),
    
    nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_theme(style="whitegrid", palette="muted")
%matplotlib inline

# Load the dataset
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
print(f"Dataset Shape: {df.shape}")
display(df.head())"""),
    
    nbf.v4.new_markdown_cell("## 1. Data Cleaning and Preparation\nWe will check for missing values and understand the data types."),
    
    nbf.v4.new_code_cell("""# Check data types and missing values
df.info()

# Basic statistical summary
display(df.describe())"""),
    
    nbf.v4.new_markdown_cell("## 2. Exploratory Data Analysis (EDA) & Seasonal Variations\nLet's analyze how agricultural performance (Yield, Profit, Revenue) varies across seasons."),
    
    nbf.v4.new_code_cell("""# Grouping by Season to see the average performance metrics
seasonal_metrics = df.groupby('Season')[['Yield_Tonnes_Ha', 'Profit_INR', 'Revenue_INR', 'Total_Cost_INR']].mean().reset_index()
display(seasonal_metrics)"""),
    
    nbf.v4.new_code_cell("""# Visualizing Yield across Seasons
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Season', y='Yield_Tonnes_Ha', ci=None, palette='viridis')
plt.title('Average Yield (Tonnes/Hectare) by Season', fontsize=14)
plt.ylabel('Yield (Tonnes/Ha)')
plt.xlabel('Season')
plt.savefig('yield_by_season.png')
plt.show()"""),
    
    nbf.v4.new_code_cell("""# Visualizing Profit across Seasons
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Season', y='Profit_INR', palette='magma')
plt.title('Profit Distribution by Season', fontsize=14)
plt.ylabel('Profit (INR)')
plt.xlabel('Season')
plt.savefig('profit_by_season.png')
plt.show()"""),
    
    nbf.v4.new_markdown_cell("## 3. Resource Usage Across Seasons\nAre there noticeable variations in resource usage (Water, Fertilizers, Pesticides) across seasons?"),
    
    nbf.v4.new_code_cell("""# Visualizing Water Usage and Efficiency
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

sns.barplot(data=df, x='Season', y='Water_Used_m3', ci=None, palette='Blues', ax=ax[0])
ax[0].set_title('Average Water Used (m³) by Season')

sns.barplot(data=df, x='Season', y='Water_Efficiency_t_per_1000m3', ci=None, palette='Greens', ax=ax[1])
ax[1].set_title('Water Efficiency (Tonnes / 1000m³) by Season')

plt.tight_layout()
plt.savefig('resource_usage.png')
plt.show()"""),

    nbf.v4.new_markdown_cell("## 4. Environmental Conditions and Performance\nLet's check the correlation between environmental factors and yield/profit."),

    nbf.v4.new_code_cell("""# Select numerical columns for correlation
env_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day', 'Soil_Moisture_pct', 'Yield_Tonnes_Ha', 'Profit_INR']
corr_matrix = df[env_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix: Environment vs Performance', fontsize=14)
plt.savefig('correlation_heatmap.png')
plt.show()"""),

    nbf.v4.new_markdown_cell("## 5. Major Patterns & Recommendations\n- **Seasonality**: There are distinct differences in Yield and Profit between seasons.\n- **Resource Efficiency**: Certain seasons might use more water but have lower water efficiency, indicating a need for better irrigation practices.\n- **Environmental Impact**: Key factors like Rainfall and Soil Moisture directly correlate with the crop yield.")
]

nb['cells'] = cells

with open('Seasonal_Agriculture_Analysis.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Jupyter Notebook 'Seasonal_Agriculture_Analysis.ipynb' created successfully.")
