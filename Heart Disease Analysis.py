#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\user\Downloads\archive (1)\heart.csv")


# In[3]:


#First five rows of dataset
data.head()


# In[4]:


#Last five rows of dataset
data.tail()


# In[5]:


#Shape of dataset; Number of rows/columns
data.shape


# In[6]:


print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])


# In[7]:


#Get information about dataset
data.info()


# In[8]:


#Check for null values
data.isnull().sum()


# In[9]:


#Check for duplicate data
data_dup = data.duplicated().any()
print(data_dup)


# In[10]:


data=data.drop_duplicates()


# In[11]:


data.shape


# In[12]:


#Get overall statistics of data
data.describe()


# In[13]:


#Draw correlation matrix
plt.figure(figsize=(17,6))
sns.heatmap(data.corr(),annot=True)


# In[14]:


#How many people have heart disease and how many people dont
data.columns


# In[15]:


data['target'].value_counts()


# In[16]:


sns.countplot(data['target'])


# In[17]:


#count of male and female
data.columns


# In[18]:


data['sex'].value_counts()


# In[19]:


sns.countplot(data['sex'])
plt.xticks([0,1],['Female','Male'])


# In[20]:


#Find gender distribution among the target variable
data.columns


# In[21]:


sns.countplot(x='sex',hue='target',data=data)
plt.xticks([0,1],['Female','Male'])
plt.legend(labels=['No_Disease','Disease'])
plt.show()


# In[22]:


#Check age distribution in Dataset
sns.distplot(data['age'],bins =20)
plt.show()


# In[23]:


#Check chest pain type
sns.countplot(data['cp'])
plt.xticks([0,1,2,3],['typical angina','atypical angina','non-anginal pain','asymptomatic'])
plt.xticks(rotation=75)
plt.show()


# In[24]:


#Show CHEST PAIN DISTRIBUTION AS PER Target variable
data.columns


# In[25]:


sns.countplot(x='cp',hue='target',data=data)
plt.legend(labels=['No_Disease','Disease'])
plt.show()


# In[26]:


#Show fasting Blood Sugar Distribution According to target variable
sns.countplot(x='fbs',hue='target',data=data)
plt.legend(labels=['No_Disease','Disease'])
plt.show()


# In[27]:


#Check Resting Blood Pressure Distribution
data.columns


# In[28]:


data['trestbps'].hist()


# In[29]:


#Compare RESTING Resting Blood Pressure As per Sex Column
g=sns.FacetGrid(data,hue='sex',aspect=4)
g.map(sns.kdeplot,'trestbps',shade=True)
plt.legend(labels=['Male','Female'])


# In[30]:


#Show distribution of Cholesterol
data.columns


# In[31]:


data['chol'].hist()


# In[32]:


#Plot continuous variables
data.columns


# In[33]:


categorical_val=[]
continuous_val=[]

for col in data.columns:
    if data[col].nunique() <= 10:
        categorical_val.append(col)
    else:
        continuous_val.append(col)


# In[34]:


categorical_val


# In[35]:


continuous_val


# In[36]:


data.hist(continuous_val,figsize=(15,6))
plt.tight_layout()
plt.show()


# In[ ]:




