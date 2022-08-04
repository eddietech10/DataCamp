'''
Distribution of education
Let's begin comparing incomes for different levels of education in the GSS dataset, which has been pre-loaded for you into a DataFrame called gss. The variable educ represents the respondent's years of education.

What fraction of respondents report that they have 12 years of education or fewer?
'''

#################################################################
'''_____________________... PRACTICE ...______________________'''
#################################################################

'''
What fraction of respondents report that they have 12 years of education or fewer?
'''

#Possible Answers

b = Cdf(gss['educ'])
b[12]
# >0.5322611710323575

'Approximately 22%'

'Approximately 31%'

'Approximately 47%'

# => 'Approximately 53%'



