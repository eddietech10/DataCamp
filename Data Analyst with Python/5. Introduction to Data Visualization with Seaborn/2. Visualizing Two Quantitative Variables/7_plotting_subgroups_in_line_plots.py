'''
Plotting subgroups in line plots
Let's continue to look at the mpg dataset. We've seen that the average miles per gallon for cars has increased over time, but how has the average horsepower for cars changed over time? And does this trend differ by country of origin?
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line',
ci=None)

# Show plot
plt.show()

#################################################################

'''
Create different lines for each country of origin ("origin") that vary in both line style and color.
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None,
            hue='origin',
            style='origin')

# Show plot
plt.show()


#################################################################

'''
Add markers for each data point to the lines.

Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for each line.
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year",
            y="horsepower",
            data=mpg,   
            kind="line", 
            ci=None,
            style="origin", 
            hue="origin",
            markers=True,
            dashes=False)

# Show plot
plt.show()

