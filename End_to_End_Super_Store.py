#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[13]:


pd.set_option('display.float_format', lambda x: '%.3f' %x)


# In[14]:


import warnings


# In[15]:


warnings.filterwarnings('ignore')


# # Gather and Clean Data

# In[18]:


df=pd.read_csv("C:\\Users\\ITS\\OneDrive\\Desktop\\superstore_dataset.csv", encoding='ISO-8859-1')


# In[19]:


df.head()


# # Check Columns Name

# In[20]:


df.columns


# # Find Shape of Dataset

# In[23]:


df.shape


# # Check Dataset Info

# In[26]:


df.info()


# # Chcek The Null Values

# In[27]:


df.isnull()


# In[28]:


df.isnull().sum()


# In[29]:


df.duplicated().any()


# # Get OverAll Statistics

# In[30]:


df.describe()


# # Drop Unnecessary Columns
Hypothesis 1: Technology products have the highest profit margin compared to other product categories.
Hypothesis 2: The East region has the highest sales compared to other regions.
Hypothesis 3: Sales are higher during certain months of the year.
Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products.
Hypothesis 5: The company's profit is more on weekdays than on weekends.

# In[31]:


df.columns


# In[32]:


df=df.drop(['Row ID','Order ID','Customer ID','Postal Code'], axis=1)


# In[33]:


df


# In[34]:


df.columns


# # Technology products have the highest profit margin compared to other product categories.
# 

# In[38]:


cat_prof=df.groupby('Category')['Profit'].sum()


# In[39]:


cat_prof


# In[41]:


cat_prof.plot(kind='bar')
plt.title("Profit BY Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()


# # The East region has the highest sales compared to other regions.
# 

# In[42]:


df.columns


# In[45]:


east_region=df.groupby('Region')['Sales'].sum()


# In[46]:


east_region


# In[48]:


east_region.plot(kind='bar')
plt.title("Total Sale by Region")
plt.xlabel("Region")
plt.ylabel("Total Sale")
plt.show()


# # Sales are higher during certain months of the year.
# 

# In[49]:


df.columns


# In[50]:


df['Order Month']=pd.DatetimeIndex(df['Order Date']).month


# In[51]:


moth_sale=df.groupby('Order Month')['Sales'].sum()


# In[52]:


moth_sale


# In[53]:


moth_sale.plot(kind='bar')
plt.title("Total Sale by Month")
plt.xlabel("Month")
plt.ylabel("Total Sale")
plt.show()


# # Orders with same-day shipping have the lowest rate of returned products.
# 

# In[54]:


df.columns


# In[55]:


total_order_by_ship_mode=df.groupby('Ship Mode').size()


# In[56]:


total_order_by_ship_mode


# In[57]:


returned_orderbyshipe=df[df['Profit']<0].groupby('Ship Mode').size()


# In[58]:


returned_orderbyshipe


# In[59]:


retr_per_byshipe_mode=(returned_orderbyshipe/total_order_by_ship_mode)*100


# In[60]:


retr_per_byshipe_mode


# In[62]:


retr_per_byshipe_mode.plot(kind='bar')
plt.title("Return Per By Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Return Per")
plt.show()


# # The company's profit is more on weekdays than on weekends.

# In[63]:


df.columns


# In[64]:


df['Order_day']=pd.DatetimeIndex(df['Order Date']).day_name()


# In[65]:


df


# In[66]:


day_profit=df.groupby('Order_day')['Profit'].sum()


# In[67]:


day_profit


# In[69]:


day_profit.plot(kind='bar')
plt.title("Total Profit by The Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Total Profit")
plt.show()


# In[ ]:




