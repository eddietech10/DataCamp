'''
Calculating a confidence interval
If you give a single estimate of a sample statistic, you are bound to be wrong by some amount. For example, the hypothesized proportion of late shipments was 6%. Even if evidence suggests the null hypothesis that the proportion of late shipments is equal to this, for any new sample of shipments, the proportion is likely to be a little different due to sampling variability. Consequently, it's a good idea to state a confidence interval. That is, you say, "we are 95% 'confident' that the proportion of late shipments is between A and B" (for some value of A and B).

Sampling in Python demonstrated two methods for calculating confidence intervals. Here, you'll use quantiles of the bootstrap distribution to calculate the confidence interval.
https://campus.datacamp.com/courses/sampling-in-python/pull-your-data-up-by-its-bootstraps-4?ex=10

late_prop_samp and late_shipments_boot_distn are available; pandas and numpy are loaded with their usual aliases.

Keywords:
- confidence interval
- bootstrap distribution
- quantiles
- hypothesis testing
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Calculate a 95% confidence interval from late_shipments_boot_distn using the quantile method, labeling the lower and upper intervals lower and upper.
'''

# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))

'''
<script.py> output:
    (0.047, 0.076)
'''

#################################################################

'''
Question
Does the confidence interval match up with the conclusion to stick with the original assumption that 6% is a reasonable value for the unknown population parameter?
Possible Answers

=> Yes, since 0.06 is included in the 95% confidence interval and we failed to reject H_{0} due to a large p-value, the results are similar.

No, since 0.06 is included in the 95% confidence interval and we should have rejected H_{0} due to a large p-value, the results do not match.

No, there is no relationship between confidence intervals and hypothesis tests.
'''

from scipy.stats import norm

alpha = 0.05
late_prop_samp = late_prop_samp
prop_child_hyp = 0.06
std_error = np.std(late_shipments_boot_distn, ddof=1)
z_score = (late_prop_samp - prop_child_hyp) / std_error
p_value = 1 - norm.cdf(z_score, loc=0, scale=1)

print(f'p_value: {p_value}')
print(f'alpha: {alpha}')
print(p_value <= alpha)

'''
p_value: 0.4468840678346485

alpha: 0.05

False
'''

#################################################################
#################################################################
#################################################################

'''
Cool and confident! When you have a confidence interval width equal to one minus the significance level, if the hypothesized population parameter is within the confidence interval, you should fail to reject the null hypothesis.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/yum-that-dish-tests-good-1?ex=11
'''
