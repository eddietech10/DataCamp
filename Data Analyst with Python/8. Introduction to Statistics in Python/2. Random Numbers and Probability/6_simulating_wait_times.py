'''
Simulating wait times
To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram to show him what he should expect. Recall from the last exercise that his minimum wait time is 0 minutes and his maximum wait time is 30 minutes.

As usual, pandas as pd, numpy as np, and matplotlib.pyplot as plt are loaded.

Keywords:
- Random number generation
- uniform distribution
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Set the random seed to 334.
'''

# Set random seed to 334
np.random.seed(334)

#################################################################

'''
Import uniform from scipy.stats.
'''

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

#################################################################

'''
Generate 1000 wait times from the continuous uniform distribution that models Amir's wait time. Save this as wait_times.
'''

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

print(wait_times)

#################################################################

'''
Create a histogram of the simulated wait times and show the plot.
'''

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times, label='Wait time')
plt.xlabel('Backup time')
plt.ylabel('Wait time')
plt.show()

#################################################################
#################################################################
#################################################################

'''
Superb simulating! Unless Amir figures out exactly what time each backup happens, he won't be able to time his data entry so it gets backed up sooner, but it looks like he'll wait about 15 minutes on average.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/random-numbers-and-probability-2?ex=12
'''
