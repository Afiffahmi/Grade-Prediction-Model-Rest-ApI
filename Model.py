import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle


# Set a random seed for reproducibility
random.seed(0)

# Define the number of rows you want in your dataset
num_rows = 140

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

    # Randomize the grade
    if 40 <= total_score <= 50:
        grade = random.choice(['5', '4'])
    elif 29 <= total_score < 40:
        grade = random.choice(['5', '4'])
    elif 20 <= total_score < 29:
        grade = random.choice(['4', '3', '2'])
    elif 10 <= total_score < 20:
        grade = random.choice(['3', '2', '1'])
    else:
        grade = '1'

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

