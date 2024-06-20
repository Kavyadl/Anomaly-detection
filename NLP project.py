#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

dataset = pd.read_csv('./rain.csv')

dataset.head()


# In[11]:


import seaborn as sns

sns.lineplot(dataset["Daily Rainfall Total (mm)"])


# In[10]:


sns.lineplot(dataset["Maximum Temperature (°C)"])


# In[9]:


sns.lineplot(dataset["Max Wind Speed (km/h)"])


# In[3]:


import pandas as pd
from sklearn.ensemble import IsolationForest

# Load your dataset into a pandas DataFrame (assuming it's already loaded)
df = pd.read_csv('./rain.csv')

# Extract relevant features (you can adjust this based on your dataset)
features = ['Daily Rainfall Total (mm)', 'Highest 30 min Rainfall (mm)', 'Highest 60 min Rainfall (mm)', 
            'Highest 120 min Rainfall (mm)', 'Mean Temperature (°C)', 'Maximum Temperature (°C)', 
            'Minimum Temperature (°C)', 'Mean Wind Speed (km/h)', 'Max Wind Speed (km/h)']

# Create feature matrix X
X = df[features]

# Initialize the Isolation Forest model
isolation_forest = IsolationForest(contamination=0.05)  # Adjust contamination based on your dataset

# Fit the model
isolation_forest.fit(X)

# Predict anomalies (1 for normal, -1 for anomalies)
anomaly_predictions = isolation_forest.predict(X)

# Add anomaly predictions to the DataFrame
df['Anomaly'] = anomaly_predictions

# Print the detected anomalies
print("Detected Anomalies:")
print(df[df['Anomaly'] == -1])


# In[ ]:




