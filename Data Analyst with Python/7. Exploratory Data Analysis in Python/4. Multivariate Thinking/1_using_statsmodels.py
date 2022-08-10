'''
Using StatsModels
Let's run the same regression using SciPy and StatsModels, and confirm we get the same results.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Compute the regression of '_VEGESU1' as a function of 'INCOME2' using SciPy's linregress().

Compute the regression of '_VEGESU1' as a function of 'INCOME2' using StatsModels' smf.ols().
'''

from scipy.stats import linregress
import statsmodels.formula.api as smf

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs, ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data = brfss).fit()
print(results.params)

#################################################################

'''
Nice job. When you start working with a new library, checks like this help ensure that you are doing it right.

In this example, we used SciPy's linregress() to compute the regression of '_VEGESU1' as a function of 'INCOME2', but we used StatsModels's smf.ols() to do the same thing.
'''

'''
<script.py> output:
    LinregressResult(slope=0.06988048092105019, intercept=1.5287786243363106, rvalue=0.11967005884864099, pvalue=1.378503916248713e-238, stderr=0.002110976356332333, intercept_stderr=0.013196467544093607)
    Intercept    5.451
    _VEGESU1     0.205
    dtype: float64


<script.py> output:
    LinregressResult(slope=0.06988048092105019, intercept=1.5287786243363106, rvalue=0.11967005884864099, pvalue=1.378503916248713e-238, stderr=0.002110976356332333, intercept_stderr=0.013196467544093607)
    Intercept    1.529
    INCOME2      0.070
    dtype: float64
'''