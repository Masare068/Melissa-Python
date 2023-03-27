#!/usr/bin/env python
# coding: utf-8

# VISUALIZING THE FIRST FIVE ROWS OF OUR DATASET

# In[138]:


import pandas as pd
data=pd.read_csv(r"C:\Users\King Freddie\Desktop\data.csv")

#visualizing the first five ROWS
data.head()


# In[139]:


import seaborn as sns


# PREPROCESSING TO ELIMINATE AND NULL VALUES DUPLICATES

# In[140]:


#check to find columns with Null values
import numpy as np
NaN_cols=data.columns[data.isna().any()].tolist()
print(NaN_cols)

#Preprocessing to remove the null values by replacing with mean value of column
columns_to_remove_null=['fixed acidity', 'citric acid', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'quality']
for column in columns_to_remove_null:
    mean=int(data[column].mean(skipna=True))
    data[column]=data[column].replace(np.NaN,mean)


# CHECKING TO VERIFY IF NULL VALUES HAVE BEEN REPLACED

# In[141]:


NaN_cols=data.columns[data.isna().any()].tolist()
print(NaN_cols)


# CHECKING DATASET FOR DUPLICATE VALUES

# In[142]:


#checking for duplicates
duplicates=data[data.duplicated()]
print(duplicates)
data.duplicated().sum()
#output shows there is no duplicate
#eliminating duplicates from the dataframe just to be sure
data.drop_duplicates(inplace=True)


# #There were null values. The first step was to identify columns with null values The method employed was to replace the null values with the 
# #mean of the entire colums. This was calculated using np.mean for each column using the no-null values.
# #The reason for using this was
# #1. To maintain the distribution of the data
# #2. To reduce bias
# 
# 
# 

# STATISTIACAL INFERENCE OF ENTIRE DATASET

# In[143]:


#Obtain statistical inference of the entire dataset
data=data.drop('ID',axis=1)
data.describe()


# The table above gives statitical desriptions of the entire dataset.
# The statistical parameters used were the count, standard deviation, minimum value, 25th percentile, 50th percentile, 75th percentile and the maximum value.
# INFERENCES
# 1. Fixed acidity had the highest mean distribution
# 2. The count for all columns were equal
# 3. The maximum value obtained was from the total sulphur dioxide column
# 

# STATISTICAL INFERENCES FOR INDIVIDUAL COLUMN

# In[144]:


data['pH'].describe()


# In[145]:


data['citric acid'].describe()


# In[146]:


data['fixed acidity'].describe()


# In[147]:


data['residual sugar'].describe()


# In[148]:


data['free sulfur dioxide'].describe()


# In[149]:


data['total sulfur dioxide'].describe()


# In[150]:


data['volatile acidity'].describe()


# In[151]:


data['citric acid'].describe()


# In[152]:


data['chlorides'].describe()


# In[153]:


data['density'].describe()


# In[154]:


data['pH'].describe()


# In[155]:


data['sulphates'].describe()


# In[156]:


data['quality'].describe()


# HIDDEN INFERENCES IN DATASET

# In[157]:


#Stastistical inference for individual column.
sns.distplot(data['quality'])


# The plot above shows the distribution plot of the quality column
# INFERENCES
# 1. Quality of 5 had the highest distribution followed by 6, 7 ,4 8 and 3 respectively
# 2. The highest density of quality obtained was 2.5
# 

# In[158]:


data.hist(figsize=(10,10))


# The histogram above illustrates the density distribution of the various variables. 
# INFERENCES
# 1. The distribution of residual sugar, total sulphur dioxide, free sulphur dioxide were skewed to the left.
# 
# 2. The skewness indicated that these variables had modes greater than median value and in turn greater than the mean of the distribution.

# OBTAINING HIDDEN STATISTICAL INFERENCES FROM PH COLUMN

# In[159]:


#showing hidden inferences
data['pH'].describe()


# USING THE PH STATISTICS TO DETERMINE THE LEVEL OF ACIDITY OF THE WINE
# WHERE THE MIN VALUE CORRESPOND TO HIGH ACIDITY IN REFERENCE TO THE PH SCALE

# In[160]:


data['acidity_levels']=pd.cut(x=data['pH'],bins=[2.740000,3.210000,3.310000,3.400000,4.010000],
                             labels=['High','Moderately High','Medium','Low'],include_lowest=True)


# GROUPING THE ACIDITY LEVELS WITH THE MEAN OF THE QUALITY

# In[161]:


data1=data.groupby(by='acidity_levels')['quality'].mean()
data1.head()


# INFERENCES
# 1. Wine with high acidity levels had a high mean quality
# 2. Wine with loe acidity levels had a low mean quality

# In[162]:


data['alcohol'].describe()


# THE CODE ABOVE SHOWS THE STATISTICAL VALUES OF THE ALCOHOL COLUMN
USING QUERY METHOD TO FIND ALCOHOL LESS THAN THE MEDIAN
# In[165]:


low_alcohol=data.query('alcohol< 10.200000')
low_alcohol.head()


# USING QUERY METHOD TO FIND ALCOHOL GREATER THAN THE MEDIAN

# In[166]:


high_alcohol=data.query('alcohol >= 10.200000')
high_alcohol.head()


# FINDING THE MEAN QUALITY OF THE LOW ALCOHOL AND HIGH ALCOHOL

# In[167]:


high_alcohol['quality'].mean()


# In[168]:


low_alcohol['quality'].mean()


# HIDDEN INFERENCE
# 1. Wine with low alcohol had a lower mean quality as compared with wine with high alcohol
# 2. This means wine with high alcohol received better ratings as compared to wine with lower alcohol content

# FINDING HIDDEN STATISTICAL INFERNECE OF RESIDUAL SUGAR 

# In[169]:


data['residual sugar'].describe()


# USING QUERY TO FIND WINE WITH RESIDUAL SUGAR GREATER THAN THE MEDIAN

# In[170]:


data=data.rename(columns={'residual sugar':'residual_sugar'})
wine_more_sugar=data.query('residual_sugar >=  2.200000')


# USING QUERY TO FIND WINE WITH RESIDUAL SUGAR LESSER THAN THE MEDIAN

# In[171]:


wine_less_sugar=data.query('residual_sugar <  2.200000')


# FINDING THE RATING OF WINE WITH MORE SUGAR AND LESS SUGAR

# In[172]:


wine_more_sugar['residual_sugar'].mean()


# In[173]:


wine_less_sugar['residual_sugar'].mean()


# INFERENCE
# 1. Wine with more residual sugar had a mean of 3.1577240566037736 higher than wine with less residual sugar
# 2. This shows that sweeter wines received more ratings

# FINDING CORRELATION BETWEEN THE VARIABLES

# In[174]:


#checking to find correlation between components
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
sns.heatmap(data.corr(),annot=True)
#From the plot 1 indicates high correlation.


# INFERENCES
# 1. Correlation number of 1 indicated high correlation between variables.
# 2. There was no correlation between pH and fixed acidity. This is because even if the pH changed the fixed acidity prevents the acidity from changing regardless
# 3. Highest correlation was obtained for same variables.

# In[ ]:




