'''
Transforming variables
When variables have skewed distributions, they often require a transformation in order to form a linear relationship with another variable so that correlation can be computed. In this exercise, you'll perform a transformation yourself.

pandas as pd, numpy as np, matplotlib.pyplot as plt, and seaborn as sns are imported, and world_happiness is loaded.

Keywords:
- log transformation
- scatterplot
- correlation coefficient
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Create a scatterplot of happiness_score versus gdp_per_cap and calculate the correlation between them.
'''

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print(cor)

'''
<script.py> output:
    0.727973301222298
'''

#################################################################

'''
Add a new column to world_happiness called log_gdp_per_cap that contains the log of gdp_per_cap.
Create a seaborn scatterplot of log_gdp_per_cap and happiness_score and calculate the correlation between them.
'''

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of log_gdp_per_cap and happiness_score
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

'''
<script.py> output:
    0.8043146004918288
'''

#################################################################
#################################################################
#################################################################

'''
Terrific transforming! The relationship between GDP per capita and happiness became more linear by applying a log transformation. Log transformations are great to use on variables with a skewed distribution, such as GDP.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/correlation-and-experimental-design-4?ex=6
'''
