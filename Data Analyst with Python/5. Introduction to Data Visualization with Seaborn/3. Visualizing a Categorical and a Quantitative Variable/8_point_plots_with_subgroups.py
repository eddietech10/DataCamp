'''
Point plots with subgroups
Let's continue exploring the dataset of students in secondary school. This time, we'll ask the question: is being in a romantic relationship associated with higher or lower school attendance? And does this association differ by which school the students attend? Let's find out using a point plot.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################


'''
Use sns.catplot() and the student_data DataFrame to create a point plot with relationship status ("romantic") on the x-axis and number of absences ("absences") on the y-axis. Color the points based on the school that they attend ("school").
'''

# Create a point plot that uses color to create subgroups
sns.catplot(x='romantic', y='absences', data=student_data, hue='school', kind='point')


# Show plot
plt.show()

#################################################################

'''
Turn off the confidence intervals for the plot.
'''

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()


#################################################################


'''
Since there may be outliers of students with many absences, use the median function that we've imported from numpy to display the median number of absences instead of the averag
'''

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()
