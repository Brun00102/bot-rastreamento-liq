from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot rodando com sucesso"

@app.route("/mensagem", methods=["POST"])
def mensagem():
    dados = request.json
    user_email = dados.get("from", {}).get("user", {}).get("userPrincipalName", "").lower()
    texto_msg = dados.get("text", "").lower()

    if user_email != "brunoosinteligenciafinanceira@outlook.com":
        return jsonify({"type": "message", "text": "⚠️ Você não tem permissão pra usar esse bot, chefia."})

    resposta = "Não entendi o que você quer, me diga: cedente 12345 ou grupo 9999"
    if "cedente" in texto_msg:
        codigo = texto_msg.split("cedente")[-1].strip()
        resposta = f"Rodando consulta pro cedente {codigo} (a lógica do OData virá aqui)"
    elif "grupo" in texto_msg:
        codigo = texto_msg.split("grupo")[-1].strip()
        resposta = f"Rodando consulta pro grupo {codigo} (a lógica do OData virá aqui)"

    return jsonify({
        "type": "message",
        "text": resposta
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
