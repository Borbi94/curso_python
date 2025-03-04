from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def index():
    return '''<html>
                <head>
                    <title>Hello World</title></head>
                    <body><h1>Hello World!</h1>
                    <p> Ir a la pagina de <a href="/
                    ">Inicio</a></p>
                    </body>
            </html>'''
 
if __name__ == '__main__':
    app.run(debug=True)