'''
The mean of means
You want to know what the average number of users (num_users) is per deal, but you want to know this number for the entire company so that you can see if Amir's deals have more or fewer users than the company's average deal. The problem is that over the past year, the company has worked on more than ten thousand deals, so it's not realistic to compile all the data. Instead, you'll estimate the mean by taking several random samples of deals, since this is much easier than collecting data from everyone in the company.

amir_deals is available and the user data for all the company's deals is available in all_deals. Both pandas as pd and numpy as np are loaded.

Keywords:
- sampling distribution
- mean of means
- seed
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Set the random seed to 321.

Take 30 samples (with replacement) of size 20 from all_deals['num_users'] and take the mean of each sample. Store the sample means in sample_means.

Print the mean of sample_means.

Print the mean of the num_users column of amir_deals.
'''

# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
    # Take sample of size 20 from num_users col of all_deals with replacement
    cur_sample = all_deals['num_users'].sample(20, replace=True)
    # Take mean of cur_sample
    cur_mean = np.mean(cur_sample)
    # Append cur_mean to sample_means
    sample_means.append(cur_mean)

# Print mean of sample_means
print(f'mean of sample_means:\n{np.mean(sample_means)}')
print('-' * 33)
# Print mean of num_users in amir_deals
print(f'mean of num_users in amir_deals:\n{np.mean(amir_deals["num_users"])}')


'''
<script.py> output:
    mean of sample_means:
    38.31333333333332
    ---------------------------------
    mean of num_users in amir_deals:
    37.651685393258425
'''


#################################################################
#################################################################
#################################################################

'''
Magnificent mean calculation! Amir's average number of users is very close to the overall average, so it looks like he's meeting expectations. Make sure to note this in his performance review!

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/more-distributions-and-the-central-limit-theorem-3?ex=9
'''
