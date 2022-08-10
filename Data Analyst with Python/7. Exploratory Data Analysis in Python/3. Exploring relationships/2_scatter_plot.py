'''
Scatter plot
Now let's make a scatterplot of weight versus age. To make the code run faster, I've selected only the first 1000 rows from the brfss DataFrame.

weight and age have already been extracted for you. Your job is to use plt.plot() to make a scatter plot.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Make a scatter plot of weight and age with format string 'o' and alpha=0.1.
'''

# Select the first 1000 respondents
brfss = brfss[:1000]

# Extract age and weight
age = brfss['AGE']
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', alpha=0.1)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()
plt.show()

#################################################################

'''
So far so good. By adjusting alpha we can avoid saturating the plot. Next we'll jitter the data to break up the columns.
'''