'''
Plot a PMF
Now let's plot a PMF for the age of the respondents in the GSS dataset. The variable 'age' contains respondents' age in years.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Select the 'age' column from the gss DataFrame and store the result in age.
'''

# Select the age column
age = gss['age']

#################################################################

'''
Make a normalized PMF of age. Store the result in pmf_age.
'''

# Make a PMF of age
pmf_age = Pmf(age)


#################################################################

'''
Plot pmf_age as a bar chart.
'''

# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

# Plot the PMF
pmf_age.bar(label=pmf_age)

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()
