'''
Non-linear model of education
The graph in the previous exercise suggests that the relationship between income and education is non-linear. So let's try fitting a non-linear model.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Add a column named 'educ2' to the gss DataFrame; it should contain the values from 'educ' squared.

Run a regression model that uses 'educ', 'educ2', 'age', and 'age2' to predict 'realinc'.
'''

import statsmodels.formula.api as smf

# Add a new column with educ squared
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Print the estimated parameters
print(results.params)

#################################################################

'''
Excellent. The slope associated with educ2 is positive, so the model curves upward.

<script.py> output:
    Intercept   -23241.884
    educ          -528.309
    educ2          159.967
    age           1696.717
    age2           -17.197
    dtype: float64

https://campus.datacamp.com/courses/exploratory-data-analysis-in-python/multivariate-thinking?ex=6
'''
