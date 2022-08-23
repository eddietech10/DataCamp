'''
Calculating p-values
In order to determine whether to choose the null hypothesis or the alternative hypothesis, you need to calculate a p-value from the z-score.

You'll now return to the late shipments dataset and the proportion of late shipments.

The null hypothesis, H_{0}, is that the proportion of late shipments is six percent.

The alternative hypothesis, H_{A}, is that the proportion of late shipments is greater than six percent.

The observed sample statistic, late_prop_samp, the hypothesized value, late_prop_hyp (6%), and the bootstrap standard error, std_error are available. norm from scipy.stats has also been loaded without an alias.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Question:
What type of test should be used for this alternative hypothesis?

Possible Answers

Two-tailed

Left-tailed

=> Right-tailed

It doesn't matter; any one will do.

A hypothesis test isn't appropriate to answer this question.
'''



#################################################################

'''
Calculate the z-score of late_prop_samp.

Calculate the p-value for the z-score, using a right-tailed test.
'''

# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_score, loc=0, scale=1)
                 
# Print the p-value
print(f'p_value: {p_value}')

'''
<script.py> output:
    p_value: 0.4468840678346485
'''

#################################################################
#################################################################
#################################################################

'''
Perfect p-value! The p-value is calculated by transforming the z-score with the standard normal cumulative distribution function.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/yum-that-dish-tests-good-1?ex=8
'''
