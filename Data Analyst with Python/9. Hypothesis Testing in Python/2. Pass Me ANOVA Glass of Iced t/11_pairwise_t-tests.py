'''
Pairwise t-tests
The ANOVA test didn't tell you which categories of shipment mode had significant differences in pack prices. To pinpoint which categories had differences, you could instead use pairwise t-tests.

late_shipments is available and pingouin has been loaded.

Keywords:
- pingouin.pairwise_ttest
- dv
- between
- padjust
- bonferroni
- bonf
- alpha
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Perform pairwise t-tests on late_shipments's pack_price variable, grouped by shipment_mode, without doing any p-value adjustment.
'''

# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pingouin.pairwise_tests(data=late_shipments,
                                           dv='pack_price',
                                           between='shipment_mode',
                                           padjust='none')

# Print pairwise_results
print(pairwise_results)

'''
<script.py> output:
            Contrast            A            B  Paired  Parametric  ...      dof  alternative      p-unc       BF10 hedges
    0  shipment_mode          Air  Air Charter   False        True  ...  600.686    two-sided  8.748e-75  5.809e+76  0.727
    1  shipment_mode          Air        Ocean   False        True  ...  986.980    two-sided  6.935e-71  1.129e+67  0.711
    2  shipment_mode  Air Charter        Ocean   False        True  ...   35.615    two-sided  3.123e-03     15.277 -0.424
    
    [3 rows x 11 columns]
'''

#################################################################

'''
Modify the pairwise t-tests to use the Bonferroni p-value adjustment.
'''

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="bonf")

# Print pairwise_results
print(pairwise_results)

'''
<script.py> output:
            Contrast            A            B  Paired  Parametric  ...      p-unc     p-corr p-adjust       BF10  hedges
    0  shipment_mode          Air  Air Charter   False        True  ...  8.748e-75  2.625e-74     bonf  5.809e+76   0.727
    1  shipment_mode          Air        Ocean   False        True  ...  6.935e-71  2.080e-70     bonf  1.129e+67   0.711
    2  shipment_mode  Air Charter        Ocean   False        True  ...  3.123e-03  9.369e-03     bonf     15.277  -0.424
    
    [3 rows x 13 columns]
'''

#################################################################

'''
Question:
Using the Bonferroni correction results and assuming a significance level of 0.1, for which pairs of shipment modes should you reject the null hypothesis that the pack prices are equal?

Possible Answers:

"Ocean" and "Air Charter"; "Ocean" and "Air"; "Air Charter" and "Air".

"Ocean" and "Air" and also "Air Charter" and "Air".

"Ocean" and "Air" only.

"Ocean" and "Air Charter" only.
'''

#################################################################
#################################################################
#################################################################

'''
Pairwise perfection! After applying the Bonferroni adjustment, the p-values for the t-tests between each of the three groups are all less than 0.1.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=15
'''
