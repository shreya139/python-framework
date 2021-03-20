from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
   app.run()

#methods to bind url
   #1. @app.route(‘/hello’)
   #2. app.add_url_rule(‘/’, ‘hello’, hello_world) #after defining the function

   
