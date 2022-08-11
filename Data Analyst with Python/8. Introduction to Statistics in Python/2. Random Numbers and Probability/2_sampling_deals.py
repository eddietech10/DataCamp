'''
Sampling deals
In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with the service they received. You'll try doing this both with and without replacement.

Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.

Both pandas as pd and numpy as np are loaded and amir_deals is available.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Set the random seed to 24.

Take a sample of 5 deals without replacement and store them as sample_without_replacement.
'''

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

'''
<script.py> output:
         Unnamed: 0    product   client status   amount  num_users
    127         128  Product B  Current    Won  2070.25          7
    148         149  Product D  Current    Won  3485.48         52
    77           78  Product B  Current    Won  6252.30         27
    104         105  Product D  Current    Won  4110.98         39
    166         167  Product C      New   Lost  3779.86         11
'''

#################################################################

'''
Take a sample of 5 deals with replacement and save as sample_with_replacement.
'''

# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace = True)
print(sample_with_replacement)

'''
<script.py> output:
         Unnamed: 0    product   client status   amount  num_users
    162         163  Product D  Current    Won  6755.66         59
    131         132  Product B  Current    Won  6872.29         25
    87           88  Product C  Current    Won  3579.63          3
    145         146  Product A  Current    Won  4682.94         63
    145         146  Product A  Current    Won  4682.94         63
'''

#################################################################

'''
Question
What type of sampling is better to use for this situation?

Possible Answers

With replacement

=> Without replacement

It doesn't matter
'''



#################################################################
#################################################################
#################################################################

'''
Spectactular sampling! It's important to consider how you'll take a sample since there's no one-size-fits-all way to sample, and this can have an effect on your results.
'''
