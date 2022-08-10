'''
Mean vs. median
In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.

pandas is loaded as pd, numpy is loaded as np, and food_consumption is available.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Import matplotlib.pyplot with the alias plt.

Subset food_consumption to get the rows where food_category is 'rice'.

Create a histogram of co2_emission for rice and show the plot.
'''

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'].dropna(), label='co2_emission for rice')

plt.xlabel('co2_emission values')
plt.ylabel('count')
plt.show()

#################################################################

'''
Question
Take a look at the histogram you just created of different countries' CO2 emissions for rice. Which of the following terms best describes the shape of the data?

Possible Answers

No skew

Left-skewed

==> Right-skewed
'''



#################################################################

'''
Use .agg() to calculate the mean and median of co2_emission for rice.
'''

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption.agg([np.mean, np.median]))

'''
<script.py> output:
            Unnamed: 0  consumption  co2_emission
    mean         718.5       29.375        37.592
    median       718.5       11.875        15.200
'''

#################################################################

'''
Question
Given the skew of this data, what measure of central tendency best summarizes the kilograms of CO2 emissions per person per year for rice?

Possible Answers

Mean

==> Median

Both mean and median
'''



#################################################################
#################################################################
#################################################################

'''
Great work! The mean is substantially higher than the median since it's being pulled up by the high values over 100 kg/person/year.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/summary-statistics-1?ex=6
'''
