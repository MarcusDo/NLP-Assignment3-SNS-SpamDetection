# Import necessary libraries
import os 
import re
import pandas as pd 
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split    

# ---- Helper functions for data preprocessing -----
# Function to read dataset 
def _read_dataset():
    dataset_dir = os.path.join(os.getcwd(), 'sms_dataset')
    df = pd.read_table(dataset_dir, names = ['label', 'message'])
    return df

# Function to split dataset 
def _data_split(df, test_size = 0.2, random_state = 1211):
    X = df['message']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state, stratify = y)
    return X_train, X_test, y_train, y_test

# Label Encoding function
def _label_encoding(df):
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    return df

def _text_tokenization(text):
    return nltk.word_tokenize(text)

# Remove Blank
def _tokens_blank_removal(tokens):
    return [token for token in tokens if token != '']

# Text Lowercasing Function
def _tokens_lower(tokens):
    return [token.lower() for token in tokens]

# Text Punctuation Removal function
def _tokens_punctuation_removal(tokens):
    return [re.sub(r'[^\w\s]', '', token) for token in tokens]

# Text Number Handling function
def _tokens_number_handling(tokens):
    return [re.sub(r'\d+', 'number', token) for token in tokens]

# Text Stopword Removal function
def _tokens_stopword_removal(tokens):
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in tokens if token not in stop_words]
    return cleaned_tokens

# Text Lemmatization function
def _tokens_lemmatization(tokens):
    lemmatizer = nltk.WordNetLemmatizer()
    cleaned_tokens = []
    for token in tokens:
        cleaned_tokens.append(lemmatizer.lemmatize(token))
    return cleaned_tokens

# ----------------------------------------------

# Data preprocessing pipeline 
def data_preprocessing(df):
    # 1. Label encoding
    df = _label_encoding(df)

    # 2. Duplicate removal
    df = df.drop_duplicates()

    # 3. Missing value removal
    df = df.dropna()

    # 4. Split the dataset 
    X_train, X_test, y_train, y_test = _data_split(df)

    # 5. Train Data Preparation: 
    X_train = X_train.apply(_text_tokenization)
    X_train = X_train.apply(_tokens_lower)
    X_train = X_train.apply(_tokens_punctuation_removal)
    X_train = X_train.apply(_tokens_number_handling)
    X_train = X_train.apply(_tokens_stopword_removal)
    X_train = X_train.apply(_tokens_lemmatization)
    X_train = X_train.apply(_tokens_blank_removal)

    # 6. Test Data Preparation:
    X_test = X_test.apply(_text_tokenization)
    X_test = X_test.apply(_tokens_lower)
    X_test = X_test.apply(_tokens_punctuation_removal)
    X_test = X_test.apply(_tokens_number_handling)
    X_test = X_test.apply(_tokens_stopword_removal)
    X_test = X_test.apply(_tokens_lemmatization)
    X_test = X_test.apply(_tokens_blank_removal)

    return X_train, X_test, y_train, y_test