# Sea Level Predictor

You will be working on this project with our Gitpod starter code.

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

- **[Python for Everybody Video Course](https://www.youtube.com) (14 hours)**
- **[How to Analyze Data with Python Pandas](https://www.youtube.com) (10 hours)**

## Objective

You will analyze a dataset of the global average sea level change since 1880 and use the data to predict the sea level change through the year 2050.

## Instructions

1. **Load the Dataset:**
   - Use Pandas to import the data from `epa-sea-level.csv`.

2. **Create a Scatter Plot:**
   - Use Matplotlib to create a scatter plot.
   - Set the **Year** column as the x-axis and the **CSIRO Adjusted Sea Level** column as the y-axis.

3. **Plot the First Line of Best Fit:**
   - Use the `linregress` function from `scipy.stats` to calculate the slope and y-intercept of the line of best fit.
   - Plot the line over the scatter plot and extend it to predict sea level rise through the year 2050.

4. **Plot the Second Line of Best Fit:**
   - Filter the data to include only years from 2000 to the most recent year in the dataset.
   - Use `linregress` to calculate the slope and y-intercept for this subset of data.
   - Plot this line over the scatter plot and extend it to predict sea level rise through the year 2050.

5. **Customize the Chart:**
   - Set the x-axis label to **Year**.
   - Set the y-axis label to **Sea Level (inches)**.
   - Add a title: **Rise in Sea Level**.

6. **Save and Return the Chart:**
   - The boilerplate includes commands to save and return the chart as an image.

## Development

Write your code in `sea_level_predictor.py`. For development, you can use `main.py` to test your code.

## Testing

The unit tests for this project are in `test_module.py`. These tests have been imported into `main.py` for your convenience.

## Submitting

Copy your project's URL and submit it to freeCodeCamp.

## Data Source

Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
