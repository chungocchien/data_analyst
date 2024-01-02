import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
    plt.scatter(year, sea_level, marker='o', color='blue', label='CSIRO Adjusted Sea Level')


    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (mm)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    slope_full, intercept_full, _, _, _ = linregress(year, sea_level)

    # Create a range of years from the earliest year to 2050
    years_future = range(min(year), 2051)

    # Predict sea level rise for the years up to 2050 using the full dataset's line of best fit
    sea_level_future_full = [slope_full * year + intercept_full for year in years_future]

    # Plot the line of best fit for the entire dataset
    plt.plot(years_future, sea_level_future_full, color='red', label='Full Dataset Line of Best Fit')

    # Create second line of best fit
    # Filter the data for years from 2000 to the most recent year
    recent_data = df[df['Year'] >= 2000]

    # Extract the filtered 'Year' and 'CSIRO Adjusted Sea Level' columns
    recent_year = recent_data['Year']
    recent_sea_level = recent_data['CSIRO Adjusted Sea Level']

    # Calculate the line of best fit for the recent data
    slope_recent, intercept_recent, _, _, _ = linregress(recent_year, recent_sea_level)

    # Predict sea level rise for the years up to 2050 using the recent data's line of best fit
    sea_level_future_recent = [slope_recent * year + intercept_recent for year in range(2000, 2051)]
    plt.plot(range(2000, 2051), sea_level_future_recent, color='green', label='Recent Data Line of Best Fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()