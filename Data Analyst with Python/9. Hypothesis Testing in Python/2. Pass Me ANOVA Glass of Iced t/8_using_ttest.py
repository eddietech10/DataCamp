'''
Using ttest()
Manually calculating test statistics and transforming them with a CDF to get a p-value is a lot of effort to compare two sample means. The comparison of two sample means is called a t-test, and the pingouin Python package has a .ttest() method to accomplish it. This method provides some flexibility in how you perform the test.

As in the previous exercise, you'll explore the difference between the proportion of county-level votes for the Democratic candidate in 2012 and 2016 to identify if the difference is significant.

sample_dem_data is available and has the columns diff, dem_percent_12, and dem_percent_16 in addition to the state and county names. pingouin and has been loaded along with pandas as pd.


'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Conduct a t-test on the sample differences (the diff column of sample_dem_data), using an appropriate alternative hypothesis chosen from "two-sided", "less", and "greater".
'''

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'],
                              y=0,
                              alternative='two-sided')
                              
# Print the test results
print(test_results)

#################################################################

'''
Question
What's the correct decision from the t-test, assuming \alpha = 0.01?

Possible Answers

Fail to reject the null hypothesis.

=> Reject the null hypothesis.

You can't conclude anything from this hypothesis test.
'''

p_val = 3.601e-115
alpha = 0.01
p_val <= alpha

#################################################################

'''
Conduct a paired test on the democratic votes in 2012 and 2016 (the dem_percent_12 and dem_percent_16 columns of sample_dem_data), using an appropriate alternative hypothesis.
'''

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], 
                              y=0, 
                              alternative="two-sided")

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'], 
                              y=sample_dem_data['dem_percent_16'],
                              paired=True,
                              alternative="two-sided")

# Print the paired test results
print(paired_test_results)

'''
<script.py> output:
                 T  dof alternative       p-val         CI95%  cohen-d        BF10  power
    T-test  30.298  499   two-sided  3.601e-115  [6.39, 7.27]    0.454  2.246e+111    1.0
'''

#################################################################

'''
Question:
Compare the paired t-test to an (inappropriate) unpaired test on the same data. How does the p-value change?

pingouin.ttest(x=sample_dem_data['dem_percent_12'], 
               y=sample_dem_data['dem_percent_16'], 
               alternative="two-sided")

Possible Answers:
The p-value from the unpaired test is smaller than the p-value from the paired test.

The p-value from the unpaired test is equal to the p-value from the paired test.

The p-value from the unpaired test is greater than than the p-value from the paired test.
'''

p_val_paired=3.601e-115
p_val_unpaired=1.346e-12

p_val_paired < p_val_unpaired
True
p_val_paired == p_val_unpaired
False

#################################################################
#################################################################
#################################################################

'''
Paired t-test party! Using .ttest() lets you avoid manual calculation to run your test. When you have paired data, a paired t-test is preferable to the unpaired version because it reduces the chance of a false negative error.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=11
'''
