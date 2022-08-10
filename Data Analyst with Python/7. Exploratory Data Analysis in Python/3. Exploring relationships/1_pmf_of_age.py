'''
PMF of age
Do people tend to gain weight as they get older? We can answer this question by visualizing the relationship between weight and age. But before we make a scatter plot, it is a good idea to visualize distributions one variable at a time. Here, you'll visualize age using a bar chart first. Recall that all PMF objects have a .bar() method to make a bar chart.

The BRFSS dataset includes a variable, 'AGE' (note the capitalization!), which represents each respondent's age. To protect respondents' privacy, ages are rounded off into 5-year bins. 'AGE' contains the midpoint of the bins.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Extract the variable 'AGE' from the DataFrame brfss and assign it to age.

Get the PMF of age and plot it as a bar chart.
'''

# Extract age
age = brfss['AGE']

# Plot the PMF
pmf_age = Pmf(age)
pmf_age.bar(label=pmf_age)

# Label the axes
plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()


#################################################################

'''
Ok, we're off to a good start. Notice that the last age range is bigger than the others. That's the kind of thing you see when you plot distributions.
'''