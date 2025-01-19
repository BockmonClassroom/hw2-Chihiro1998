# Name: Yuchen(Olivia) Kuang
# Date: 2025/1/18
# Function: Data analysis and visualization of my plant

# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read the data of my plant
data = pd.read_csv('data/plant_data.csv')

# Print all the data line by line to test my csv documnt organize in a right way
# print(data.to_string())

# 1.Graph histograms of your data with appropriate labels.

# Draw the histograms of leaf_width
plt.figure(figsize=(14, 10))

# Histograms title for all
plt.suptitle('Leaf Width', fontsize=20, fontweight='bold')

# leaf_width - All
plt.subplot(2, 2, 1)
plt.hist(data['leaf_width'], bins=10, color='lightblue',edgecolor='White')
plt.xlabel('All')
plt.ylabel('Count')

# leaf_width - Zamioculcas zamiifolia
plt.subplot(2, 2, 2)
subset = data[data['plant_name'] == 'Zamioculcas zamiifolia']
plt.hist(subset['leaf_width'], bins=10, color='skyblue',edgecolor='White')
plt.xlabel('Zamioculcas zamiifolia')
plt.ylabel('Count')

# leaf_width - Snake Plant
plt.subplot(2, 2, 3)
subset = data[data['plant_name'] == 'Snake Plant']
plt.hist(subset['leaf_width'], bins=10, color='pink',edgecolor='White')
plt.xlabel('Snake Plant')
plt.ylabel('Count')

# leaf_width - Bunny Ears Cactus
plt.subplot(2, 2, 4)
subset = data[data['plant_name'] == 'Bunny Ears Cactus']
plt.hist(subset['leaf_width'], bins=10, color='salmon', edgecolor='White')
plt.xlabel('Bunny Ears Cactus')
plt.ylabel('Count')

# show the graph
plt.tight_layout()
plt.show()

# Draw the histograms of leaf_length
plt.figure(figsize=(14, 10))

# Histograms title for all
plt.suptitle('Leaf Length', fontsize=20, fontweight='bold')

# leaf_length - All
plt.subplot(2, 2, 1)
plt.hist(data['leaf_length'], bins=10, color='lightblue', edgecolor='White')
plt.xlabel('All')
plt.ylabel('Count')

# leaf_length - Zamioculcas zamiifolia
plt.subplot(2, 2, 2)
subset = data[data['plant_name'] == 'Zamioculcas zamiifolia']
plt.hist(subset['leaf_length'], bins=10, color='skyblue', edgecolor='White')
plt.xlabel('Zamioculcas zamiifolia')
plt.ylabel('Count')

# leaf_length - Snake Plant
plt.subplot(2, 2, 3)
subset = data[data['plant_name'] == 'Snake Plant']
plt.hist(subset['leaf_length'], bins=10, color='pink', edgecolor='White')
plt.xlabel('Snake Plant')
plt.ylabel('Count')

# leaf_length - Bunny Ears Cactus
plt.subplot(2, 2, 4)
subset = data[data['plant_name'] == 'Bunny Ears Cactus']
plt.hist(subset['leaf_length'], bins=10, color='salmon', edgecolor='White')
plt.xlabel('Bunny Ears Cactus')
plt.ylabel('Count')

# Adjust layout to leave space for the main title
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# 2. Graph boxplots of your data with appropriate labels. 

# # Extract leaf_width and leaf_length of all
all_width_data = data['leaf_width'] 
all_length_data = data['leaf_length'] 

plants = ['All'] + list(data['plant_name'].unique())

# Extract leaf_width and leaf_length data by plant_name
width_groups = [all_width_data] + [data[data['plant_name'] == plant]['leaf_width'] for plant in plants[1:]]
length_groups = [all_length_data] + [data[data['plant_name'] == plant]['leaf_length'] for plant in plants[1:]]

# Draw the boxplots for leaf_width and leaf_length
plt.figure(figsize=(14, 6)) 

# leaf_width
plt.subplot(1, 2, 1)
plt.boxplot(width_groups, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='black'), 
            medianprops=dict(color='red'), 
            showfliers=True)
plt.xticks(range(1, len(plants) + 1), plants, fontsize=12)
plt.title('Leaf Width', fontsize=16)

# leaf_length
plt.subplot(1, 2, 2)
plt.boxplot(length_groups, patch_artist=True, 
            boxprops=dict(facecolor='lightgreen', color='black'), 
            medianprops=dict(color='red'), 
            showfliers=True)
plt.xticks(range(1, len(plants) + 1), plants, fontsize=12)
plt.title('Leaf Length', fontsize=16)

# show the graph
plt.tight_layout()
plt.show()

# 3. Graph a scatter plot of your entire data set with each subset different color and a ledger

# Set the color and label data
colors = ['lightcoral', 'lightgreen', 'lightskyblue']
labels = data['plant_name'].unique() 

# Draw the scatter plot
plt.figure(figsize=(10, 6))

# Draw the plot for each plant
for plant, color in zip(labels, colors):
    subset = data[data['plant_name'] == plant]
    plt.scatter(subset['leaf_width'], subset['leaf_length'], 
                color=color, label=plant, alpha=0.8, s=100, edgecolor='gray')

# Set the range for X and Y
plt.xlim(2, 8)
plt.ylim(2, 30) 

# Set the title and Label name
plt.title('Leaf Length vs Width', fontsize=16)
plt.xlabel('Leaf Width', fontsize=12)
plt.ylabel('Leaf Length', fontsize=12)

# Add the grid
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Add a legend
plt.legend(fontsize=12, title_fontsize=15, loc='upper left')

# show the graph
plt.tight_layout()
plt.show()

# 4. Explain each graph in terms of variance, mean, median, and standard deviation. 

# Get unique plant names
plants = data['plant_name'].unique()

# Calculate the leaf_width statistic for each plant
print("Statistics for Leaf Width:")
for plant in plants:
    subset = data[data['plant_name'] == plant]
    mean_width = subset['leaf_width'].mean()  # Mean
    variance_width = subset['leaf_width'].var()  # Variance
    median_width = subset['leaf_width'].median()  # Median
    std_width = subset['leaf_width'].std()  # Standard Deviation
    print(f"{plant}:")
    print(f"  Mean: {mean_width:.2f}")
    print(f"  Variance: {variance_width:.2f}")
    print(f"  Median: {median_width:.2f}")
    print(f"  Standard Deviation: {std_width:.2f}")

# Calculate the leaf_width statistic for all plants combined
mean_width_all = data['leaf_width'].mean()
variance_width_all = data['leaf_width'].var()
median_width_all = data['leaf_width'].median()
std_width_all = data['leaf_width'].std()
print("\nAll Plants (Leaf Width):")
print(f"  Mean: {mean_width_all:.2f}")
print(f"  Variance: {variance_width_all:.2f}")
print(f"  Median: {median_width_all:.2f}")
print(f"  Standard Deviation: {std_width_all:.2f}")

# Calculate the leaf_length statistic for each plant
print("\nStatistics for Leaf Length:")
for plant in plants:
    subset = data[data['plant_name'] == plant]
    mean_length = subset['leaf_length'].mean()  # Mean
    variance_length = subset['leaf_length'].var()  # Variance
    median_length = subset['leaf_length'].median()  # Median
    std_length = subset['leaf_length'].std()  # Standard Deviation
    print(f"{plant}:")
    print(f"  Mean: {mean_length:.2f}")
    print(f"  Variance: {variance_length:.2f}")
    print(f"  Median: {median_length:.2f}")
    print(f"  Standard Deviation: {std_length:.2f}")

# Calculate the leaf_length statistic for all plants combined
mean_length_all = data['leaf_length'].mean()
variance_length_all = data['leaf_length'].var()
median_length_all = data['leaf_length'].median()
std_length_all = data['leaf_length'].std()
print("\nAll Plants (Leaf Length):")
print(f"  Mean: {mean_length_all:.2f}")
print(f"  Variance: {variance_length_all:.2f}")
print(f"  Median: {median_length_all:.2f}")
print(f"  Standard Deviation: {std_length_all:.2f}")

# 5. What can you infer with data and graphs that you have? 
# Detail on my README.md