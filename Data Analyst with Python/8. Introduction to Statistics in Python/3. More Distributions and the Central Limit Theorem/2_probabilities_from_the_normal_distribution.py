'''
Probabilities from the normal distribution
Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics, you want to calculate the probability of Amir closing a deal worth various amounts.

norm from scipy.stats is imported as well as pandas as pd. The DataFrame amir_deals is loaded.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
What's the probability of Amir closing a deal worth less than $7500?
'''

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

'''
<script.py> output:
    0.8943502263331446
'''

#################################################################

'''
What's the probability of Amir closing a deal worth more than $1000?
'''

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)

print(prob_over_1000)

'''
<script.py> output:
    0.9772498680518208
'''

#################################################################

'''
What's the probability of Amir closing a deal worth between $3000 and $7000?
'''

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)

'''
<script.py> output:
    0.6826894921370859
'''

#################################################################

'''
What amount will 25% of Amir's sales be less than?
'''

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)

'''
<script.py> output:
    3651.0204996078364
'''

#################################################################
#################################################################
#################################################################

'''
Nifty normal distribution usage! You know that you can count on Amir 75% (1-0.25) of the time to make a sale worth at least $3651.02. This information could be useful in making company-wide sales projections.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/more-distributions-and-the-central-limit-theorem-3?ex=3
'''
