from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ab')
def student():
    return 'join!'

@app.route('/abc')
def name():
    return 'Navya'

@app.route('/temp')
def temp():
    return render_template('ab.html',d="sir")

if __name__ == '__main__':
    app.run()
