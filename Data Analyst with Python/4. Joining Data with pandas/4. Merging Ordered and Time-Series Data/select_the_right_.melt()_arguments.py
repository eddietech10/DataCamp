'''
Select the right .melt() arguments:

You are given a table named inflation. Chose the option to get the same output as the table below.

   country    indicator  year  annual
0   Brazil  Inflation %  2017    3.45
1   Canada  Inflation %  2017    1.60
2   France  Inflation %  2017    1.03
3    India  Inflation %  2017    2.49
4   Brazil  Inflation %  2018    3.66
5   Canada  Inflation %  2018    2.27
6   France  Inflation %  2018    1.85
7    India  Inflation %  2018    4.86
8   Brazil  Inflation %  2019    3.73
9   Canada  Inflation %  2019    1.95
10  France  Inflation %  2019    1.11
11   India  Inflation %  2019    7.66
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

# Possible Answers:

inflation.melt(id_vars=['country','indicator'], var_name='annual')

inflation.melt(id_vars=['country'], var_name='indicator', value_name='annual')

inflation.melt(id_vars=['country','indicator'], var_name='year', value_name='annual')

inflation.melt(id_vars=['country'], var_name='year', value_name='annual')