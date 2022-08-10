'''
Jittering
In the previous exercise, the ages fall in columns because they've been rounded into 5-year bins. If we jitter them, the scatter plot will show the relationship more clearly. Recall how Allen jittered height and weight in the video:

height_jitter = height + np.random.normal(0, 2, size=len(brfss))
weight_jitter = weight + np.random.normal(0, 2, size=len(brfss))
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Add random noise to age with mean 0 and standard deviation 2.5.

Make a scatter plot between weight and age with marker size 5 and alpha=0.2. Be sure to also specify 'o'.
'''

# Select the first 1000 respondents
brfss = brfss[:1000]

# Add jittering to age
age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
# Extract weight
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', markersize=5, alpha=0.2)


plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()


#################################################################

'''
Excellent. By smoothing out the ages and avoiding saturation, we get the best view of the data. But in this case the nature of the relationship is still hard to see. In the next lesson, we'll see some other ways to visualize it.
'''
