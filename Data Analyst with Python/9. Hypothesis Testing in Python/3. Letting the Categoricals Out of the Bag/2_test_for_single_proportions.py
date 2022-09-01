'''
Test for single proportions
In Chapter 1, you calculated a p-value for a test hypothesizing that the proportion of late shipments was greater than 6%. In that chapter, you used a bootstrap distribution to estimate the standard error of the statistic. An alternative is to use an equation for the standard error based on the sample proportion, hypothesized proportion, and sample size.

z = \dfrac{\hat{p} - p_{0}}{\sqrt{\dfrac{p_{0}*(1-p_{0})}{n}}} 

You'll revisit the p-value using this simpler calculation.

late_shipments is available. pandas and numpy are available under their usual aliases, and norm is loaded from scipy.stats.


'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Hypothesize that the proportion of late shipments is 6%.

Calculate the sample proportion of shipments where late equals "Yes".

Calculate the number of observations in the sample.
'''

# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments['late'] == 'Yes').mean()

# Calculate the sample size
n = len(late_shipments)

# Print p_hat and n
# print(f'p_hat: {p_hat}\nn: {n}')
print(p_hat, n)

'''
<script.py> output:
    p_hat: 0.061
    n: 1000
'''

#################################################################

'''
Calculate the numerator and denominator of the z-score.

Calculate the z-score as the ratio of these numbers.
'''

# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments['late'] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Calculate the numerator and denominator of the test statistic
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)

# Calculate the test statistic
z_score = numerator / denominator

# Print the result
print(f'z_score: {z_score}')

'''
<script.py> output:
    z_score: 0.13315591032282698
'''

#################################################################

'''
Transform the z-score into a p-value, remembering that this is a "greater than" alternative hypothesis.
'''

# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments['late'] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Calculate the numerator and denominator of the test statistic
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)

# Calculate the test statistic
z_score = numerator / denominator

# Calculate the p-value from the z-score
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(f'p_value: {p_value}')

'''
<script.py> output:
    p_value: 0.44703503936503364
'''
#################################################################
#################################################################
#################################################################

'''
Well proportioned! While bootstrapping can be used to estimate the standard error of any statistic, it is computationally intensive. For proportions, using a simple equation of the hypothesized proportion and sample size is easier to compute.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/letting-the-categoricals-out-of-the-bag-3?ex=3
'''
