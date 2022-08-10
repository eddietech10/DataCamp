'''
Visualizing predictions
Now let's visualize the results from the previous exercise!
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Plot mean_income_by_educ using circles ('o'). Specify an alpha of 0.5.

Plot the prediction results with a line, with df['educ'] on the x-axis and pred on the y-axis.
'''

# Plot mean income in each age group
plt.clf() # The clf() function in pyplot module of matplotlib library is used to clear the current figure. Syntax: matplotlib.pyplot.clf().

grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ, 'o', alpha=0.5)

# Plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()

#################################################################

'''
Looks like this model captures the relationship pretty well. Nice job.

https://campus.datacamp.com/courses/exploratory-data-analysis-in-python/multivariate-thinking?ex=9
'''
