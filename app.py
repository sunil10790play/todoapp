from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }])

#always include this at the bottom of your code
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")