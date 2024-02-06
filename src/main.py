import data.misc as misc
misc.print_intro()
# Imports 
import warnings
warnings.filterwarnings('ignore')
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' #hides annoying TF messages during import
import joblib
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import data.data_preprocessing as pp 
import models.train_model as model 
import models.predict_model as predict 

print("--------------------------")
print("Loading data")
df = pp.load_data('../data/raw/KDDTrain+.csv')
df_test = pp.load_data('../data/raw/KDDTest+.csv')

selected_features = ['logged_in', 'count', 'serror_rate', 
					  'srv_serror_rate', 'same_srv_rate', 
					  'dst_host_srv_count', 'dst_host_same_srv_rate', 
					  'dst_host_serror_rate', 'dst_host_srv_serror_rate', 
					  'rerror_rate', 'srv_rerror_rate', 'diff_srv_rate', 
					  'dst_host_count', 'dst_host_diff_srv_rate', 'class']

print("--------------------------")
print("Preprocessing data")
df = pp.process_data(df, selected_features)
df_test = pp.process_data(df_test, selected_features)
df_test = pp.align_cols(df, df_test)

print("Using the following features in the training:")
print(selected_features)

X_train_scaled, X_val_scaled, X_test_scaled, y_true, X_test_full_scaled, y_test_full = pp.train_test_split_data(df, df_test)
print("--------------------------")
print("Preprocessing done")
print("--------------------------")

print("Training model now:")

input_dim = X_train_scaled.shape[1]
encoding_dim = 6  # or choose a different size for the encoding layer

autoencoder = model.build_model(input_dim)
model.print_model(autoencoder)
model.visualise_model(autoencoder)


# Specify a learning rate
learning_rate = 0.01
epochs = 20
batch_size = 256
shuffle = True


history = model.train_model(autoencoder, X_train_scaled, X_val_scaled, 
					  learning_rate, epochs, batch_size, shuffle)

print("Model trained successfully")
print("--------------------------")

threshold = 0.95
print("Metrics:")
print("--------------------------")
reconstruction_error, y_pred = predict.predict_model(autoencoder, threshold, X_test_scaled, y_true)
print("--------------------------")
print("Plotting losses:")
predict.plot_losses(history)
print("--------------------------")
print("Plotting reconstruction error:")
predict.plot_reco_error(reconstruction_error, y_true)
print("--------------------------")
print("Producing threshold scan:")
predict.threshold_scan(reconstruction_error, y_true)

