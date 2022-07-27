'''
Explore financials with .query():

You have been given a table of financial data from some popular social network companies called social_fin. All of the values are in thousands of US dollars.

Use the .query() method and the IPython shell to explore social_fin and select the True statement.
'''


#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Possible Answers:

There 2 rows where the value is greater than $50,000,000K.

There are 3 rows for total revenue for Facebook.

There are 6 rows where the net income has a negative value.

There are 45 rows, where the gross profit is greater than $100K.
'''

social_fin.query('financial == "net_income" and value < 0')

