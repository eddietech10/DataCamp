'''
Make a PMF
The GSS dataset has been pre-loaded for you into a DataFrame called gss. You can explore it in the IPython Shell to get familiar with it.

In this exercise, you'll focus on one variable in this dataset, 'year', which represents the year each respondent was interviewed.

The Pmf class you saw in the video has already been created for you. You can access it outside of DataCamp via the empiricaldist library.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Make a PMF for year with normalize=False and display the result.
'''

# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)

# Print the result
print(pmf_year)

#################################################################

# Question
# How many respondents were interviewed in 2016?

# Possible Answers

test = gss['year'] == 2016
test.sum()

# => 2867

1613

2538

0.045897

