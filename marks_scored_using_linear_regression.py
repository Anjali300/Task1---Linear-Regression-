# -*- coding: utf-8 -*-
"""Marks Scored Using Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d8Wxh4H-CQaxplnLwkqtX860mBKVlpC0

**Task1 Under GRIP @TSF 
BY- Anjali Garg**

**Importing all libraries required in the notebook**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

"""**Redaing the data from remote link**"""

url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

s_data.head(10)

"""**Plotting the distribution of scores**"""

s_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

"""**Splitting the X and Y values**"""

X = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values

"""**Splitting the training and testing part**

"""

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=0)

"""**Training the model**"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

print("Training complete.")

"""**Plotting the regression line**"""

line = regressor.coef_*X+regressor.intercept_

"""**Plotting the test data**"""

plt.scatter(X, y)
plt.plot(X, line);
plt.show()

print(X_test) # Testing data - In Hours
y_pred = regressor.predict(X_test) # Predicting the scores

"""**Comparing Actual vs Predicted**"""

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df

"""**Testing the model on your own data**"""

hours = np.array([9.25]) # No. of hours should be mentioned inside array
hours = hours.reshape(-1,1)
own_pred = regressor.predict(hours)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))

"""**Accuracy of Model**"""

print(regressor.score(X_test, y_test))

"""**Thank you**"""