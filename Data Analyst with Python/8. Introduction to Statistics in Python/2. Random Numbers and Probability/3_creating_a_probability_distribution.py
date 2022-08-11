'''
Creating a probability distribution
A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space based on the size of the groups that come most often. On one night, there are 10 groups of people waiting to be seated at the restaurant, but instead of being called in the order they arrived, they will be called randomly. In this exercise, you'll investigate the probability of groups of different sizes getting picked first. Data on each of the ten groups is contained in the restaurant_groups DataFrame.

Remember that expected value can be calculated by multiplying each possible outcome with its corresponding probability and taking the sum. The restaurant_groups data is available. pandas is loaded as pd, numpy is loaded as np, and matplotlib.pyplot is loaded as plt.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Create a histogram of the group_size column of restaurant_groups, setting bins to [2, 3, 4, 5, 6]. Remember to show the plot.
'''

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()

#################################################################

'''
Count the number of each group_size in restaurant_groups, then divide by the number of rows in restaurant_groups to calculate the probability of randomly selecting a group of each size. Save as size_dist.

Reset the index of size_dist.

Rename the columns of size_dist to group_size and prob.
'''

# Create probability distribution
#size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups['group_size'].value_counts().sum()
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

'''
2    0.6
4    0.2
6    0.1
3    0.1
Name: group_size, dtype: float64
'''


# Reset index and rename columns
# size_dist = size_dist.sample(4, replace=True)
size_dist = size_dist.reset_index()
'''
   index  group_size
0      2         0.6
1      4         0.2
2      6         0.1
3      3         0.1
'''
size_dist.columns = ['group_size', 'prob']
print(size_dist)

'''
   index  group_size
0      2         0.6
1      4         0.2
2      6         0.1
3      3         0.1
'''


#################################################################

'''
Calculate the expected value of the size_distribution, which represents the expected group size, by multiplying the group_size by the prob and taking the sum.
'''

# Calculate expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])
print(expected_value)

'''
<script.py> output:
    2.9000000000000004
'''

#################################################################

'''
Calculate the probability of randomly picking a group of 4 or more people by subsetting for groups of size 4 or more and summing the probabilities of selecting those groups.
'''

# Subset groups of size 4 or more
groups_4_or_more = size_dist.sample()

'''
   group_size  prob
1           4   0.2
'''

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['group_size'] * groups_4_or_more['prob'])
print(prob_4_or_more)

'''
<script.py> output:
    0.30000000000000004
'''

#################################################################
#################################################################
#################################################################

'''
Dexterous distribution utilization! You'll continue to build upon these skills since many statistical tests and methods use probability distributions as their foundation.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/random-numbers-and-probability-2?ex=6
'''
