import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv('synthetic_data.csv')

# Define features and the target
X = data[['test1', 'test2', 'assignment1', 'assignment2', 'quiz1', 'carrymark', 'taking_notes', 'attendance', 'listening']]
y = data['grade']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)

# # Feature scaling
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test= sc.transform(X_test)

# Create and train a K-Nearest Neighbors (KNN) model
k = 30  # Number of neighbors (you can change this)
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X_train, y_train)


# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


# Display evaluation results
print("Mean Squared Error:", mse)
print("R2", r2)



# # Save to file in the current working directory
# pkl_filename = "model.pkl"
# with open(pkl_filename, 'wb') as file:
#     pickle.dump(model, file)

# # Load from file
# with open(pkl_filename, 'rb') as file:
#     pickle_model = pickle.load(file)
    
# # Calculate the accuracy score and predict target values
# score = pickle_model.score(X_test, y_test)
# print("Test score: {0:.2f} %".format(100 * score))
# Ypredict = pickle_model.predict(X_test)