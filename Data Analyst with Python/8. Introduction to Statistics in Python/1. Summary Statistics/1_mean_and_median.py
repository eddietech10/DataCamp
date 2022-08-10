'''
Mean and median
In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. The food_consumption dataset contains information about the kilograms of food consumed per person per year in each country in each food category (consumption) as well as information about the carbon footprint of that food category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.

In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.

pandas is imported as pd for you and food_consumption is pre-loaded.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Import numpy with the alias np.

Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that holds rows for 'USA'. Call these be_consumption and usa_consumption.

Calculate the mean and median of kilograms of food consumed per person per year for both countries.
'''

# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

'''
<script.py> output:
    42.13272727272727
    12.59
    44.650000000000006
    14.58
'''

#################################################################

'''
Subset food_consumption for rows with data about Belgium and the USA.

Group the subsetted data by country and select only the consumption column.

Calculate the mean and median of the kilograms of food consumed per person per year in each country using .agg().
'''

# Import numpy as np
import numpy as np

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') | (food_consumption['country'] == 'USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))

#################################################################
#################################################################
#################################################################

'''
###_____________________... IMPORTANT ...______________________###
Marvelous mean and median calculation! When you want to compare summary statistics between groups, it's much easier to use .groupby() and .agg() instead of subsetting and calling the same functions multiple times.

<script.py> output:
               mean  median
    country                
    Belgium  42.133   12.59
    USA      44.650   14.58

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/summary-statistics-1?ex=5
'''
