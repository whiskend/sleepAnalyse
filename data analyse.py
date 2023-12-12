import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the provided CSV file
file_path = './Sleep.csv'
sleep_data = pd.read_csv(file_path)

# Grouping the data by 'Sleep Duration' and calculating the required statistics
grouped_data = sleep_data.groupby('Sleep Duration').agg({
    'Stress Level': ['mean', 'min', 'max', 'std'],
    'Quality of Sleep': ['mean', 'min', 'max', 'std'],
    'Physical Activity Level': ['mean', 'min', 'max', 'std'],
    'Age': ['min', 'max']  # Including Age min and max
})

# Displaying the full summary statistics for each 'Sleep Duration' group
print(grouped_data)

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Creating a figure with 2x2 subplots (axes)
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Plotting and filling the area between 'max' and 'min' for each statistic
# Stress Level
axes[0, 0].plot(grouped_data['Stress Level']['mean'], label='Mean', color='blue')
axes[0, 0].plot(grouped_data['Stress Level']['min'], label='Min', color='green')
axes[0, 0].plot(grouped_data['Stress Level']['max'], label='Max', color='red')
axes[0, 0].fill_between(grouped_data.index, grouped_data['Stress Level']['min'], grouped_data['Stress Level']['max'], color='skyblue', alpha=0.3)
axes[0, 0].set_title('Stress Level Statistics by Sleep Duration')
axes[0, 0].set_ylabel('Stress Level')

# Quality of Sleep
axes[0, 1].plot(grouped_data['Quality of Sleep']['mean'], label='Mean', color='blue')
axes[0, 1].plot(grouped_data['Quality of Sleep']['min'], label='Min', color='green')
axes[0, 1].plot(grouped_data['Quality of Sleep']['max'], label='Max', color='red')
axes[0, 1].fill_between(grouped_data.index, grouped_data['Quality of Sleep']['min'], grouped_data['Quality of Sleep']['max'], color='skyblue', alpha=0.3)
axes[0, 1].set_title('Quality of Sleep Statistics by Sleep Duration')
axes[0, 1].set_ylabel('Quality of Sleep')

# Physical Activity Level
axes[1, 0].plot(grouped_data['Physical Activity Level']['mean'], label='Mean', color='blue')
axes[1, 0].plot(grouped_data['Physical Activity Level']['min'], label='Min', color='green')
axes[1, 0].plot(grouped_data['Physical Activity Level']['max'], label='Max', color='red')
axes[1, 0].fill_between(grouped_data.index, grouped_data['Physical Activity Level']['min'], grouped_data['Physical Activity Level']['max'], color='skyblue', alpha=0.3)
axes[1, 0].set_title('Physical Activity Level Statistics by Sleep Duration')
axes[1, 0].set_ylabel('Physical Activity Level')

# Age Range
axes[1, 1].plot(grouped_data['Age']['min'], label='Min Age', color='green')
axes[1, 1].plot(grouped_data['Age']['max'], label='Max Age', color='red')
axes[1, 1].fill_between(grouped_data.index, grouped_data['Age']['min'], grouped_data['Age']['max'], color='skyblue', alpha=0.3)
axes[1, 1].set_title('Age Range by Sleep Duration')
axes[1, 1].set_ylabel('Age')
axes[1, 1].set_xlabel('Sleep Duration (hours)')

# Adding legends and adjusting the layout for better readability
for ax in axes.flat:
    ax.legend()

plt.tight_layout()
plt.show()

# Calculating the mean of the standard deviations for Stress Level, Quality of Sleep, and Physical Activity Level
std_data = {
    'Stress Level': grouped_data['Stress Level', 'std'].mean(),
    'Quality of Sleep': grouped_data['Quality of Sleep', 'std'].mean(),
    'Physical Activity Level': grouped_data['Physical Activity Level', 'std'].mean()
}

# Creating a DataFrame for plotting
std_df = pd.DataFrame(list(std_data.items()), columns=['Variable', 'Average Std Dev'])

# Plotting the average standard deviation as a bar graph
plt.figure(figsize=(8, 6))
sns.barplot(x='Variable', y='Average Std Dev', data=std_df, palette='viridis')
plt.title('Average Standard Deviation of Stress Level, Quality of Sleep, and Physical Activity Level')
plt.ylabel('Average Standard Deviation')
plt.show()
