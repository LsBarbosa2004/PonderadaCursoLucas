import pandas as pd

def demographic_data_analyzer():
    #Questões: 
    # 1: How many people of each race are represented in this dataset?
    # 2: What is the average age of men?
    # 3: What is the percentage of people who have a Bachelor's degree?
    # 4: What percentage of people with advanced education make more than 50K?
    # 5: What percentage of people without advanced education make more than 50K?
    # 6: What is the minimum number of hours a person works per week?
    # 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    # 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    # 9: Identify the most popular occupation for those who earn >50K in India.
    
    df = pd.read_csv('adult.data.csv', header=None, delimiter=',', names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
        'occupation', 'relationship', 'race', 'sex', 'capital-gain',
        'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ])
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')
    df.dropna(inplace=True)
    
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100, 1)
    lower_education_rich = round((df[~advanced_education & (df['salary'] == '>50K')].shape[0] / df[~advanced_education].shape[0]) * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    min_hours_workers = df['hours-per-week'] == min_work_hours
    rich_percentage = round((df[min_hours_workers & (df['salary'] == '>50K')].shape[0] / df[min_hours_workers].shape[0]) * 100, 1)
    countries_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries_total = df['native-country'].value_counts()
    country_percentages = (countries_salary / countries_total * 100).dropna()
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = india_occupation.mode()[0]
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    results = demographic_data_analyzer()
    for key, value in results.items():
        print(f"{key}: {value}")
