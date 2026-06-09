from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6LVq98Ya5jL2IfdDi_-ttId1dCxiwtAftNglFfTIG9bNQ")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming = request.form.get("Body", "")
    prompt = f"Correct the English grammar and spelling. Return ONLY the corrected sentence, nothing else.\n\n{incoming}"
    response = model.generate_content(prompt)
    corrected = response.text.strip()
    resp = MessagingResponse()
    resp.message(corrected)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
