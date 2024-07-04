# lib manipulation data
import numpy as np
import pandas as pd

# lib data preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# ----------------------------------------------------------------------------------------

# function for normalized min-max
def normalized(dataset, features):
  # 1. memilih features
  data = dataset.filter(features)
  data = data.values
  
  # 2. normalisasi min-max
  scaler = MinMaxScaler(feature_range=(-1,1))
  scaled = scaler.fit_transform(np.array(data))

  return scaler, scaled
# ----------------------------------------------------------------------------------------

# func for splitting data
def splitting(scaled):

  # # split data train and test
  # train_data, test_data = train_test_split(scaled, train_size=0.80, test_size=0.20, shuffle=False)
  
  # 3. set training data
  train_size = 216
  train_data = scaled[0:train_size,:]

  # 3. set testing data
  test_data = scaled[train_size:len(scaled),:]
  
  return train_data, test_data
# ----------------------------------------------------------------------------------------

# function for supervised learning
def process_univariate_supervised(look_back, dataset):
    
  # declare variable X and Y
  dataX = []
  dataY = []
  
  # for loop for create supervised learning
  for i in range(look_back, len(dataset)):
      
    # insert value X and Y 
    dataX.append(dataset[i-look_back:i, 0])
    dataY.append(dataset[i, 0])
      
  # return value X and Y
  return np.array(dataX), np.array(dataY)
# ----------------------------------------------------------------------------------------

# function for supervised learning
def results_univariate_supervised(train_data, test_data):
   
  # set time series lag
  look_back = 1
  
  # process supervised learning
  x_train, y_train = process_univariate_supervised(look_back, train_data)
  x_test, y_test = process_univariate_supervised(look_back, test_data)

  # reshape input to be [samples, time steps, features]
  x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
   
  # return values
  return x_train, y_train, x_test, y_test
# ----------------------------------------------------------------------------------------
