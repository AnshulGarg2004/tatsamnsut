from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# @app.route('/lesson') 
# def lessons() :
#     return render_template('lessons.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

if __name__ == "__main__":
    app.run(debug=True)
