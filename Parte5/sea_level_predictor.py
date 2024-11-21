import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, label='Best Fit: 1880-2050', color='red')

    recent_data = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = slope2 * x_pred_recent + intercept2
    plt.plot(x_pred_recent, y_pred_recent, label='Best Fit: 2000-2050', color='green')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()
