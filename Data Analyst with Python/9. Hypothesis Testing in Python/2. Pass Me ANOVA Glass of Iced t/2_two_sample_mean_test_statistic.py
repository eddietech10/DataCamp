'''
Two sample mean test statistic
The hypothesis test for determining if there is a difference between the means of two populations uses a different type of test statistic to the z-scores you saw in Chapter 1. It's called "t", and it can be calculated from three values from each sample using this equation.

t = \dfrac{(\bar{x}_{\text{child}} - \bar{x}_{\text{adult}})}{\sqrt{\dfrac{s_{\text{child}}^2}{n_{\text{child}}} + \dfrac{s_{\text{adult}}^2}{n_{\text{adult}}}}}

While trying to determine why some shipments are late, you may wonder if the weight of the shipments that were on time is less than the weight of the shipments that were late. The late_shipments dataset has been split into a "yes" group, where late == "Yes" and a "no" group where late == "No". The weight of the shipment is given in the weight_kilograms variable.

The sample means for the two groups are available as xbar_no and xbar_yes. The sample standard deviations are s_no and s_yes. The sample sizes are n_no and n_yes. numpy is also loaded as np.

Keywords:
- t-statistic
- standard deviation
- standard error
- t-test
- z-score
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Calculate the numerator of the t test statistic.

Calculate the denominator of the t test statistic.

Use those two numbers to calculate the t test statistic.
'''

# Calculate the numerator of the test statistic
numerator = xbar_yes - xbar_no

# Calculate the denominator of the test statistic
denominator = np.sqrt((s_yes**2 / n_yes) + (s_no**2 / n_no))

# Calculate the test statistic
t_stat = numerator / denominator

# Print the test statistic
print(f't_stat: {t_stat}')

'''
<script.py> output:
    t_stat: 2.3936661778766433
'''

#################################################################
#################################################################
#################################################################

'''
t-rrific! When testing for differences between means, the test statistic is called 't' rather than 'z', and can be calculated using six numbers from the samples. Here, the value is about -2.39 or 2.39, depending on the order you calculated the numerator.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=3
'''
