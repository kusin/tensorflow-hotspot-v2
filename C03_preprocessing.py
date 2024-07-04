# lib manipulation data
import numpy as np
import pandas as pd

# lib data preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# ----------------------------------------------------------------------------------------

def normalized(dataset, features):
  # 1. memilih features
  data = dataset.filter(features)
  data = data.values
  
  # 2. normalisasi min-max
  scaler = MinMaxScaler(feature_range=(-1,1))
  scaled = scaler.fit_transform(np.array(data))

  return scaler, scaled
# ----------------------------------------------------------------------------------------

def splitting(scaled):

  # # split data train and test
  # train_data, test_data = train_test_split(scaled, train_size=0.80, test_size=0.20, shuffle=False)
  
  # set training data
  train_size = 216
  train_data = scaled[0:train_size,:]

  # set testing data
  test_data = scaled[train_size:len(scaled),:]
  
  return train_data, test_data
# ----------------------------------------------------------------------------------------
