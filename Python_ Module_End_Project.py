#!/usr/bin/env python
# coding: utf-8

# # Preprocessing

# In[33]:


##importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


# Load the dataset
df = pd.read_csv("C:/Users\edass\Downloads\myexcel.csv.csv")
df


# In[9]:


# Replace the 'height' column with random values between 150 and 180
df["height"] = np.random.randint(150, 181, size=len(df))
df


# In[11]:





# In[12]:


# Display data types of all columns
print(df.dtypes)


# In[13]:


# drop column Height 
df.drop(columns=["Height"], inplace=True)


# In[14]:


print(df.head())


# In[15]:


df.info()


# In[18]:


print(df.shape)


# # 1.  Distribution of employees across each team

# In[19]:


team_distribution = df['Team'].value_counts()


# In[20]:


team_distribution


# In[21]:


team_percentage = (team_distribution / df.shape[0]) * 100


# In[40]:


# Team distribution bar chart
team_distribution.plot(kind='bar')
plt.title('Distribution of Employees Across Teams')
plt.xlabel('Team')
plt.ylabel('Number of Employees')
plt.show()


# In[22]:


team_percentage


# In[ ]:


key insights

Most Represented Team is New Orleans Pelicans which is 4.3 %
Least represented team is Minnesota Timberwolves  which is 2.19%


# # 2. Segregate employees based on their positions

# In[26]:


positions_distribution = df['Position'].value_counts()
positions_distribution


# Key insights
# 
# SG (Shooting Guard) has the highest count (87 employees), meaning this position is the most common in the dataset.
# C (Center) has the lowest count (50 employees), meaning it is the least represented position.
# 

# In[39]:


# Position distribution bar plot
positions_distribution.plot(kind='bar')
plt.title('Distribution of Employees Based on Positions')
plt.xlabel('Position')
plt.ylabel('Number of Employees')
plt.show()


# # 3. Identify the predominant age group

# In[31]:


# Define age group bins
age_groups = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 70], labels=["20-30", "30-40", "40-50", "50-60", "60-70"])

# Count the number of employees in each age group
age_group_counts = age_groups.value_counts()

# Find the predominant (most common) age group
predominant_age_group = age_group_counts.idxmax()

# Display results
print("Age group distribution:")
print(age_group_counts)
print(f"\nThe predominant age group is: {predominant_age_group}")


# In[41]:


# Distribution of employees by age group bar plot
age_groups.value_counts().plot(kind='bar')
plt.title('Distribution of Employees by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.show()


# In[ ]:


Key insights

The 20-30 age group dominates with 284 employees, meaning the workforce is primarily young.
There are only 64 employees in this group, indicating a sharp decline in representation after 30
This suggests that older employees are either not hired or leave before reaching these age ranges.


# # 4. Highest salary expenditure by team and position

# In[32]:


# Group by "team" and sum salaries
team_salary_expenditure = df.groupby("Team")["Salary"].sum()

# Find the team with the highest salary expenditure
highest_salary_team = team_salary_expenditure.idxmax()
highest_salary_team_amount = team_salary_expenditure.max()

# Group by "position" and sum salaries
position_salary_expenditure = df.groupby("Position")["Salary"].sum()

# Find the position with the highest salary expenditure
highest_salary_position = position_salary_expenditure.idxmax()
highest_salary_position_amount = position_salary_expenditure.max()

# Display results
print("Total salary expenditure by team:\n", team_salary_expenditure)
print(f"\nTeam with the highest salary expenditure: {highest_salary_team} (${highest_salary_team_amount})")

print("\nTotal salary expenditure by position:\n", position_salary_expenditure)
print(f"\nPosition with the highest salary expenditure: {highest_salary_position} (${highest_salary_position_amount})")


# In[ ]:





# In[42]:


# Salary expenditure by team bar plot
team_salary_expenditure.plot(kind='bar')
plt.title('Salary Expenditure by Team')
plt.xlabel('Team')
plt.ylabel('Total Salary')
plt.show()

# Salary expenditure by position bar plot
position_salary_expenditure.plot(kind='bar')
plt.title('Salary Expenditure by Position')
plt.xlabel('Position')
plt.ylabel('Total Salary')
plt.show()


# In[ ]:


Key insights

PGs are the highest-paid position ($373.6M) in total salary.
PFs earn $361.3M, making them the second-highest paid position.
Centers earn $283.4M, the lowest of all positions.
SGs ($338.2M) and SFs ($326.3M) are well-paid, but slightly below PGs and PFs


# # 5. Correlation between age and salary

# In[35]:


# Calculate correlation between age and salary
correlation = df["Age"].corr(df["Salary"])

# Display correlation value
print(f"Correlation between Age and Salary: {correlation:.4f}")

# Scatter plot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x=df["Age"], y=df["Salary"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title("Correlation between Age and Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# In[37]:


# Check correlation matrix of all numeric columns
print(df.corr())

# Or visualize with a heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()


# In[ ]:


Key insights

Since 0.16 is close to 0, it suggests that age has little influence on salary.
A positive value means that as age increases, salary tends to increase, but the effect is very weak.
This suggests that other factors (like experience, position, or education) likely play a bigger role in determining salary.

