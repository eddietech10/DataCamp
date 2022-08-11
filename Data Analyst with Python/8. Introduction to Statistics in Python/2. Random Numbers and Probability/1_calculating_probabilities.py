'''
Calculating probabilities
You're in charge of the sales team, and it's time for performance reviews, starting with Amir. As part of the review, you want to randomly select a few of the deals that he's worked on over the past year so that you can look at them more deeply. Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.

Recall that the probability of an event can be calculated by
P(\text{event}) = \frac{\text{# ways event can happen}}{\text{total # of possible outcomes}}

Both pandas as pd and numpy as np are loaded and amir_deals is available.
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Count the number of deals Amir worked on for each product type and store in counts.
'''

# Count the deals for each product
counts = amir_deals['product'].value_counts()
print(counts)

'''
<script.py> output:
    Product B    62
    Product D    40
    Product A    23
    Product C    15
    Product F    11
    Product H     8
    Product I     7
    Product E     5
    Product N     3
    Product G     2
    Product J     2
    Name: product, dtype: int64
'''

#################################################################

'''
Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on. Save this as probs.
'''

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / counts.sum()
print(probs)

'''
<script.py> output:
    Product B    0.348
    Product D    0.225
    Product A    0.129
    Product C    0.084
    Product F    0.062
    Product H    0.045
    Product I    0.039
    Product E    0.028
    Product N    0.017
    Product G    0.011
    Product J    0.011
    Name: product, dtype: float64
'''

#################################################################

'''
Question
If you randomly select one of Amir's deals, what's the probability that the deal will involve Product C?

Possible Answers

15%

80.43%

=> 8.43%

22.5%

124.3%
'''



#################################################################
#################################################################
#################################################################

'''
Perfect probability calculations! Now that you know what the chances are, it's time to start sampling.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/random-numbers-and-probability-2?ex=3
'''
