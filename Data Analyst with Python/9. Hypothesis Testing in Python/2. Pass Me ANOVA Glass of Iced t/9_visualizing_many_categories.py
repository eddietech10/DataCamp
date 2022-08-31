'''
Visualizing many categories
So far in this chapter, we've only considered the case of differences in a numeric variable between two categories. Of course, many datasets contain more categories. Before you get to conducting tests on many categories, it's often helpful to perform exploratory data analysis (EDA), calculating summary statistics for each group and visualizing the distributions of the numeric variable for each category using box plots.

Here, we'll return to the late shipments data, and how the price of each package (pack_price) varies between the three shipment modes (shipment_mode): "Air", "Air Charter", and "Ocean".

late_shipments is available; pandas and matplotlib.pyplot are loaded with their standard aliases, and seaborn is loaded as sns.


'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
Group late_shipments by shipment_mode and calculate the mean pack_price for each group, storing the result in xbar_pack_by_mode.
'''

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].mean()

# Print the grouped means
print(xbar_pack_by_mode)

'''
<script.py> output:
    shipment_mode
    Air            39.712
    Air Charter     4.227
    Ocean           6.432
    Name: pack_price, dtype: float64
'''

#################################################################

'''
Group late_shipments by shipment_mode and calculate the standard deviation pack_price for each group, storing the result in s_pack_by_mode.
'''

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].std()

# Print the grouped standard deviations
print(s_pack_by_mode)

'''
<script.py> output:
    shipment_mode
    Air            48.933
    Air Charter     0.993
    Ocean           5.303
    Name: pack_price, dtype: float64
'''

#################################################################

'''
Create a boxplot from late_shipments with "pack_price" as x and "shipment_mode" as y.
'''

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(data=late_shipments, x='pack_price', y='shipment_mode')
plt.show()

#################################################################
#################################################################
#################################################################

'''
Beautiful boxplotting! There certainly looks to be a difference in the pack price between each of the three shipment modes. Do you think the differences are statistically significant?

https://campus.datacamp.com/courses/hypothesis-testing-in-python/pass-me-anova-glass-of-iced-t-2?ex=13
'''
