# -*- coding: utf-8 -*-
"""Salary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1op0Aolj_4eaw-TcIoDHMnWwLE4Hxg8HD
"""

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, silhouette_score

# Load dataset
# Load dataset
df = pd.read_csv('/content/drive/MyDrive/AI/ds_salaries new.csv')

# Inspect the DataFrame to understand the structure
print(df.head())
print(df.columns)
print(df.dtypes)

# Replace 'target_column' with the actual name of your target column
target_column = 'salary'  # Update this with your target column name

# Separate features and target variable
X = df.drop(target_column, axis=1)
y = df[target_column]

# Encode categorical variables in X
X = pd.get_dummies(X)

# Ensure the target variable y is numeric
if y.dtype == 'object':
    le = LabelEncoder()
    y = le.fit_transform(y)

# Standardize the features (important for SVM and KNN)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SVM
svm_model = svm.SVC(kernel='linear')
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_predictions)
print(f'SVM Accuracy: {svm_accuracy}')

# Apply KMeans
kmeans_model = KMeans(n_clusters=3, n_init=10, random_state=42)  # Adjust n_clusters based on your data
kmeans_model.fit(X_train)
kmeans_predictions = kmeans_model.predict(X_test)
# For clustering, use a different evaluation metric like silhouette score or adjusted rand index
try:
    kmeans_silhouette = silhouette_score(X_test, kmeans_predictions)
    print(f'KMeans Silhouette Score: {kmeans_silhouette}')
except ValueError as e:
    print(f"KMeans evaluation error: {e}")

# Apply Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_predictions = nb_model.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_predictions)
print(f'Naive Bayes Accuracy: {nb_accuracy}')

# Apply KNN
knn_model = KNeighborsClassifier(n_neighbors=5)  # Adjust n_neighbors based on your data
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_predictions)
print(f'KNN Accuracy: {knn_accuracy}')