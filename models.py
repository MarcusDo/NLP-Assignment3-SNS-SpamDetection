# Import Necessary libraries
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score, ConfusionMatrixDisplay

mat = confusion_matrix (y_predict, y_valid)
dis = ConfusionMatrixDisplay( confusion_matrix = mat)
dis.plot()
plt.tight_layout()
plt.show()
models = {
    'Logistic Regression': LogisticRegression(),
    'Multinomial Naive Bayes': MultinomialNB(),
    'Random Forest': RandomForestClassifier()
}

def hyperparameter_tuning(model, paramaters, X_train, y_train, cv=5):
    tuner = GridSearchCV(estimator=model, param_grid= paramaters, cv=cv, scoring='roc_auc')
    tuner.fit(X_train, y_train)
    return tuner.best_estimator_

def train (model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

def evaluate(model, X_test, y_test, include_roc=True, include_cr = True, include_cm = True):
    y_pred = model.predict(X_test)
    y_pred_probs = model.predict_proba(X_test)[:,1]
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

