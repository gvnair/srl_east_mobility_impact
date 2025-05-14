import pandas as pd

# Load your cleaned data
df = pd.read_csv('data/cleaned_commute_data.csv')

# Calculate % of commuters using each mode
df['pct_commute_by_car'] = df['Car_driver'] / df['Total_commuters']
df['pct_commute_by_bus'] = df['Bus'] / df['Total_commuters']
df['pct_commute_by_train'] = df['Train'] / df['Total_commuters']
df['pct_commute_by_bike'] = df['Bicycle'] / df['Total_commuters']
df['pct_commute_by_walk'] = df['Walked'] / df['Total_commuters']
df['pct_commute_by_tram/light_rail'] = df['Tram/light_rail'] / df['Total_commuters']
# Show a preview
print(df[['Suburb', 'pct_commute_by_car']])

df.to_csv('data/commute_mode_share_cleaned.csv', index=False)