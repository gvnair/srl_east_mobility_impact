import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned commute data
df = pd.read_csv('data/cleaned_commute_data.csv')

# Calculate % mode share per suburb
df['Car'] = df['Car_driver'] / df['Total_commuters']
df['Train'] = df['Train'] / df['Total_commuters']
df['Tram'] = df['Tram/light_rail'] / df['Total_commuters']
df['Bus'] = df['Bus'] / df['Total_commuters']
df['Walked'] = df['Walked'] / df['Total_commuters']

# List of modes and colours
modes = ['Car', 'Train', 'Tram','Bus', 'Walked']
colours = ['#4CAF50', '#2196F3','#DB09D4','#FF9800', '#9E9E9E']

# Setup plot
plt.figure(figsize=(10, 6))
bottom_vals = [0] * len(df)

# Plot each mode as a stacked bar
for i, mode in enumerate(modes):
    plt.bar(df['Suburb'], df[mode], bottom=bottom_vals, label=mode, color=colours[i])
    bottom_vals = [a + b for a, b in zip(bottom_vals, df[mode])]

# Format
plt.ylabel('Proportion of Commuters')
plt.title('Proportion of Modes of Transportation by Suburb (2021 Census)')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.legend(title="Mode of Transport")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Save and show
plt.savefig('outputs/commute_mode_proportions_stacked.png')
plt.show()
