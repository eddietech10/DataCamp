'''
Calculating the sample mean
The late_shipments dataset contains supply chain data on the delivery of medical supplies. Each row represents one delivery of a part. The late columns denotes whether or not the part was delivered late. A value of "Yes" means that the part was delivered late, and a value of "No" means the part was delivered on time.

Let's begin our analysis by calculating a point estimate (or sample statistic), namely the proportion of late shipments.

late_shipments is available, and pandas is loaded as pd.

Keywords:
- sample size
- sample mean
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Print the late_shipments dataset.
'''

# Print the late_shipments dataset
print(late_shipments)

#################################################################

'''
Calculate the proportion of late shipments in the sample; that is, the mean cases where the late column is "Yes".
'''

# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = (late_shipments['late'] == 'Yes').mean()

# Print the results
print(late_prop_samp)

'''
proportion of late shipments: 0.061
'''

#################################################################
#################################################################
#################################################################

'''
Cool calculating! The proportion of late shipments in the sample is 0.061, or 6.1%.

https://campus.datacamp.com/courses/hypothesis-testing-in-python/yum-that-dish-tests-good-1?ex=3
'''

