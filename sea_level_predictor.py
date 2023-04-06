import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  # Create scatter plot
  plt.subplots(figsize=(15, 15))
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.xlim(df['Year'][0], 2050)
  plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
  
  # Create first line of best fit
  m, c, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x = np.arange(df['Year'][0], 2051)
  plt.plot(x, m * x + c, color='red')

  # Create second line of best fit
  m, c, _, _, _ = linregress(
    df.loc[df['Year'] >= 2000]['Year'],
    df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
  x = np.arange(2000, 2051)
  plt.plot(x, m * x + c, color='purple')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
