from flask import Flask, render_template
from draw_cool_thing import get_image

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('lsystem.html')

@app.route('/lsystem/<step>/<axiom>/<ruleF>/<ruleG>')
def lsystem(step, axiom, ruleF, ruleG):
    get_image(int(step), axiom, ruleF, ruleG) 
    return render_template('lsystem.html')


@app.route('/hello/<string:name>')
def hello(name):
    if name != 'Макщ':
        return f'hello {name}!!!'
    return 'kys'


if __name__ == '__main__':
    app.run(debug=True)
