from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI

client = OpenAI(api_key="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")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming = request.form.get("Body", "")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Correct the English grammar and spelling. Return ONLY the corrected sentence, nothing else."},
            {"role": "user", "content": incoming}
        ]
    )
    corrected = response.choices[0].message.content.strip()
    resp = MessagingResponse()
    resp.message(corrected)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
