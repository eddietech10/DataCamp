'''
- Merge employees and top_cust with a left join, setting indicator argument to True. Save the result to empl_cust.

- Select the srid column of empl_cust and the rows where _merge is 'left_only'. Save the result to srid_list.

Subset the employees table and select those rows where the srid is in the variable srid_list and print the results.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################


# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)

#################################################################

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']


#################################################################

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])


#################################################################
