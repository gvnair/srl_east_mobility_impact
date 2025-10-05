SRL East Mobility Impact_east
This project models the projected impact of Melbourne’s Suburban Rail Loop East (SRL East) on reducing car usage and vehicle emissions by 2035. Using publicly available data and Python-based simulations, it estimates the shift in commuter behaviour and the resulting sustainability benefits.

## 📊 Key Features

- Population growth forecasting using ABS Census data  
- Mode share estimation for suburban commuting patterns  
- Simulation of modal shift from car to rail (15% assumption)  
- Calculation of reductions in vehicle kilometres travelled (VKT)  
- Estimation of CO₂ emissions saved with SRL East  
- Comparison between 'with SRL' and 'without SRL' scenarios  
- Visualisation of results via bar and stacked charts  

## 🛠 Tools Used

- Python 3  
- pandas, numpy  
- matplotlib  
- ABS TableBuilder  
- Git & GitHub  

## 📁 Project Structure
data/ # Cleaned and source datasets (commute modes, population)
scripts/ # Python scripts for simulation and visualisation
outputs/ # Charts and CSV outputs from simulation
README.md # This file

## 🧠 Assumptions

- 15% of 2035 car commuters in SRL East suburbs will switch to rail  
- Average round-trip commute distance is 12 km  
- Emission factor: 0.192 kg CO₂/km for petrol cars  
- Working days per year: 240 (48 weeks × 5 days)  

## 📍 Target Suburbs

Suburbs analysed include Clayton, Box Hill, Glen Waverley, and surrounding SA2 areas affected by SRL East.

## 🔗 Author

This project was developed independently by Gokul Nair in 2025 as part of a data analytics portfolio.
