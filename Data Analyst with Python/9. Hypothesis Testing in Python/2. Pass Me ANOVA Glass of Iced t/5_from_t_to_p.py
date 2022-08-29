'''
From t to p
Previously, you calculated the test statistic for the two-sample problem of whether the mean weight of shipments is smaller for shipments that weren't late (late == "No") compared to shipments that were late (late == "Yes"). In order to make decisions about it, you need to transform the test statistic with a cumulative distribution function to get a p-value.

Recall the hypotheses:

H_{0}: The mean weight of shipments that weren't late is the same as the mean weight of shipments that were late.

H_{A}: The mean weight of shipments that weren't late is less than the mean weight of shipments that were late.

The test statistic, t_stat, is available, as are the samples sizes for each group, n_no and n_yes. Use a significance level of alpha = 0.05.

t has also been imported from scipy.stats.

Keywords:
- t-distribution
- cumulative distribution function
- p-value
- significance level
- standard error
- standard deviation
- bootstrapping
- hypothesis testing
- p-value
- sample size
- test statistic
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Question
What type of test does the alternative hypothesis indicate that we need?

Possible Answers:

Two-tailed

=> Left-tailed

Right-tailed
'''

#################################################################

'''
Calculate the degrees of freedom for the test.

Compute the p-value using the test statistic, t_stat.
'''

# Calculate the degrees of freedom
degrees_of_freedom = (n_no + n_yes) - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat, df=degrees_of_freedom)

# Print the p_value
print(f'p_value: {p_value}')

'''
<script.py> output:
    p_value: 0.008432382146249523
'''

#################################################################

'''
Question:
What decision should you make based on the results of the hypothesis test?

Possible Answers

Fail to reject the null hypothesis.

Reject the null hypothesis.

You can't conclude anything from this hypothesis test.
'''

p_value = 0.008432382146249523
alpha = 0.05
result = p_value < alpha
print(f'result: {result}')

#################################################################
#################################################################
#################################################################

'''
Perspicacious p-value predictions! When the standard error is estimated from the sample standard deviation and sample size, the test statistic is transformed into a p-value using the t-distribution.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=7
'''
