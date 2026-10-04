# Student Performance Prediction

A machine learning project that predicts students' final grades (`G3`) using student-related academic and behavioral features.

## Project Overview

This project uses **Linear Regression** to predict a student's final grade based on selected features such as study time, previous failures, educational support, social factors, health, absences, and previous grades.

The project was created as a practical exercise to reinforce regression concepts and practice the complete machine learning workflow.

## Dataset

The dataset contains information about students, including:

* Study time
* Previous failures
* School and family support
* Extra paid classes
* Extracurricular activities
* Desire for higher education
* Internet access
* Family relationship quality
* Free time
* Going out with friends
* Health
* Absences
* First-period grade (`G1`)
* Second-period grade (`G2`)
* Final grade (`G3`)

## Features Used

The model uses the following features:

* `studytime`
* `failures`
* `schoolsup`
* `famsup`
* `paid`
* `activities`
* `higher`
* `internet`
* `famrel`
* `freetime`
* `goout`
* `health`
* `absences`
* `G1`
* `G2`

### Target

`G3` — Final student grade.

## Data Preprocessing

The dataset was prepared before training:

* Removed selected columns that were not used for this project.
* Converted binary categorical values such as `yes/no` into numerical values (`1/0`).
* Converted other categorical values into numerical representations.
* Checked the feature data types.
* Checked for missing values.
* Split the dataset into training and testing sets.

## Machine Learning Model

**Linear Regression** was used because the target variable (`G3`) is a continuous numerical value, making this a regression problem.

The data was split using:

* 70% Training data
* 30% Testing data
* `random_state = 23`

## Evaluation Metrics

The model was evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R-squared (R²)

## Results

| Metric | Result |
| ------ | -----: |
| MAE    |  1.309 |
| MSE    |  4.857 |
| R²     |  0.781 |

### Interpretation

* **MAE = 1.309:** The model's predictions were, on average, about 1.31 grade points away from the actual final grade.
* **MSE = 4.857:** Represents the average squared prediction error.
* **R² = 0.781:** The model explains approximately 78.1% of the variance in the test-set target values.

## Important Note

`G1` and `G2` are included as input features when predicting `G3`. Since these grades are previous-period grades and are closely related to the final grade, they provide strong predictive information.

Therefore, the reported performance should not be interpreted as predicting the final grade without knowing previous grades.

## Technologies

* Python
* Pandas
* Scikit-learn

## Project Structure

```text
Student-Performance-Prediction/
│
├── student_data.csv
├── code.py
└── README.md
```

## What I Practiced

Through this project, I practiced:

* Data loading with Pandas
* Data cleaning
* Feature selection
* Categorical data encoding
* Checking data types
* Checking missing values
* Train/test splitting
* Linear Regression
* Making predictions
* Regression evaluation metrics
* MAE
* MSE
* R²

## Future Improvements

Possible future improvements include:

* Comparing Linear Regression with other regression algorithms.
* Testing the model without `G1` and `G2`.
* Exploring feature importance and feature relationships.
* Applying more advanced preprocessing techniques.
* Comparing different models using the same evaluation metrics.
