from urllib import request
from xmlrpc.client import DateTime
from flask import Flask , render_template , request , redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

class Search(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(100))
    date = db.Column(db.String(100))

@app.route('/',methods=['GET'])
def index():

    return render_template('index.html')


@app.route('/search/',methods=['POST'])
def search():
    data = request.form['search']
    
    print(data)
    x = datetime.now()
    format = x.strftime("%b %d %Y %I:%M:%S %p")

    print(format)
  
    

    content = Search(content=data,date=format)

    db.session.add(content)
    db.session.commit()

    return redirect('https://google.com/search?q='+ data)

if __name__ == '__main__':
    app.run(debug=True)
