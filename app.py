from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Fetch questions from the database
cursor.execute("SELECT * FROM questions")
questions = cursor.fetchall()

# Close the database connection
conn.close()

# Store the user's score
score = 0

# Custom function to calculate the length of a list


def length(lst):
    return len(lst)


# Add the custom function to the Jinja2 environment
app.jinja_env.globals.update(length=length)


@app.route('/')
def index():
    # Reset the score when quiz is started
    global score
    score = 0
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score

    if request.method == 'POST':
        # Get the selected answer from the form
        selected_option = request.form['option']
        # Get the current question index
        question_index = int(request.form['question_index'])

        # Get the answer index from the database
        answer_index = questions[question_index][6]

        # Check if the selected answer is correct
        if selected_option == str(answer_index):
            score += 1

        # Move to the next question
        if question_index < len(questions) - 1:
            next_question_index = question_index + 1
            return render_template('quiz.html', question=questions[next_question_index], question_index=next_question_index)
        else:
            return render_template('result.html', score=score, total_questions=len(questions))

    # Display the first question
    return render_template('quiz.html', question=questions[0], question_index=0)


if __name__ == '__main__':
    app.run(debug=True)
