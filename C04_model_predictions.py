# lib neural network algorithms
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU

# lib ensemble learning
from xgboost import XGBRegressor
# ----------------------------------------------------------------------------------------

# func model predictions
def get_models(algorithm, timestep, activation, optimizer, dropout):

  # 1. The LSTM architecture
  if algorithm == "SBi-LSTM":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(LSTM(units=50, activation=activation, return_sequences=True, input_shape=(timestep.shape[1], 1))),
      tf.keras.layers.Bidirectional(LSTM(units=50, activation=activation, return_sequences=False)),
      tf.keras.layers.Dropout(dropout),
      tf.keras.layers.Dense(1)
    ])
  
  # 1. The GRU-RNN architecture
  if algorithm == "SBi-GRU":
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
      tf.keras.layers.Bidirectional(GRU(units=50, activation=activation, return_sequences=True, input_shape=(timestep.shape[1], 1))),
      tf.keras.layers.Bidirectional(GRU(units=50, activation=activation, return_sequences=False)),
      tf.keras.layers.Dropout(dropout),
      tf.keras.layers.Dense(1)
    ])
  
  # 2. compile models
  model.compile(optimizer=optimizer, loss="mae")

  # return values
  return model
# ----------------------------------------------------------------------------------------

def get_prediction(model, batch_size, epochs, x_train, y_train, x_test, y_test):

  # 3. fitting models
  history = model.fit(

    # input and target data
    x=x_train, y=y_train,

    # set parameter tuning
    batch_size=batch_size, epochs=epochs, verbose="auto", 

    # set validation data
    validation_data=(x_test, y_test),
    shuffle=False, use_multiprocessing=False
  )

  # 4. predict models
  predictions = model.predict(x=x_test, verbose=0)

  # return values
  return history, predictions
# ----------------------------------------------------------------------------------------
