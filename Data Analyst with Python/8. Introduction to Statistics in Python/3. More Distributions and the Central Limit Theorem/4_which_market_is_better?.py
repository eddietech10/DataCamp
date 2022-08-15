'''
Which market is better?
The key metric that the company uses to evaluate salespeople is the percent of sales they make over $1000 since the time put into each sale is usually worth a bit more than that, so the higher this metric, the better the salesperson is performing.

Recall that Amir's current sales amounts have a mean of $5000 and a standard deviation of $2000, and Amir's predicted amounts in next quarter's market have a mean of $6000 and a standard deviation of $2600.

norm from scipy.stats is imported.

Based only on the metric of percent of sales over $1000, does Amir perform better in the current market or the predicted market?
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Possible Answers

Amir performs much better in the current market.

Amir performs much better in next quarter's predicted market.

=> Amir performs about equally in both markets.
'''

current = 1 - norm.cdf(1000, 5000, 2000)
'''
In [16]: current
Out[16]: 0.9772498680518208
'''

predicted = 1 - norm.cdf(1000, 6000, 2600)
'''
In [17]: predicted
Out[17]: 0.9727648049862613
'''

#################################################################
#################################################################
#################################################################

'''
Great work! In the current market, Amir makes sales over $1000 about 97.7% of the time, and about 97.3% of the time in the predicted market, so there's not much of a difference. However, his average sale amount is higher in the predicted market, so your company may want to consider other metrics as well.

https://campus.datacamp.com/courses/introduction-to-statistics-in-python/more-distributions-and-the-central-limit-theorem-3?ex=5
'''
