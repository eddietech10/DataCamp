'''
Starting with the licenses table on the left, merge it to the biz_owners table on the column account, and save the results to a variable named licenses_owners.

Group licenses_owners by title and count the number of accounts for each title. Save the result as counted_df

Sort counted_df by the number of accounts in descending order, and save this as a variable named sorted_df.

Use the .head() method to print the first few rows of the sorted_df.
'''


#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################


# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())