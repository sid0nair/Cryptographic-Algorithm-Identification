import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv("/Users/sidnair/Desktop/Python Master/SIH/nist_feature_dataset.csv")
#print(data.shape[0])

x,y = data.iloc[:,:-1] , data.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100 , random_state=42)
rf_model.fit(x_train,y_train)

rf_predictions = rf_model.predict(x_train)
rf_probs = rf_model.predict_proba(x_train)

encoder = OneHotEncoder(sparse_output=False)
rf_encoded = encoder.fit_transform(rf_predictions.reshape(-1,1))

x_train_combined = np.hstack((x_train,rf_encoded))

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(x_train_combined, y_train)

rf_test_predictions = rf_model.predict(x_test)
rf_test_encoded = encoder.transform(rf_test_predictions.reshape(-1, 1))
x_test_combined = np.hstack((x_test, rf_test_encoded))

final_predictions = lr_model.predict(x_test_combined)
accuracy = accuracy_score(y_test, final_predictions)
report = classification_report(y_test, final_predictions)

print(f"Hybrid Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", report)