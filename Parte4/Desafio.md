# Page View Time Series Visualizer

You will be working on this project with our Gitpod starter code.

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

- **[Python for Everybody Video Course](https://www.youtube.com) (14 hours)**
- **[How to Analyze Data with Python Pandas](https://www.youtube.com) (10 hours)**

For this project, you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

## Instructions

Use the data to complete the following tasks:

1. Use Pandas to import the data from `fcc-forum-pageviews.csv`. Set the index to the date column.
2. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
3. Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to `examples/Figure_1.png`. 
   - The title should be **Daily freeCodeCamp Forum Page Views 5/2016-12/2019**.
   - The label on the x-axis should be **Date** and the label on the y-axis should be **Page Views**.
4. Create a `draw_bar_plot` function that draws a bar chart similar to `examples/Figure_2.png`.
   - It should show average daily page views for each month grouped by year.
   - The legend should show month labels and have a title of **Months**.
   - On the chart, the label on the x-axis should be **Years** and the label on the y-axis should be **Average Page Views**.
5. Create a `draw_box_plot` function that uses Seaborn to draw two adjacent box plots similar to `examples/Figure_3.png`. 
   - These box plots should show how the values are distributed within a given year or month and how it compares over time.
   - The title of the first chart should be **Year-wise Box Plot (Trend)** and the title of the second chart should be **Month-wise Box Plot (Seasonality)**.
   - Make sure the month labels on the bottom start at **Jan**, and the x and y axes are labeled correctly.
6. For each chart, make sure to use a copy of the data frame.

The boilerplate includes commands to prepare the data and save and return the images.

## Development

Write your code in `time_series_visualizer.py`. For development, you can use `main.py` to test your code.

## Testing

The unit tests for this project are in `test_module.py`. These tests have been imported into `main.py` for your convenience.

## Submitting

Copy your project's URL and submit it to freeCodeCamp.
