'''
Calculating a z-score
Since variables have arbitrary ranges and units, we need to standardize them. For example, a hypothesis test that gave different answers if the variables were in Euros instead of US dollars would be of little value. Standardization avoids that.

One standardized value of interest in a hypothesis test is called a z-score. To calculate it, you need three numbers: the sample statistic (point estimate), the hypothesized statistic, and the standard error of the statistic (estimated from the bootstrap distribution).

The sample statistic is available as late_prop_samp.

late_shipments_boot_distn is a bootstrap distribution of the proportion of late shipments, available as a list.

pandas and numpy are loaded with their usual aliases.

Keywords:
- standard error
- z-score
- Hypothesized value
- Standardization
- bootstrap distribution
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Hypothesize that the proportion of late shipments is 6%.

Calculate the standard error from the standard deviation of the bootstrap distribution.

Calculate the z-score.
'''

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)

'''
<script.py> output:
    0.13353771933071554
'''
#################################################################
#################################################################
#################################################################

'''
Zesty z-scoring! The z-score is a standardized measure of the difference between the sample statistic and the hypothesized statistic.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/yum-that-dish-tests-good-1?ex=4
'''
