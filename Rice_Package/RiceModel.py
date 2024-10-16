import pandas as pd
# from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error , mean_squared_error,accuracy_score
from sklearn.neighbors import KNeighborsClassifier

class riceknn:

    df = pd.read_csv("FinalRice.csv")
    X = pd.DataFrame(df, columns=[ 'Area', 'Perimeter', 'Major_Axis_Length','Minor_Axis_Length', 'Eccentricity', 'Convex_Area', 'Extent'])
    y=pd.Series(df["Class"])

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=32)
    # model_knn = KNeighborsClassifier()
    # model_knn.fit(X_train, y_train)
    # y_hat=model_knn.predict(X_test)
    # s=accuracy_score(y_test,y_hat)     # 0.8971668415529905
    finalmodel= KNeighborsClassifier()
    finalmodel.fit(X,y)

    # from joblib import dump , load
    # dump(finalmodel,"KNNforRice.joblib")
