#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

# import plotly as ply

data = pd.read_csv("https://raw.githubusercontent.com/AllanMisasaUCL/SoftwarekonstruktionE21/main/marketing_campaign.csv", sep='\t')
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
data.head()


# In[3]:


data['Income']


# In[4]:


list1 = ['Year_Birth', 'Education', 'Marital_Status', 'Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'NumWebVisitsMonth']
list1 [0]


# In[5]:


årstal = list1[0]
data[årstal]


# In[6]:


def kolonne(tal):
    print("Hvilken kolonne skal vises?")
    valg = list1[tal]
    return data[valg]


# In[7]:


kolonne(2)


# In[11]:


def søjlediagram(tal):
    print("Hvilken graf skal vises?")
    kolonner = data.columns
    valg = kolonner[tal]
    graf = plt.hist(data[valg])
    
def barchart(tal):
    print("Hvilken graf skal vises?")
    kolonner = data.columns
    valg = kolonner[tal]
    graf = plt.bar(data[valg], max(data[valg]))
    
def diagram(tal):
    print("Hvilken graf skal vises?")
    kolonner = data.columns
    valg = kolonner[tal]
    graf = plt.plot(data[valg])
    
#def piechart(tal):
#    print("hvilken graf skal vises?")
#    kolonner = data.columns
#    valg = kolonner[tal]
#    graf = plt.pie(data[valg], startangle=90)

sorteret_indkomst = np.sort(data['Income'])
sorteret_alder = np.sort(data['Year_Birth'])
sorteret_uddannelse = np.sort(data['Education'])
sorteret_forhold = np.sort(data['Marital_Status'])
sorteret_børn = np.sort(data['Kidhome'])
sorteret_teenager = np.sort(data['Teenhome'])
sorteret_sidstebesøg = np.sort(data['Recency'])
sorteret_vin = np.sort(data['MntWines'])


listesort = [sorteret_indkomst, sorteret_alder, sorteret_uddannelse, sorteret_forhold, sorteret_børn, sorteret_teenager, sorteret_sidstebesøg, sorteret_vin]
label = ['Indkomst', 'Alder', 'Uddannelse', 'Forhold', 'Børn hjemme', 'Teenagere hjemme', 'Sidste besøg', 'Vin forbrug på en måned']
def sorteret_diagram():
    print("Hvilken graf skal vises?")
    tal = input()
    valg = listesort[int(tal)]
    graf = plt.plot(valg)


# In[12]:


sorteret_diagram()


# In[13]:


søjlediagram(1)


# In[42]:


plt.plot(sorteret_indkomst)


# In[ ]:





# In[ ]:





# In[ ]:




