# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F1Gtjj35MC2XsDVTtBIKUdfMD9Wtpqb7
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar el dataset limpio
data = pd.read_csv('data/cleaned_dataset.csv')

# Separar variables independientes (X) y la variable dependiente (y)
X = data.drop(columns=['Desercion'])
y = data['Desercion']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar una lista para almacenar los resultados
results = []

# Modelo 1: Regresión Logística
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
y_pred_logreg = logreg.predict(X_test)
results.append(['Regresión Logística', accuracy_score(y_test, y_pred_logreg)])

# Evaluación del modelo de Regresión Logística
print("Evaluación de Regresión Logística:")
print("Accuracy:", accuracy_score(y_test, y_pred_logreg))
print(confusion_matrix(y_test, y_pred_logreg))
print(classification_report(y_test, y_pred_logreg))

# Modelo 2: Árbol de Decisión
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)
results.append(['Árbol de Decisión', accuracy_score(y_test, y_pred_tree)])

# Evaluación del modelo de Árbol de Decisión
print("Evaluación de Árbol de Decisión:")
print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print(confusion_matrix(y_test, y_pred_tree))
print(classification_report(y_test, y_pred_tree))

# Modelo 3: Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
results.append(['Random Forest', accuracy_score(y_test, y_pred_rf)])

# Evaluación del modelo de Random Forest
print("Evaluación de Random Forest:")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Modelo 4: K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
results.append(['K-Nearest Neighbors', accuracy_score(y_test, y_pred_knn)])

# Evaluación del modelo KNN
print("Evaluación de K-Nearest Neighbors:")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))

# Modelo 5: Support Vector Machine (SVM)
svm = SVC()
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
results.append(['Support Vector Machine', accuracy_score(y_test, y_pred_svm)])

# Evaluación del modelo SVM
print("Evaluación de Support Vector Machine:")
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print(confusion_matrix(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))

# Modelo 6: Gradient Boosting
gb = GradientBoostingClassifier()
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
results.append(['Gradient Boosting', accuracy_score(y_test, y_pred_gb)])

# Evaluación del modelo Gradient Boosting
print("Evaluación de Gradient Boosting:")
print("Accuracy:", accuracy_score(y_test, y_pred_gb))
print(confusion_matrix(y_test, y_pred_gb))
print(classification_report(y_test, y_pred_gb))

# Guardar resultados de todos los modelos en un DataFrame
results_df = pd.DataFrame(results, columns=['Modelo', 'Accuracy'])

print("Comparativa de modelos:")
print(results_df)