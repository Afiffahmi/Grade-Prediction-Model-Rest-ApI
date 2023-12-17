import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv('synthetic_data.csv')

# Let's take a look at the first few rows of the dataset to understand its structure
print(data.head())

# Define features and the target
X = data[['test1', 'test2', 'assignment1', 'assignment2', 'quiz1', 'carrymark']]
y = data['grade']


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)

k = 30  # Number of neighbors (you can change this)
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X_train, y_train)

with open('knn_model.pkl', 'wb') as file:
    pickle.dump(model, file)


# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


# Display evaluation results
print("Mean Squared Error:", mse)
print("R2", r2)
