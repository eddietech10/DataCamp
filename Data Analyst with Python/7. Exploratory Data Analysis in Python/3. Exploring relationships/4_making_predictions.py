'''
Making predictions
At this point, we have a model that predicts income using age, education, and sex.

Let's see what it predicts for different levels of education, holding age constant.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Using np.linspace(), add a variable named 'educ' to df with a range of values from 0 to 20.

Add a variable named 'age' with the constant value 30.

Use df to generate predicted income as a function of education.
'''

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0,20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())

#################################################################

'''
Nice job. Now let's see what the results look like.

<script.py> output:
    0    12182.345
    1    11993.359
    2    11857.672
    3    11775.286
    4    11746.199
    dtype: float64

https://campus.datacamp.com/courses/exploratory-data-analysis-in-python/multivariate-thinking?ex=8
'''
