# Imports 
import pandas as pd 
import numpy as np 
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path):
    data = pd.read_csv(path) 
    df = pd.DataFrame(data)
    df.columns = df.columns.str.strip("'")
    return df

def process_data(df, features): 
    if features:
        df_new = df[features]
    df_new = pd.get_dummies(df_new)
    return df_new

def align_cols(df, df_test): 
    # Get missing columns in the test set
    missing_cols = set(df.columns) - set(df_test.columns)
    # Add a missing column in test set with default value equal to 0
    for c in missing_cols:
        df_test[c] = 0
    # Ensure the order of column in the test set is in the same order than in train set
    df_test = df_test[df.columns]
    return df_test

def split_classes(df):
    # Assuming 'class_normal' and 'class_anomaly' are binary columns indicating the class
    normal_data = df[df["class_normal"] == 1]
    anomalies = df[df['class_anomaly'] == 1]
    return normal_data, anomalies 

def remove_classes(df):
    new_df = df.drop(['class_normal', 'class_anomaly'], axis=1)
    return new_df 


def conv_to_float(df): 
    return np.asarray(df).astype(np.float32)

def train_test_split_data(df, df_test): 
    normal_data, anomalies = split_classes(df)
    normal_data_test, anomalies_test = split_classes(df_test)

    # Split the normal data
    X_train, X_temp = train_test_split(normal_data, test_size=0.2, random_state=42)
    X_val, X_test_normal = train_test_split(X_temp, test_size=0.5, random_state=42)

    # Remove 'class_normal' and 'class_anomaly' columns
    X_train = remove_classes(X_train)
    X_val = remove_classes(X_val)
    X_test_normal = remove_classes(X_test_normal)
    X_test_full = remove_classes(df_test)

    # Prepare truth labels for full test set 
    y_test_full = df_test[['class_normal', 'class_anomaly']].values
    y_test_full = y_test_full.astype(int)
    y_test_full = y_test_full[:,1]

    # Fit and transform scaler on training data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_full_scaled = scaler.transform(X_test_full)

    # Transform validation and normal test data
    X_val_scaled = scaler.transform(X_val)
    X_test_normal_scaled = scaler.transform(X_test_normal)

    # Prepare anomaly test data
    X_test_anomaly = anomalies.sample(n=len(X_test_normal))
    X_test_anomaly_scaled = scaler.transform(X_test_anomaly.drop(['class_normal', 'class_anomaly'], axis=1))

    # Combine scaled normal and anomaly samples to create the final test set
    X_test_scaled = np.concatenate([X_test_normal_scaled, X_test_anomaly_scaled])

    # Prepare true labels for the test set
    y_true_normal = np.zeros(len(X_test_normal))
    y_true_anomaly = np.ones(len(X_test_anomaly))
    y_true = np.concatenate([y_true_normal, y_true_anomaly])

    # Convert to float
    X_train = conv_to_float(X_train)
    X_val = conv_to_float(X_val)
    X_train_scaled = conv_to_float(X_train_scaled)
    X_val_scaled = conv_to_float(X_val_scaled)
    X_test_scaled = conv_to_float(X_test_scaled)
    X_test_full_scaled = conv_to_float(X_test_full_scaled)
    X_test_full = conv_to_float(X_test_full)
    y_test_full = conv_to_float(y_test_full)

    return X_train_scaled, X_val_scaled, X_test_scaled, y_true, X_test_full_scaled, y_test_full
