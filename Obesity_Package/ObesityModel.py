import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class myKNN:
    # def PredictionKNN(self,newdata):
    #     return (self.model_knn.predict_proba(newdata).max())*100

    df = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")
    X=df.drop("NObeyesdad",axis=1)
    y=df["NObeyesdad"]

    X['Gender'].replace({'Female': 1,'Male': 2}, inplace=True)
    X['family_history_with_overweight'].replace({'yes': 1,'no': 2}, inplace=True)
    X['FAVC'].replace({'yes': 1,'no': 2}, inplace=True)
    X["CAEC"].replace({"no":1,"Sometimes" :2 , "Frequently" :3,"Always" : 4}, inplace=True)
    X["CALC"].replace({"no":1,"Sometimes" :2 , "Frequently" :3,"Always" : 4}, inplace=True)
    X['SMOKE'].replace({'yes': 1,'no': 2}, inplace=True)
    X["MTRANS"].replace({"Automobile":1,"Motorbike" :2 , "Public_Transportation" :3,"Walking" : 4,"Bike":5}, inplace=True)
    X["SCC"].replace({"yes":1,"no" : 2},inplace=True)
# print(X.head().to_string())


    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=32)
# fit model
    model_knn = KNeighborsClassifier()
    model_knn.fit(X, y)
    # data=[1,21,1.62,64,1,0,2,3,2,2,2,2,0,1,1,3]
    # predictions = model_knn.predict([data])
    # print(predictions)
# listmy = [max(i) for i,j in predictions.tolist()]
# print(predictions)
# print(listmy)
# print(model_knn.predict_proba(newdata).max().index())
# print(model_knn.score(X, y))
#     def PredictionKNN(self,newdata):
#         # return (model_knn.predict_proba(newdata).max())*100
#         return

    from joblib import dump , load
    dump(model_knn,"KNNforObesity.joblib")

