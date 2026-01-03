import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample dataset
data = {
    'Math': [8, 6, 5, 9, 4, 7],
    'Science': [9, 7, 6, 8, 5, 6],
    'Computer': [9, 8, 5, 9, 4, 7],
    'Communication': [5, 7, 8, 6, 9, 8],
    'Career': [
        'Engineer',
        'Software Developer',
        'Teacher',
        'Data Scientist',
        'Journalist',
        'Manager'
    ]
}

df = pd.DataFrame(data)

# Features and target
#Created by Pranay Lade and Rishabh
X = df[['Math', 'Science', 'Computer', 'Communication']]
y = df['Career']

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# User input
print("Enter your skill ratings (1 to 10):")
math = int(input("Math: "))
science = int(input("Science: "))
computer = int(input("Computer: "))
communication = int(input("Communication: "))

# Prediction
user_input = pd.DataFrame([[math, science, computer, communication]], columns=['Math', 'Science', 'Computer', 'Communication'])
prediction = model.predict(user_input)

print("\nRecommended Career:", prediction[0])

