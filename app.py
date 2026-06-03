import os, logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

def send_text_response(text):
    return {"version": "2.0", "template": {"outputs": [{"simpleText": {"text": text}}]}}

@app.route("/webhook", methods=["POST"])
def webhook():
    return jsonify(send_text_response(
        "📋 현재 예약 중인 알림 서비스를 확인하고 싶으시다면\n"
        "아래 내용을 보내주세요 😊\n\n"
        "1. 성함\n"
        "2. 연락처\n\n"
        "확인 후 아래와 같은 형식으로\n"
        "현재 예약 중인 서비스를 안내해드립니다 🔔"
    ))

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
