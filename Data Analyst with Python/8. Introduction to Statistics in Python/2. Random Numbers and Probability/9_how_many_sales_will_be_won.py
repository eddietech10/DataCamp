'''
How many sales will be won?
Now Amir wants to know how many deals he can expect to close each week if his win rate changes. Luckily, you can use your binomial distribution knowledge to help him calculate the expected value in different situations. Recall from the video that the expected value of a binomial distribution can be calculated by n \times p.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.

Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.

Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%.
'''

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

'''
<script.py> output:
    0.8999999999999999
'''

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

'''
<script.py> output:
    0.75
'''

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)

'''
<script.py> output:
    1.0499999999999998
'''

#################################################################
#################################################################
#################################################################

'''
Excellent expectation experimentation! If Amir's win rate goes up by 5%, he can expect to close more than 1 deal on average each week.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/random-numbers-and-probability-2?ex=16
'''
