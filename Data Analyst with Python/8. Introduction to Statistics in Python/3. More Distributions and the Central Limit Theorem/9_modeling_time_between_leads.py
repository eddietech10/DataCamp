'''
Modeling time between leads
To further evaluate Amir's performance, you want to know how much time it takes him to respond to a lead after he opens it. On average, it takes 2.5 hours for him to respond. In this exercise, you'll calculate probabilities of different amounts of time passing between Amir receiving a lead and sending a response.

Keywords:
- exponential distribution
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Import expon from scipy.stats. What's the probability it takes Amir less than an hour to respond to a lead?
'''

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

'''
<script.py> output:
    0.3296799539643607
'''

#################################################################

'''
# Import expon from scipy.stats
from scipy.stats import expon
'''

# Print probability response takes > 4 hours
print(1 - expon.cdf(4, scale=2.5))

'''
<script.py> output:
    0.20189651799465536
'''

#################################################################

'''
What's the probability it takes Amir 3-4 hours to respond to a lead?
'''

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))

'''
<script.py> output:
    0.09929769391754684
'''

#################################################################
#################################################################
#################################################################

'''
Excellent exponential computations! There's only about a 20% chance it will take Amir more than 4 hours to respond, so he's pretty speedy in his responses.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/more-distributions-and-the-central-limit-theorem-3?ex=15
'''
