'''
ANOVA
The box plots made it look like the distribution of pack price was different for each of the three shipment modes. However, it didn't tell us whether the mean pack price was different in each category. To determine that, we can use an ANOVA test. The null and alternative hypotheses can be written as follows.

H_{0}: Pack prices for every category of shipment mode are the same.

H_{A}: Pack prices for some categories of shipment mode are different.

We'll set a significance level of 0.1.

late_shipments is available and pingouin has been loaded.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Run an ANOVA on late_shipments investigating 'pack_price' (the dependent variable) between the groups of 'shipment_mode'.
'''

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data=late_shipments,
                               dv='pack_price',
                               between='shipment_mode')

# Print anova_results
print(anova_results)

'''
<script.py> output:
              Source  ddof1  ddof2       F      p-unc    np2
    0  shipment_mode      2    997  21.865  5.089e-10  0.042
'''

#################################################################

'''
Question:
Assuming a significance level of 0.1, should you reject the null hypothesis that there is a difference between pack prices between the shipment modes?

Possible Answers:
Yes. The p-value is greater than or equal to the significance level, so the null hypothesis should be rejected.

=> Yes. The p-value is less than or equal to the significance level, so the null hypothesis should be rejected.

No. The p-value is greater than or equal to the significance level, so the null hypothesis should fail to be rejected.

No. The p-value is less than or equal to the significance level, so the null hypothesis should fail to be rejected.
'''

alpha = 0.1
p_value = 5.089e-10
p_value <= alpha
True

#################################################################
#################################################################
#################################################################

'''
Amazing ANOVA! There is a significant difference in pack prices between the shipment modes. However, we don't know which shipment modes this applies to.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=14
'''
