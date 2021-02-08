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
    return MSE(y_test, y_pred, squared=False)

def regression_metrics(y_test, y_pred, verbose=False):

    mse = MSE(y_test, y_pred)
    rmse = RMSE(y_test, y_pred)
    mae = MAE(y_test, y_pred)
    mape = MAPE(y_test, y_pred)
    r2 = R2(y_test, y_pred)
    
    if verbose==True:
        print("MSE: ",mse)
        print("RMSE:",rmse)
        print("MAE: ",mae)
        print("MAPE:",mape)
        print("R2:  ",r2)
        
    return r2
