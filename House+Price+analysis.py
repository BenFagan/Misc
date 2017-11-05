
# coding: utf-8

# In[1]:

import pandas as pandas
import statsmodels.api
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn
from sklearn import preprocessing
get_ipython().magic(u'matplotlib inline')
 
# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)


# In[4]:

cd


# In[5]:

cd desktop


# In[21]:

# data = pandas.read_csv('C:|train.csv')
data = pandas.read_csv('train.csv')
print (data['SalePrice'].describe()) # to check price range


# In[22]:

# quite a difference between mean and median
# grlive first and second floor? God place to start
# don't forget from sklearn to import preprocessing - mean and median is large so we set median and median to same
data['GrLivAreaNorm'] = preprocessing.scale(data['GrLivArea'], with_mean='True', with_std='False')
data['SalePriceNorm'] = preprocessing.scale(data['SalePrice'], with_mean='True', with_std='False')
 
print(data['GrLivAreaNorm'].mean()) # mean of our new area and price
print(data['SalePriceNorm'].mean())
 
# convert variables to numeric format using convert_objects function
data['GrLivAreaNorm'] = pandas.to_numeric(data['GrLivAreaNorm'], errors='coerce')
data['SalePriceNorm'] = pandas.to_numeric(data['SalePriceNorm'], errors='coerce')

# view the centering
data['SalePriceNorm'].diff().hist() # histogram
# diff() = calculate n-th discrete distance


# In[36]:

# linear regression - to prove distribution, is it normal?
scat1 = seaborn.regplot(x="SalePriceNorm", y="GrLivAreaNorm", scatter=True, data=data, line_kws={"linewidth": 0.5, "color": "r"})
plt.xlabel('Sale Price')
plt.ylabel('Above Ground Living Area')
plt.title ('Scatterplot for the Association Between Sale Price and Ground Living Area')
print(scat1)


# In[33]:

print ("OLS regression model for the association between sale price and ground living area")
reg1 = smf.ols('SalePrice ~ GrLivArea', data=data).fit()
print (reg1.summary())
# r squared will tell confidence in model


# In[ ]:

# So about 50% accurate

