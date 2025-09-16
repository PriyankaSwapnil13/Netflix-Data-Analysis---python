#!/usr/bin/env python
# coding: utf-8

# # Netflix
# 
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('Netflix project.csv')


# In[3]:


data


# # 1.Head()
# 

# In[4]:


data.head()


# # 2.Tail()

# In[5]:


data.tail()


# # 3.Shape

# In[6]:


data.shape


# # 4.Size

# In[8]:


data.size


# # 5.Columns

# In[9]:


data.columns


# # 6.dtypes

# In[10]:


data.dtypes


# # 7.Info()

# In[11]:


data.info()


# # 8. duplicate() - find duplicate values and remove the duplicates records.

# In[12]:


data.head()


# In[13]:


data.shape


# In[14]:


data.duplicated()


# In[15]:


data[data.duplicated()]


# In[17]:


data.drop_duplicates()


# In[18]:


data.drop_duplicates(inplace = True)  # To remove the duplicate rows permanently


# In[19]:


data[data.duplicated()]


# In[20]:


data.shape


# # 9. isnull()

# In[21]:


data.head()


# In[22]:


data.isnull()


# In[23]:


data.isnull().sum()     #It show the count of null values


# # seaborn library (heat-map)

# In[4]:


import seaborn as sns


# In[26]:


sns.heatmap(data.isnull())


# # Q1. For 'House of cards', What is the show id and who is the director of this show?

# # isin()

# In[28]:


data.head()


# In[29]:


data['Title']


# In[30]:


data['Title'].isin(['House of Cards']) #To show all records of a particular items in any column


# In[32]:


data[data['Title'].isin(['House of Cards'])]


# # str.contains()

# In[33]:


data[data['Title'].str.contains('House of Cards')] #To show all records of a particular string in any column


# # Q2. In which year highest number of the TV shows & movies were relased? show with Bar graph.

# In[6]:


data.dtypes


# # to_datetime

# In[4]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[5]:


data.head()


# In[38]:


data.dtypes


# # dt.year.value_counts()

# In[11]:


data['Date_N'].dt.year.value_counts()                             #it counts the occurence of all individual years in date column


# # Bar Graph

# In[10]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# # Q3.How many movies & TV shows are in the dataset? show with Bar Graph.

# # groupby()

# In[11]:


data.head(2)


# In[12]:


data.groupby('Category').Category.count()


# # countplot()

# In[20]:


sns.countplot(x='Category', data=data)
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()


# # Q4. Show all the movies that were release in year 2000.

# # Creating new column

# In[21]:


data.head(2)


# In[15]:


data['Year'] = data['Date_N'].dt.year


# In[16]:


data.head(2)


# # Filtering

# In[28]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]


# In[29]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2020)]


# # Q5. Show only the Title of all TV shows that were released in India only.

# # Filtering

# In[37]:


data.head(2)


# In[44]:


data[(data['Category']=='TV show') & (data['Country']=='India')]['Title']
print(data)


# # Q6. Show Top 10 Directors, who gave the highhest number of TV shows & movies to Netflix?

# In[5]:


data.head()


# In[6]:


data['Director'].value_counts()


# In[9]:


data['Director'].value_counts().head(10)


# # Q7. Show all the records, where "Category is movie and type is comedies" or "country is united kingdom".

# # Filtering (And, or Operators)

# In[10]:


data.head(2)


# In[12]:


data[ (data['Category']=='Movie') & (data['Type']=='Comedies')]


# In[15]:


data[ (data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# # Q8. In how many movies/shows, Tom Cruise was cast?

# In[17]:


data.head(2)


# In[18]:


data[data['Cast'] == 'Tom Cruise']


# # str.contains()

# In[19]:


data_new = data.dropna()   # It drops the rows that contains all or any missing values.


# In[20]:


data_new.head(2)


# In[21]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# # Q9. What are the different ratings defined by Netflix?

# # nunique()

# In[22]:


data.head(2)


# In[23]:


data['Rating'].nunique()


# # unique

# In[24]:


data['Rating'].unique()


# # Q9.1. How many movies got the 'TV-14' rating, in canada?

# In[25]:


data.head(2)


# In[26]:


data[ (data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') ]


# In[27]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14')].shape


# In[28]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country']=='Canada')]


# # Q9.2. How many TV show got the 'R' rating, after year 2018?

# In[17]:


data.head(2)


# In[18]:


data[ (data['Category'] == 'TV Show') & (data['Rating'] == 'R') ]


# In[19]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]


# # Q10. What is the maximum duration of a Movie/Show on netflix?

# In[20]:


data.head(2)


# # data.Duration.unique()

# In[22]:


data.Duration.dtype


# # str.split()

# In[23]:


data.head(2)


# In[25]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ',expand = True)


# In[26]:


data.head(2)


# In[27]:


data['Minutes']


# In[28]:


data['Minutes'].max()


# In[29]:


data['Minutes'].min()


# In[30]:


data.dtypes


# # Q11. Which individual country has the highest no. of TV Show?

# In[31]:


data.head(2)


# In[32]:


data_tvshow = data[data['Category'] == 'TV Show']


# In[33]:


data_tvshow.head(2)


# In[34]:


data_tvshow.Country.value_counts()


# In[35]:


data_tvshow.Country.value_counts().head(1)


# # Q12. How can we sort the dataset by Year?

# In[36]:


data.head(2)


# In[37]:


data.sort_values(by = 'Year')


# In[39]:


data.sort_values(by = 'Year', ascending = False).head(10)


# # Q13. Find all the instances where:

# # Category is 'Movie' and Type is 'Dramas'

# # or

# # Category is 'TV Show' & Type is 'Kids'TV'

# data.head(2)

# In[41]:


data.head(2)


# In[42]:


data[(data['Category']=='Movie') & (data['Type']=='Dramas')].head(2)


# In[44]:


data[(data['Category']=='TV Show') & (data['Type']=="Kids' TV")]


# In[45]:


data[ (data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']=="Kids' TV") ]


# In[ ]:




