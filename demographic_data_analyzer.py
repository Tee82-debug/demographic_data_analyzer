import pandas as pd

def calculate(print_data=True):
    column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
    'hours_per_week', 'native_country', 'salary'
    ]

    df = pd.read_csv('/Users/a1/Downloads/adult/adult_data.csv', names= column_names, skipinitialspace=True)

    # Question 1: How many people of each race are represented in this dataset?

    race_count = df['race'].value_counts()


    # Question 2: What is the average age of men

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)


    # Question 3: What is the percentage of people who have a Bachelor's degree'

    total_people = len(df)

    percentage_bachelors = round((df[df['education']== 'Bachelors'].shape[0] / len(df)) * 100, 1)

    #percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)



    # Question 4:What percentage of people with advanced education (Bachelor, Masters, or Dectorate) make more than 50k

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100 , 1)
    lower_education_rich = round((lower_education[lower_education['salary']== '>50K'].shape[0]) * 100, 1)




    # # Question 5: What is the minimum number of hours a person works per week?

    min_work_hours = df['hours_per_week'].min()


    # # Question 6: What is the minimum number of hours a person works per week have a salary of more than 50k?
    min_work_hours = df['hours_per_week'].min()
    num_min_workers = df[df['hours_per_week'] == min_work_hours]
    percentage_rich = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)



    # Question 7: What country has the highest percentage of people that earn >50k, and what is the percentage

    rich_countries =  df[df['salary'] == '>50K']['native_country'].value_counts()
    total_countries = df['native_country'].value_counts()


    # # Percentage of rich people in each country 
    rich_percentage_by_country = (rich_countries / total_countries) * 100
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max(), 1)


    # Question 8: identify the most popular occupation for those who earn >50k in India.

    india_occupations = df[(df['native_country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_in_occupation = india_occupations.value_counts().idxmax()


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {percentage_rich}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_in_occupation)


    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'percentage_rich': percentage_rich,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_in_occupation 
        }
