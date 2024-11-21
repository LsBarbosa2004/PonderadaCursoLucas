# Medical Data Visualizer

You will be working on this project with our Gitpod starter code.

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

- **[Python for Everybody Video Course](https://www.youtube.com) (14 hours)**
- **[How to Analyze Data with Python Pandas](https://www.youtube.com) (10 hours)**

In this project, you will visualize and make calculations from medical examination data using `matplotlib`, `seaborn`, and `pandas`. The dataset values were collected during medical examinations.

## Data Description

The rows in the dataset represent patients, and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

**File name:** `medical_examination.csv`

| Feature                        | Variable Type         | Variable      | Value Type                        |
|--------------------------------|-----------------------|---------------|-----------------------------------|
| Age                            | Objective Feature     | age           | int (days)                        |
| Height                         | Objective Feature     | height        | int (cm)                          |
| Weight                         | Objective Feature     | weight        | float (kg)                        |
| Gender                         | Objective Feature     | gender        | categorical code                  |
| Systolic blood pressure        | Examination Feature   | ap_hi         | int                               |
| Diastolic blood pressure       | Examination Feature   | ap_lo         | int                               |
| Cholesterol                    | Examination Feature   | cholesterol   | 1: normal, 2: above normal, 3: well above normal |
| Glucose                        | Examination Feature   | gluc          | 1: normal, 2: above normal, 3: well above normal |
| Smoking                        | Subjective Feature    | smoke         | binary                            |
| Alcohol intake                 | Subjective Feature    | alco          | binary                            |
| Physical activity              | Subjective Feature    | active        | binary                            |
| Presence or absence of cardiovascular disease | Target Variable | cardio        | binary                            |

## Instructions

Create a chart similar to `examples/Figure_1.png`, where we show the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with `cardio=1` and `cardio=0` in different panels.

1. **Import the data** from `medical_examination.csv` and assign it to the `df` variable.
2. **Add an `overweight` column** to the data. To determine if a person is overweight:
   - Calculate BMI: `weight (kg) / height (m)^2`.
   - If BMI > 25, the person is overweight (value `1`), otherwise not (value `0`).
3. **Normalize data**:
   - Make `0` always good and `1` always bad.
   - For `cholesterol` and `gluc`: if the value is `1`, set it to `0`. If the value is more than `1`, set it to `1`.
4. **Draw the Categorical Plot** in the `draw_cat_plot` function:
   - Create a DataFrame for the categorical plot using `pd.melt` with values from `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight` in the `df_cat` variable.
   - Group and reformat the data in `df_cat` to split it by `cardio`. Show the counts of each feature.
   - Rename one of the columns for the categorical plot to work correctly.
   - Convert the data into long format and create a chart showing the value counts of the categorical features using `sns.catplot()`.
   - Store the figure in the `fig` variable.
5. **Draw the Heat Map** in the `draw_heat_map` function:
   - Clean the data in the `df_heat` variable by filtering out incorrect data:
     - `ap_lo` <= `ap_hi`
     - `height` is within the 2.5th and 97.5th percentiles.
     - `weight` is within the 2.5th and 97.5th percentiles.
   - Calculate the correlation matrix and store it in the `corr` variable.
   - Generate a mask for the upper triangle and store it in the `mask` variable.
   - Set up the `matplotlib` figure and plot the correlation matrix using `sns.heatmap()`.
6. Store the resulting figures for both plots.

## Development

Write your code in `medical_data_visualizer.py`. For development, you can use `main.py` to test your code.

## Testing

The unit tests for this project are in `test_module.py`. These tests have been imported into `main.py` for your convenience.

## Submitting

Copy your project's URL and submit it to freeCodeCamp.
