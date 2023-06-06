from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/hello/<name>')
def hello(name):
    return (f'Hello {name}!')

if __name__ == '__main__':
    app.run()