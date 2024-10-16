import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error , mean_squared_error,accuracy_score
# import numpy as np

# Data Prepration :
df = pd.read_csv("Finalabalone.csv")
X=df.drop("Rings",axis=1)
y=df["Rings"]
# df["Sex"] = df["Sex"].replace({'I': 1,'F': 2,'M': 3})

X['Sex'].replace({'I': 1,'F': 2,'M': 3}, inplace=True)

#  Modeling
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.35,random_state=32)
reg_model = LinearRegression()
reg_model.fit(X_train,y_train)
test_prediction = reg_model.predict(X_test)
y_pred=pd.Series(test_prediction)
ymean = ((y_test-(y_test.mean()))**2).sum()
# print((((y_test - y_pred)**2).sum())/ymean) # 0.65
# print(reg_model.predict([[2,0.47,0.355,0.1,0.4755,0.1675,0.0805,0.185]]))

 # Deployment
final_model = LinearRegression()
final_model.fit(X,y)

# y_hat = final_model.predict(X)
# y_pred2=pd.Series(y_hat)
# ymean1 = ((y-(y.mean()))**2).sum()
# print((((y - y_pred2)**2).sum())/ymean1)

from joblib import dump,load
dump(final_model,'RegForAbandon2.joblib')

# loaded_model = load('sales_model.joblib')
# print(loaded_model.predict([[149,29,29]]))