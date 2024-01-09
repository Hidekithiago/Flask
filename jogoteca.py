from flask import Flask

app = Flask(__name__) # Cria uma instância da classe Flask


@app.route("/inicio") # Define a rota da aplicação
def ola():
    return "<h1>Olá Mundo!</h1>" # Retorna uma string


app.run() # Executa o servidor web