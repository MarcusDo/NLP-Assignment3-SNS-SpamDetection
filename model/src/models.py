# Import Necessary libraries
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import roc_auc_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Input, InputLayer
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.optimizers import Adam
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

class LSTM_model:
    def __init__(self, input_dim= None, output_dim = 45, input_length= 100, lstm_units= [64, 32], 
                 dense_units= [32], dropout_rate= 0.2, lr= 0.001, epochs= 10, batch_size= 32, random_state= 1211):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.input_length = input_length
        self.lstm_units = lstm_units
        self.dense_units = dense_units
        self.dropout_rate = dropout_rate
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size
        self.random_state = random_state
        self.history = None
        self.model = self._build_model()

    def _build_model(self):
        layers = [
            Input(shape = (self.input_length,)),
            Embedding(input_dim=self.input_dim, output_dim=self.output_dim, input_length=self.input_length),
        ]
        for i, units in enumerate(self.lstm_units):
            return_sequences = i < len(self.lstm_units) - 1
            layers.append(LSTM(units, activation='tanh', return_sequences=return_sequences))
            layers.append(Dropout(self.dropout_rate))

        for units in self.dense_units:
            layers.append(Dense(units, activation='relu'))
            layers.append(Dropout(self.dropout_rate))

        layers.append(Dense(1, activation='sigmoid'))

        self.model = Sequential(layers)
        return self.model

    def compile(self):
        self.model.compile(loss=BinaryCrossentropy(), optimizer=Adam(learning_rate=self.lr))
        return self.model
    
    def fit(self, X_train, y_train, X_val=None, y_val=None):
        tf.random.set_seed(self.random_state)

        validation_data = None
        if X_val is not None and y_val is not None:
            validation_data = (X_val, y_val)
            
        self.history = self.model.fit(
            X_train,
            y_train,
            validation_data=validation_data,
            epochs=self.epochs,
            batch_size=self.batch_size,
            verbose=0
        )
        return self

    def predict_proba(self, X):
        proba = self.model.predict(X).flatten()
        return np.column_stack((1-proba, proba))
    
    def predict(self, X):
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int).flatten()

    
class LogisticRegression_model (BaseEstimator, ClassifierMixin):
    def __init__(self, C = 1.0, max_iter= 100, reg='l2', random_state=1211, solver='liblinear'):
        self.C = C
        self.max_iter = max_iter
        self.reg = reg
        self.random_state = random_state
        self.solver = solver

        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LogisticRegression(C=self.C, max_iter=self.max_iter, penalty=self.reg, random_state=self.random_state, solver=self.solver))
        ])
    
    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self
    
    def predict(self, X):
        return self.model.predict(X)
    
    def predict_proba(self, X):
        return self.model.predict_proba(X)

class MultinomialNB_model (BaseEstimator, ClassifierMixin):
    def __init__(self, alpha=1.0, fit_prior=True):
        self.alpha = alpha
        self.fit_prior = fit_prior

        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB(alpha=self.alpha, fit_prior=self.fit_prior))
        ])
    
    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self
    
    def predict(self, X):
        return self.model.predict(X)
    
    def predict_proba(self, X):
        return self.model.predict_proba(X)
