#-*- coding: utf-8 -*

from flask import Flask, render_template
from flask import request
from flask import current_app
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# manager = Manager(app)
# init flask_bootstrap
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/net')
def index2():
    return render_template('net.html')

@app.route('/rev')
def index3():
    return render_template('rev.html')

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()
