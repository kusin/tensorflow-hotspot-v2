# libs manipulations array
import numpy as np

# lib evaluate models
import scipy.stats as sc
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

# func evaluate models
def evaluate_models(ytrue, ypred):

  # calculate r and p-value
  r = sc.mstats.pearsonr(ytrue, ypred)[0]
  p = sc.mstats.pearsonr(ytrue, ypred)[1]

  # calculate mae
  mae = mean_absolute_error(ytrue, ypred)

  # calculate rmse
  rmse = root_mean_squared_error(ytrue, ypred)

  # calculate mape
  mape = mean_absolute_percentage_error(ytrue, ypred)

  # return values
  return np.round(r,4), np.round(p,4), np.round(mae,4), np.round(rmse,4), np.round(mape,4)