import pandas as pd
import numpy as np

# Load commute mode share
df_commute = pd.read_csv('data/commute_mode_share_cleaned.csv')

# Load population forecast with annual growth rate
df_pop = pd.read_csv('data/population_forecast.csv')

# Rename for clarity if needed
df_pop = df_pop.rename(columns={'2021_population': 'base_population'})

# Merge on Suburb
df = pd.merge(df_commute, df_pop[['Suburb', 'base_population', 'annual_growth_rate']], on='Suburb')

# Project population to 2035
df['population_2035'] = np.floor(df['base_population'] * ((1 + df['annual_growth_rate']) ** 14)).astype(int)

# Estimate 2035 car commuters
df['car_commuters_2035'] = np.floor(df['population_2035'] * df['pct_commute_by_car']).astype(int)


# Simulation assumptions
mode_shift_rate = 0.15             # 15% switch from car to SRL
avg_trip_distance_km = 12          # Average round-trip distance (can adjust)
emission_factor = 0.192            # kg CO₂ per km (petrol car)

# Mode shift effect
df['commuters_switched'] = np.floor(df['car_commuters_2035'] * mode_shift_rate).astype(int)
df['annual_vkt_reduced'] = df['commuters_switched'] * avg_trip_distance_km * 2 * 5 * 48
df['annual_vkt_without_srl'] = df['car_commuters_2035'] * avg_trip_distance_km * 2 * 5 * 48
df['annual_vkt_with_srl'] = df['annual_vkt_without_srl'] - df['annual_vkt_reduced']
df['co2_saved_tonnes'] = (df['annual_vkt_reduced'] * emission_factor) / 1000
df['co2_saved_tonnes'] = df['co2_saved_tonnes'].round(2)
df['co2_without_srl'] = (df['annual_vkt_without_srl'] * emission_factor) / 1000
df['co2_without_srl'] = df['co2_without_srl'].round(2)
df['co2_with_srl'] = df['co2_without_srl'] - df['co2_saved_tonnes']

# Final output
# Only selected columns in the output
columns_to_keep = [
    'Suburb',
    'population_2035',
    'car_commuters_2035',
    'annual_vkt_without_srl',
    'annual_vkt_with_srl',
    'co2_without_srl',
    'co2_with_srl'
]

# Save clean results to CSV
df[columns_to_keep].to_csv('outputs/srl_simulation_results.csv', index=False)

print(df[['Suburb', 'population_2035', 'car_commuters_2035', 'commuters_switched', 'co2_saved_tonnes']])

print("Simulation results saved to: outputs/srl_simulation_results.csv")
