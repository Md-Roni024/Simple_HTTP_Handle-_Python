from flask import Flask;

app = Flask(__name__)

@app.route('/')
def welcome():
    return "This my first application using flask!Okk"

@app.route('/home')
def home():
    return "This my Home route!"

if __name__ == '__main__':
    app.run(debug=True)
