import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import ElasticNetCV
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
from math import sqrt

dic = {}
lst_reg = []
lst_rms = []
lst_r2 = []
lst_vs = []
lst_mae = []

def display(reg, reg_name):
    reg=reg.fit(x_train,y_train)
    y_pred=reg.predict(x_test)
    r2 = reg.score(x_test,y_test)
    
    lst_reg.append(reg_name)    
        
    rms = sqrt(mean_squared_error(y_test, y_pred))
    #print("The Root mean square error for the Regressor is: "+str(rms))
    rms = round(rms,2)
    lst_rms.append(str(rms))
    
    r2 = r2_score(y_test,y_pred)
    #print("r squared value: "+str(r2))
    r2 = round(r2,2)
    lst_r2.append(r2)
    
    var_score = explained_variance_score(y_test,y_pred)
    #print("Variance Score: "+str(var_score))
    var_score = round(var_score,2)
    lst_vs.append(var_score)
    
    mean_abs_error=mean_absolute_error(y_test,y_pred)
    #print("Mean Absolute Error: "+str(mean_abs_error))
    mean_abs_error = round(mean_abs_error,2)
    lst_mae.append(mean_abs_error)
    
    #print(reg.coef_,reg.intercept_)
    
    dic['Regressor'] = lst_reg
    dic['RMSE'] = lst_rms
    dic['R Square'] = lst_r2
    dic['Var Score'] = lst_vs
    dic['Mean Abs Err'] = lst_mae

d= pd.read_csv("Test_Correlation_transform_weka.csv")
col_names=d.columns.values
train =d.values
target = train[:,-1:]
train = train[:,1:-1]
x_train,x_test,y_train,y_test=train_test_split(train,target,test_size=0.4,random_state=0)

target = np.ravel(target)
#print(target.shape)
y_train = np.ravel(y_train)
y_test = np.ravel(y_test)

reg=LinearRegression(fit_intercept=True)
rname = "LinearRegression"
display(reg,rname)

reg=SGDRegressor(loss="squared_loss",penalty=None,random_state=33)
rname = "SGDRegressor"
display(reg,rname)

reg=SGDRegressor(loss="squared_loss",penalty='l1',random_state=33)
rname = "SGDRegressor L1"
display(reg,rname)

reg=SGDRegressor(loss="squared_loss",penalty='l2',random_state=33)
rname = "SGDRegressor L2"
display(reg,rname)

reg=LassoCV(fit_intercept=True)
rname = "LassoCV"
display(reg,rname)


reg=RidgeCV(fit_intercept=True)
rname = "RidgeCV"
display(reg,rname)

reg=ElasticNetCV(fit_intercept=True)
rname = "ElasticNetCV"
display(reg,rname)

reg=SVR(kernel="linear")
rname = "SVR Linear"
display(reg,rname)

reg=SVR(kernel="poly")
rname = "SVR Poly"
display(reg,rname)

reg=SVR(kernel="rbf")
rname = "SVR rbf"
display(reg,rname)

reg=RandomForestRegressor(n_estimators=10)
rname = "RandomForestRegressor"
display(reg,rname)
print()

reg=ExtraTreesRegressor(n_estimators=10)
rname = "ExtraTreesRegressor"
display(reg,rname)

reg=BaggingRegressor(n_estimators=10)
rname = "BaggingRegressor"
display(reg,rname)

data_frame = pd.DataFrame(dic, columns = dic.keys())
print(data_frame)