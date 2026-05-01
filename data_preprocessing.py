import os 
import pandas as pd 
from sklearn.model_selection import train_test_split    

# ---- Helper functions for data preprocessing -----
# Function to read dataset 
def read_dataset():
    dataset_dir = os.path.join(os.getcwd(), 'sms_dataset')
    df = pd.read_table(dataset_dir, names = ['label', 'message'])
    return df

# Function to split dataset 
def data_split(df, test_size = 0.2, random_state = 1211):
    X = df['message']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state)
    return X_train, X_test, y_train, y_test

# Label Encoding function
def label_encoding(df):
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    return df

# 

# ----------------------------------------------

# Data preprocessing pipeline function
def data_preprocessing(df):
    # 1. Label encoding
    df = label_encoding(df)
    # 2. Split the dataset 
    X_train, X_test, y_train, y_test = data_split(df)

    return X_train, X_test, y_train, y_test