from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Oiii, meu nome é larissa, tenho 21 anos e sou dev front-end!"

if __name__ == '__main__':
    app.run(debug=True)