# lib data manipulation 
import pandas as pd

# function load dataset
def data_hotspot(df):

  # load dataset
  dataset = pd.read_csv("dataset/"+df, parse_dates=['acq_date'])
  dataset = dataset[["acq_date", "hotspot", "sst_anom", "oni_anom", "soi_anom"]]
  
  # return values
  return dataset