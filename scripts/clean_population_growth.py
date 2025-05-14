import pandas as pd

# Load both CSVs (adjust file paths as needed)
df_2021 = pd.read_csv('data/2021_population_srl_suburbs.csv')
df_2016 = pd.read_csv('data/2016_population_srl_suburbs.csv')

# Merge on 'Suburb'
df = pd.merge(df_2016[['Suburb','2016_population']], df_2021[['Suburb','2021_population']], on='Suburb')

# Calculate annual growth rate
def calculate_growth(p2016, p2021, years=5):
    return (p2021 / p2016) ** (1 / years) - 1

# Apply the function row-wise
df['annual_growth_rate'] = df.apply(lambda row: calculate_growth(row['2016_population'], row['2021_population']), axis=1
)

# Preview and save
print(df)
df.to_csv('data/population_forecast.csv', index=False)
