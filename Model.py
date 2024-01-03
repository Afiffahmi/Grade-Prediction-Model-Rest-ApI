import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle


# Set a random seed for reproducibility
random.seed(0)

# Define the number of rows you want in your dataset
num_rows = 300

# Create empty lists to store data
gender = []
test1 = []
test2 = []
assignment1 = []
assignment2 = []
quiz1 = []
grades = []
carrymark = []


# Generate random data
for _ in range(num_rows):
    test1_score = random.uniform(1, 10)
    test2_score = random.uniform(1, 10)
    assignment1_score = random.uniform(1, 10)
    assignment2_score = random.uniform(1, 15)
    quiz1_score = random.uniform(1, 5)

    # Calculate the total score
    total_score = test1_score + test2_score + assignment1_score + assignment2_score + quiz1_score

    if 45 <= total_score <= 50:
        grade = 5.0
    elif 42 <= total_score < 45:
        grade = 4.7
    elif 39 <= total_score < 42:
        grade = 4.4
    elif 36 <= total_score < 39:
        grade = 4.1
    elif 33 <= total_score < 36:
        grade = 3.8
    elif 30 <= total_score < 33:
        grade = 3.5
    elif 27 <= total_score < 30:
        grade = 3.2
    elif 24 <= total_score < 27:
        grade = 2.9
    elif 21 <= total_score < 24:
        grade = 2.6
    elif 18 <= total_score < 21:
        grade = 2.3
    elif 15 <= total_score < 18:
        grade = 2.0
    elif 12 <= total_score < 15:
        grade = 1.7
    elif 9 <= total_score < 12:
        grade = 1.4
    else:
        grade = 1.0


    test1.append(test1_score)
    test2.append(test2_score)
    assignment1.append(assignment1_score)
    assignment2.append(assignment2_score)
    quiz1.append(quiz1_score)
    grades.append(grade)
    carrymark.append(total_score)

# Create a DataFrame from the lists
data = pd.DataFrame({
    'test1': test1,
    'test2': test2,
    'assignment1': assignment1,
    'assignment2': assignment2,
    'quiz1': quiz1,
    'grade': grades,
    'carrymark': carrymark,
})

# Save the DataFrame to a CSV file
data.to_csv('synthetic_data.csv', index=False)

