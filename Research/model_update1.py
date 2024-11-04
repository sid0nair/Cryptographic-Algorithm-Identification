import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV

# Load data
data = pd.read_csv("/Users/sidnair/Desktop/Python Master/SIH/nist_feature_dataset.csv")

# Split data into features and target variable
x, y = data.iloc[:, :-1], data.iloc[:, -1]

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=69)

# Define parameter grid for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Create a GridSearchCV object for Random Forest
rf_grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=69), 
                               param_grid=param_grid,
                               scoring='accuracy',
                               cv=3)

# Fit the grid search to the training data
rf_grid_search.fit(x_train, y_train)

# Best parameters found for Random Forest
best_rf_model = rf_grid_search.best_estimator_

# Make predictions with the best Random Forest model
rf_predictions = best_rf_model.predict(x_train)
encoder = OneHotEncoder(sparse_output=False)  # Initialize encoder before use
rf_encoded = encoder.fit_transform(rf_predictions.reshape(-1, 1))

# Combine original training data with encoded predictions
x_train_combined = np.hstack((x_train, rf_encoded))

# Define parameter grid for Logistic Regression
lr_param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],  
    'solver': ['liblinear', 'saga']  
}

# Create a GridSearchCV object for Logistic Regression
lr_grid_search = GridSearchCV(estimator=LogisticRegression(max_iter=1000), 
                               param_grid=lr_param_grid,
                               scoring='accuracy',
                               cv=3)

# Fit the grid search to the combined training data
lr_grid_search.fit(x_train_combined, y_train)

# Best parameters found for Logistic Regression
best_lr_model = lr_grid_search.best_estimator_

# Make predictions on test set using the best Random Forest model
rf_test_predictions = best_rf_model.predict(x_test)
rf_test_encoded = encoder.transform(rf_test_predictions.reshape(-1, 1))  # Transform test predictions

# Combine original test data with encoded test predictions
x_test_combined = np.hstack((x_test, rf_test_encoded))

# Final predictions with tuned Logistic Regression model
final_predictions = best_lr_model.predict(x_test_combined)

# Calculate accuracy and classification report
accuracy = accuracy_score(y_test, final_predictions)
report = classification_report(y_test, final_predictions)

print(f"Hybrid Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", report)