import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create the 'questions' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer INTEGER NOT NULL
    )
''')

# Insert sample data into the 'questions' table
sample_questions = [
    ('What is the capital of France?', 'Paris', 'London', 'Rome', 'Madrid', 1),
    ('Which planet is known as the Red Planet?',
     'Mars', 'Venus', 'Jupiter', 'Saturn', 1),
    ('What is the chemical symbol for gold?', 'Au', 'Ag', 'Fe', 'Hg', 1)
]
cursor.executemany(
    'INSERT INTO questions (question_text, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)', sample_questions)

# Commit the changes and close the connection
conn.commit()
conn.close()
