from flask import Flask, render_template

app = Flask(__name__)

# Dummy student data for demonstration
students = [
    {"name": "Alice", "course": "Math", "marks": 90},
    {"name": "Bob", "course": "Science", "marks": 85},
    {"name": "Charlie", "course": "History", "marks": 95},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/course')
def course():
    return render_template('course.html', students=students)

@app.route('/ranker_gallery')
def ranker_gallery():
    return render_template('ranker_gallery.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
