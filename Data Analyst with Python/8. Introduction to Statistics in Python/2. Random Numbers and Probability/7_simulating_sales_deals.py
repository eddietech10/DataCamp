'''
Simulating sales deals
Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on. Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals so he can better understand his performance.

numpy is imported as np.

Keywords:
- binom.rsv()
- binom.pmf()
- binom.cdf()
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Import binom from scipy.stats and set the random seed to 10.
'''

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

#################################################################

'''
Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on.
'''

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))

#################################################################

'''
Simulate a typical week of Amir's deals, or one week of 3 deals.
'''

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 1 week of 3 deals
print(binom.rvs(3, 0.3, size=1))

#################################################################

'''
Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals.
'''

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(np.mean(deals))

'''
<script.py> output:
    0.8269230769230769
'''

#################################################################
#################################################################
#################################################################

'''
Brilliant binomial simulation! In this simulated year, Amir won 0.83 deals on average each week.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/random-numbers-and-probability-2?ex=14
'''
