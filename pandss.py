import pandas as pd
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Deepak', 'Esha'],
    'Marks': [85, 92, 76, 59, 88],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math']
}

df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


print("\nStudents who scored > 80:")
print(df[df['Marks'] > 80])


print("\nAverage marks per subject:")
print(df.groupby('Subject')['Marks'].mean())
