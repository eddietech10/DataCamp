'''
Why is t needed?
The process for calculating p-values is to start with the sample statistic, standardize it to get a test statistic, then transform it via a cumulative distribution function. In Chapter 1, that final transformation was denoted , and the CDF transformation used the (standard normal) z-distribution. In the last video, the test statistic was denoted , and the transformation used the t-distribution.

In which hypothesis testing scenario is a t-distribution needed instead of the z-distribution?


'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Possible Answers

The t-distribution is just another name for the z-distribution, so they can be used interchangeably.

The t-distribution is the same thing as the z-distribution for very small sample sizes.

=> When a sample standard deviation is used in estimating a standard error.

When you are comparing the means of three or more samples, rather than comparing a single sample mean to a value.
'''



#################################################################
#################################################################
#################################################################

'''
Terrific t! Using a sample standard deviation to estimate the standard error is computationally easier than using bootstrapping. However, to correct for the approximation, you need to use a t-distribution when transforming the test statistic to get the p-value.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=5
'''
