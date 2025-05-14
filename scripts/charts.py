import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your simulation results
df = pd.read_csv('outputs/srl_simulation_results.csv')

# Set up bar chart indices
x = np.arange(len(df['Suburb']))  # number of suburbs
bar_width = 0.35

# Bar chart for CO₂ emissions with vs. without SRL
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width/2, df['co2_without_srl'], width=bar_width, label='Without SRL', color='lightgray')
plt.bar(x + bar_width/2, df['co2_with_srl'], width=bar_width, label='With SRL', color='mediumseagreen')
plt.xticks(x, df['Suburb'], rotation=45)
plt.ylabel('Tonnes of CO₂ Emitted')
plt.title('Total CO₂ Emissions in 2035: With vs Without SRL East')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/co2_total_comparison.png')
plt.show()

# Bar chart for CO₂ emissions with vs. without SRL
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width/2, df['annual_vkt_without_srl'], width=bar_width, label='Without SRL', color='lightgray')
plt.bar(x + bar_width/2, df['annual_vkt_with_srl'], width=bar_width, label='With SRL', color='mediumseagreen')
plt.xticks(x, df['Suburb'], rotation=45)
plt.ylabel('Annual Vehicle Kilometres Traveled (millions)')
plt.title('Total VKT in 2035: With vs Without SRL East')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/vkt_total_comparison.png')
plt.show()
