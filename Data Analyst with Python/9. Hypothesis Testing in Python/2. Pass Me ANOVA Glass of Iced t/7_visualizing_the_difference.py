'''
Visualizing the difference
Before you start running hypothesis tests, it's a great idea to perform some exploratory data analysis; that is, calculating summary statistics and visualizing distributions.

Here, you'll look at the proportion of county-level votes for the Democratic candidate in 2012 and 2016, sample_dem_data. Since the counties are the same in both years, these samples are paired. The columns containing the samples are dem_percent_12 and dem_percent_16.

dem_votes_potus_12_16 is available as sample_dem_data. pandas and matplotlib.pyplot are loaded with their usual aliases.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Create a new diff column containing the percentage of votes for the democratic candidate in 2012 minus the percentage of votes for the democratic candidate in 2016.
'''

# Calculate the differences from 2012 to 2016:
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Print sample_dem_data
print(f'sample_dem_data:\n {sample_dem_data}')

#################################################################

'''
Calculate the mean of the diff column as xbar_diff:
'''
# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Print xbar_diff
print(f'xbar_diff: {xbar_diff}')


#################################################################
'''
Calculate the standard deviation of the diff column as s_diff.
'''

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Print s_diff
print(f's_diff: {s_diff}')

#################################################################

'''
Plot a histogram of the diff column with 20 bins:
'''

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins=20)
plt.show()



#################################################################
#################################################################
#################################################################

'''
Delightful difference discovery! Notice that the majority of the histogram lies to the right of zero.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=10
'''
