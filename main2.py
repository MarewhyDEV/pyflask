from flask import Flask
import random

app = Flask(__name__)

yt = ["Yazi","Tura"]

@app.route("/")
def hello_world():
    return '''<h1>Hello, World!</h1> 
      <a href="/yazitura">Yazı Tura At</a>'''

@app.route("/yazitura")
def yazitura():
    info = random.choice(yt)
    return f'<h3>{info}</h3>'

app.run(debug=True)
