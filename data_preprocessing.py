import os 
import re
import pandas as pd 
import nltk
from nltk.corpus import stopwords
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

# Text Cleaning Function 
def text_cleaning(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text) 
    text = text.split()
    text = ' '.join(text)
    return text

# Text Tokenization function
def text_tokenization(text):
    return nltk.word_tokenize(text)

# Text Stopword Removal function
def stopword_removal(tokens):
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = []
    for token in tokens:
        if token not in stop_words:
            cleaned_tokens.append(token)
    return cleaned_tokens

def word_lemmatization(tokens):
    lemmatizer = nltk.WordNetLemmatizer()
    cleaned_tokens = []
    for token in tokens:
        cleaned_tokens.append(lemmatizer.lemmatize(token))
    return cleaned_tokens

# ----------------------------------------------

# Data preprocessing pipeline function
def data_preprocessing(df):
    # 1. Label encoding
    df = label_encoding(df)
    # 2. Split the dataset 
    X_train, X_test, y_train, y_test = data_split(df)
    # 3. Text cleaning and tokenization for training data

    return X_train, X_test, y_train, y_test