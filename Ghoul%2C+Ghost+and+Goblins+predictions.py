
# coding: utf-8

# In[13]:

import numpy as np
import pandas as pd 
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[14]:

cd


# In[15]:

cd desktop


# In[16]:

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


# In[17]:

train.head()


# In[18]:

sns.pairplot(train.drop("id", axis=1), hue="type", markers=["o", "s", "D"], diag_kind="kde")
# don't forget matplotline to make the plots distinct - operates like matplotlib


# In[19]:

X_train = pd.get_dummies(train.drop(["id","type"], axis=1)) # drop id and type from the set
y_train = train["type"] # specify type

X_test = pd.get_dummies(test.drop(["id"], axis=1))
X_train.head()


# In[22]:

from sklearn.model_selection import train_test_split


# In[10]:

from sklearn.metrics import classification_report


# In[11]:

y_pred = model.predict(X_val)
y_pred = np.argmax(y_pred, axis=1)
y_pred # print


# In[ ]:



