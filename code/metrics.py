from math import sqrt
import numpy as np
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import r2_score as R2
from sklearn.utils import check_array

def MAPE(y_true, y_pred):
    # mean_absolute_percentage_error

    return np.mean(np.abs((y_true - y_pred) / y_true))

def RMSE(y_test, y_pred):
    # root_mean_squared_error
    return sqrt(MSE(y_test, y_pred))

def regression_metrics(y_test, y_pred):

    print("MSE: ",MSE(y_test, y_pred))
    print("RMSE:",RMSE(y_test, y_pred))
    print("MAE: ",MAE(y_test, y_pred))
    print("MAPE:",MAPE(y_test, y_pred))
    print("R2:  ",R2(y_test, y_pred))
