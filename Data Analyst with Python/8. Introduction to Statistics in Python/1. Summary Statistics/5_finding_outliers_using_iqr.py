'''
Finding outliers using IQR
Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than Q1−1.5×IQR or greater than Q3+1.5×IQR, it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.

Diagram of a box plot showing median, quartiles, and outliers
https://assets.datacamp.com/production/repositories/5758/datasets/ca7e6e1832be7ec1842f62891815a9b0488efa83/Screen%20Shot%202020-04-28%20at%2010.04.54%20AM.png

In this exercise, you'll calculate IQR and use it to find some outliers. pandas as pd and numpy as np are loaded and food_consumption is available.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission. Store the resulting DataFrame as emissions_by_country.
'''

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

print(emissions_by_country)

#################################################################

'''
Compute the first and third quartiles of emissions_by_country and store these as q1 and q3.

Calculate the interquartile range of emissions_by_country and store it as iqr.
'''

from scipy.stats import iqr

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
# iqr = iqr(emissions_by_country)
iqr = np.quantile(emissions_by_country, 0.75) - np.quantile(emissions_by_country, 0.25)

#################################################################

'''
Calculate the lower and upper cutoffs for outliers of emissions_by_country, and store these as lower and upper.
'''

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - (1.5 * iqr)
upper = q3 + (1.5 * iqr)

#################################################################

'''
Subset emissions_by_country to get countries with a total emission greater than the upper cutoff or a total emission less than the lower cutoff.
'''

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)

'''
<script.py> output:
    country
    Argentina    2172.4
    Name: co2_emission, dtype: float64
'''

#################################################################
#################################################################
#################################################################

'''
Outstanding outlier detection! It looks like Argentina has a substantially higher amount of CO2 emissions per person than other countries in the world.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/summary-statistics-1?ex=10
'''
