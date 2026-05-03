# Import Necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tf.keras.models import Sequential
from tf.keras.layers import Embedding, LSTM, Dense, Dropout
from tf.keras.losses import BinaryCrossentropy
from tf.keras.optimizers import Adam
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score, ConfusionMatrixDisplay

class LSTM_model:
    def __init__(self, input_dim= None, output_dim = 128, input_length= 100, lstm_units= 128, dropout_rate= 0.2):
        self.model = Sequential([
            Embedding(input_dim=input_dim, output_dim=output_dim, input_length=input_length),
            LSTM(lstm_units, dropout=dropout_rate, recurrent_dropout=dropout_rate),
            Dense(1, activation='sigmoid')
        ])
    
    def _compile(self, learning_rate=0.001):
        self.model.compile(loss= BinaryCrossentropy(), optimizer=Adam(learning_rate=learning_rate), metrics=['auc'])
        return self.model

    def _predict(self, X):
        return np.argmax(self.model.predict(X), axis=-1)

    def _predict_proba(self, X):
        return self.model.predict(X)
    
class LogisticRegression_model:
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LogisticRegression())
        ])
    
    def _fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model
    
    def _predict(self, X):
        return self.model.predict(X)
    
    def _predict_proba(self, X):
        return self.model.predict_proba(X)[:,1]

class MultinomialNB_model:
    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB())
        ])
    
    def _fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model
    
    def _predict(self, X):
        return self.model.predict(X)
    
    def _predict_proba(self, X):
        return self.model.predict_proba(X)[:,1]

def evaluate(model, X_test, y_test, include_roc=True, include_cr = True, include_cm = True):
    y_pred = model._predict(X_test)
    y_pred_probs = model._predict_proba(X_test)
    auc = roc_auc_score(y_test, y_pred_probs)
    print("AUC Score:", auc)

    # Classification Report
    if include_cr:
        print("Classification Report:\n", classification_report(y_test, y_pred))

    # Confusion Matrix
    if include_cm:
        print("Confusion Matrix:\n")
        cfm = confusion_matrix (y_pred, y_test)
        ConfusionMatrixDisplay(confusion_matrix = cfm).plot(cmap= 'Greens')
        plt.tight_layout()
        plt.show()
    
    if include_roc:
        fpr, tpr, _ = roc_curve(y_test, y_pred_probs, pos_label=1)
        plt.plot(fpr, tpr, lw = 2, color ='red', label=f'{model.__class__.__name__} (area = {auc:.2f})' )
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--') 
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('FPR')
        plt.ylabel('TPR')
        plt.title('AUC-ROC Curve Comparison')
        plt.show()

