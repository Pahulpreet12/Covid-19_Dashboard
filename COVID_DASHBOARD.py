#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import os


# In[2]:


path1="C:\\Users\\HP\\Desktop\\here\\projects\\covid_dashboard\\covid_19_india.csv"
path2="C:\\Users\\HP\\Desktop\\here\\projects\\covid_dashboard\\covid_vaccine_statewise.csv"
path3="C:\\Users\\HP\\Desktop\\here\\projects\\covid_dashboard\\StatewiseTestingDetails.csv"


# In[3]:


df1=pd.read_csv(path1)
df1.drop(columns=['ConfirmedIndianNational','ConfirmedForeignNational'],inplace=True)
df1.head()


# In[4]:


df2=pd.read_csv(path2)
df2.head()


# In[5]:


#print(df2.columns)


# In[6]:


df2.drop(columns=['Sessions',' Sites '],inplace=True)
import numpy as np
df2.replace({np.nan:0},inplace=True)


# In[7]:


df2.drop(columns=['Male (Doses Administered)', 'Female (Doses Administered)','Transgender (Doses Administered)'],inplace=True)
df2.drop(columns=['Male(Individuals Vaccinated)','Female(Individuals Vaccinated)', 'Transgender(Individuals Vaccinated)'],inplace=True)


# In[8]:


df2.head()


# In[9]:


df3=pd.read_csv(path3)
df3.replace({np.nan:0},inplace=True)
df3.head()


# In[10]:


fig1=px.line(df1,x='Date',y='Confirmed',color="State/UnionTerritory",hover_name="State/UnionTerritory",title='Statewise cases')
fig1.show()


# In[11]:


fig2=px.line(df1,x='Date',y='Deaths',color="State/UnionTerritory",hover_name="State/UnionTerritory",title='Statewise Deaths')
fig2.show()


# In[ ]:





# In[12]:


df = df2.query("State=='India'")
df = df[(df['First Dose Administered']>0)]
fig3=px.line(df,x='Updated On', y=['First Dose Administered','Second Dose Administered'],title='NUMBER OF VACCINES ADMINISTERED')
fig3.show()


# In[ ]:





# In[13]:


df = df2.query("State=='India'")
df = df[(df[' Covaxin (Doses Administered)']>0)]
fig4=px.line(df,x='Updated On', y=[' Covaxin (Doses Administered)', 'CoviShield (Doses Administered)',
       'Sputnik V (Doses Administered)'],title='VACCINE TYPE ADMINISTERED')
fig4.show()


# In[14]:


print(df2.columns)


# In[15]:


df = df2.query("State=='India'")
#df = df[(df['60+ Years (Doses Administered)']>0)]
fig5=px.line(df,x='Updated On', y=['18-44 Years (Doses Administered)', '45-60 Years (Doses Administered)',
       '60+ Years (Doses Administered)', '18-44 Years(Individuals Vaccinated)',
       '45-60 Years(Individuals Vaccinated)',
       '60+ Years(Individuals Vaccinated)'],title='DOSES ADMINISTERED AGEWISE')
fig5.show()


# In[16]:


df3.columns


# In[17]:


fig6=px.line(df3,x='Date', y=['TotalSamples', 'Positive'],color='State',title='STATEWISE POSITIVE')
fig6.show()


# In[ ]:


app = dash.Dash()

app.layout=html.Div([
    html.H1(children='DASHBOARD PROJECT',style={'text-align': 'center', 'background-color': 'rgb(230, 180, 180)','margin-top':'0'}),
    html.H1('COVID-19',style={'text-align': 'center', 'background-color': 'rgb(130, 255, 120)'}),
    html.H2('Visualization of Covid-19 trends in India',style={'text-align': 'center', 'background-color': 'rgb(130, 255, 120)'}),
    html.Hr(),
    html.Hr(),
    html.Div(children=[
        dcc.Graph(id="graph1",figure=fig1, style={'display': 'inline-block'}),
        dcc.Graph(id="graph2",figure=fig2, style={'display': 'inline-block'})
    ]),
    html.Hr(),
    html.Div([
        dcc.Graph(id="graph3",figure=fig3, style={'display': 'inline-block'}),
        dcc.Graph(id="graph6",figure=fig4, style={'display': 'inline-block'})
    ]),
    html.Div(children=[
        dcc.Graph(id="graph4",figure=fig5, style={'display': 'inline-block'}),
        dcc.Graph(id="graph5",figure=fig6, style={'display': 'inline-block'})
    ],style={'background-color':'rgb(60, 58, 37)'}),
    html.Hr()
],style={'text-align': 'center', 'border':'black,solid,14.25px','background-color': 'rgb(185,130, 46)','margin-top':'0','font-style': 'italic','position': 'relative','top': '25px','border-radius': '15px'})



if __name__ == "__main__":
    app.run_server()
    

