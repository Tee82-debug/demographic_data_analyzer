Demographic Data Analyzer

This project analyzes demographic data from the U.S. Census dataset to derive insights about education, work hours, salary levels, and occupations in various countries.

Project Overview

The primary goal of this project is to analyze a dataset containing census information and generate useful statistics, including:

Race representation in the dataset
Average age of men
Percentage of individuals with a Bachelor's degree
Relationship between education level and income
Work hours and income analysis
Countries with the highest percentage of high-income earners
Popular occupations in India among high-income earners

Dataset
The dataset used for this analysis is sourced from the U.S. Census data. It includes information on attributes such as:

Age
Work class
Education level
Occupation
Race
Gender
Native country
Hours per week
Salary (more than 50K or not)
Requirements
The project uses Python and several libraries for data manipulation and analysis. Below are the dependencies:

Python 3
pandas: Used for reading and analyzing the data.
numpy: Utilized for numerical operations (if needed).

To install the dependencies, you can run the following command:

pip install pandas numpy

Key Functions

calculate(): This is the core function that processes the dataset and returns a dictionary with the following statistical results:
race_count: Number of individuals of each race.
average_age_men: Average age of men in the dataset.
percentage_bachelors: Percentage of individuals with a Bachelor's degree.
higher_education_rich: Percentage of people with higher education (Bachelors, Masters, Doctorate) earning more than 50K.
lower_education_rich: Percentage of people without higher education earning more than 50K.
min_work_hours: Minimum number of hours a person works per week.
rich_percentage: Percentage of people working the fewest hours who still earn more than 50K.
highest_earning_country: The country with the highest percentage of high-income earners.
highest_earning_country_percentage: The percentage of high-income earners in the top-earning country.
top_IN_occupation: The most popular occupation among high-income earners in India.
