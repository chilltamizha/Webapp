from turtle import title
from flask import Flask , render_template
import intro
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',title='my website')

if __name__ == '__main__':
    app.run(debug=True)