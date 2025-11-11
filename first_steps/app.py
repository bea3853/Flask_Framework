from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>teste</p>"



# carregue o código:
# com python -m flask run
# Instalação:
# pip install Flask

# Ambiente Virtual: 
# mkdir myproject
# cd myproject
# python3 -m venv .venv
