from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Oiii, meu nome é larissa, tenho 21 anos e sou dev front-end!"

if __name__ == '__main__':
    app.run()