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

# Text Cleaning Function 
def _text_cleaning(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text) 
    text = text.split()
    text = ' '.join(text)
    return text

# Text Tokenization function
def _text_tokenization(text):
    return nltk.word_tokenize(text)

# Text Stopword Removal function
def _stopword_removal(tokens):
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in tokens if token not in stop_words]
    return cleaned_tokens

# Text Lemmatization function
def _word_lemmatization(tokens):
    lemmatizer = nltk.WordNetLemmatizer()
    cleaned_tokens = []
    for token in tokens:
        cleaned_tokens.append(lemmatizer.lemmatize(token))
    return cleaned_tokens

# Word Vectorization function - TF-IDF 
def _word_vectorization(X):
    X = X.apply(lambda row: ' '.join(row))
    vectorizer = TfidfVectorizer()
    vectorized_text = vectorizer.fit_transform(X)
    X = vectorized_text.toarray()
    return X
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
    X_train = X_train.apply(_text_cleaning)
    X_train = X_train.apply(_text_tokenization)
    X_train = X_train.apply(_stopword_removal)
    X_train = X_train.apply(_word_lemmatization)
    X_train = _word_vectorization(X_train)

    # 6. Test Data Preparation:
    X_test = X_test.apply(_text_cleaning)
    X_test = X_test.apply(_text_tokenization)
    X_test = X_test.apply(_stopword_removal)
    X_test = X_test.apply(_word_lemmatization)
    X_test = _word_vectorization(X_test)

    return X_train, X_test, y_train, y_test