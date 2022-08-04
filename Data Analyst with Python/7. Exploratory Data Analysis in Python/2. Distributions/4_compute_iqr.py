'''
Compute IQR
Recall from the video that the interquartile range (IQR) is the difference between the 75th and 25th percentiles. It is a measure of variability that is robust in the presence of errors or extreme values.

In this exercise, you'll compute the interquartile range of income in the GSS dataset. Income is stored in the 'realinc' column, and the CDF of income has already been computed and stored in cdf_income.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Calculate the 75th percentile of income and store it in percentile_75th.
'''

# Calculate the 75th percentile
percentil = 0.75
percentile_75th = cdf_income.inverse(percentil)
print(percentile_75th)

#################################################################

'''
Calculate the 25th percentile of income and store it in percentile_25th.
'''

# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile

percentile_25th = cdf_income.inverse(0.25)

#################################################################

'''
Calculate the interquartile range of income. Store the result in iqr.
'''

# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)

#################################################################

#Question
#What is the interquartile range (IQR) of income in the GSS dataset?

#Possible Answers

# => 'Approximately 29676'

'Approximately 26015'

'Approximately 34702'

'Approximately 30655'



