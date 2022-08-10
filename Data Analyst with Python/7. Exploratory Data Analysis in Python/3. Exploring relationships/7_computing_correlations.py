'''
Computing correlations
The purpose of the BRFSS is to explore health risk factors, so it includes questions about diet. The variable '_VEGESU1' represents the number of servings of vegetables respondents reported eating per day.

Let's see how this variable relates to age and income.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################


'''
From the brfss DataFrame, select the columns 'AGE', 'INCOME2', and '_VEGESU1'.

Compute the correlation matrix for these variables.
'''

# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())

#################################################################


'''
<script.py> output:

                AGE  INCOME2  _VEGESU1
    AGE       1.000   -0.015     -0.01
    INCOME2  -0.015    1.000      0.12
    _VEGESU1 -0.010    0.120      1.00
'''


#################################################################


'''
Interpreting correlations
In the previous exercise, the correlation between income and vegetable consumption is about 0.12. The correlation between age and vegetable consumption is about -0.01.

Which of the following are correct interpretations of these results:

A: People with higher incomes eat more vegetables.
B: The relationship between income and vegetable consumption is linear.
C: Older people eat more vegetables.
D: There could be a strong nonlinear relationship between age and vegetable consumption.
'''


# Possible Answers

'A and C only.'

'B and D only.'

'B and C only.'

# ==> 'A and D only.'



#################################################################

'''
Correct! The correlation between income and vegetable consumption is small, but it suggests that there is a relationship. But a correlation close to 0 does mean there is no relationship.
'''