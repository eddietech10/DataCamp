'''
Subsetting rows with .query():

In this exercise, you will revisit GDP and population data for Australia and Sweden from the World Bank and expand on it using the .query() method. You'll merge the two tables and compute the GDP per capita. Afterwards, you'll use the .query() method to sub-select the rows and create a plot. Recall that you will need to merge on multiple columns in the proper order.

The tables gdp and pop have been loaded for you.
'''



#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Use merge_ordered() on gdp and pop on columns country and date with the fill feature, save to gdp_pop and print.
'''

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method='ffill')

#################################################################

'''
Add a column named gdp_per_capita to gdp_pop that divides gdp by pop.
'''

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

#################################################################

'''
Pivot gdp_pop so values='gdp_per_capita', index='date', and columns='country', save as gdp_pivot.
'''

# Pivot table of gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

#################################################################


'''
Use .query() to select rows from gdp_pivot where date is greater than equal to "1991-01-01". Save as recent_gdp_pop.
'''

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()
