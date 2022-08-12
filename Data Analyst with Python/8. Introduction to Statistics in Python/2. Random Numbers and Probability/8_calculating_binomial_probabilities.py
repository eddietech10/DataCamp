'''
Calculating binomial probabilities
Just as in the last exercise, assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. In this exercise, you'll calculate what the chances are of him closing different numbers of deals using the binomial distribution.

binom is imported from scipy.stats.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.
'''

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)

print(prob_3)


'''
<script.py> output:
    0.784
'''

#################################################################

'''
What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.
'''

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)

print(prob_less_than_or_equal_1)

'''
<script.py> output:
    0.026999999999999996
'''

#################################################################

'''
What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.
'''

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)

print(prob_greater_than_1)

'''
<script.py> output:
    0.21599999999999997
'''

#################################################################
#################################################################
#################################################################

'''
Powerful probability calculations! Amir has about a 22% chance of closing more than one deal in a week.
'''
