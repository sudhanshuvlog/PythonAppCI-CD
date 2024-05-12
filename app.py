# app.py

from flask import Flask 
from urllib.parse import quote 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello World123!'
    
    name = "sudhansu"
    company = "gfg"   
    def a():
        print("abcd")
        a()
    def b(x, y):
        z= x+y
        print(z)

    def add(a,b):
        c=a+b
        
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
