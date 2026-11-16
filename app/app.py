import os
from flask import Flask, jsonify
# ===== VARIAÇÃO DA DUPLA =====
NOME_DUPLA = "dupla-21"
MENSAGEM = "Olá da dupla 21"
PORTA = 5021
# =============================

VERSAO = os.environ.get("APP_VERSION", "v1")
app = Flask(__name__)

@app.route("/saude")
def saude():
    return jsonify(status="erro", versao=VERSAO)

@app.route("/aluno")
def aluno():
    return jsonify(dupla=NOME_DUPLA, mensagem=MENSAGEM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORTA)
