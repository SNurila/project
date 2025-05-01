from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

try:
    summarizer = pipeline("summarization")
except Exception as e:
    print("🔥 Failed to load summarizer model:", e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    if not summarizer:
        return jsonify({"summary": "🚫 Model not available."}), 500

    try:
        text = request.json.get("text", "")
        if not text:
            return jsonify({"summary": "⚠️ No input text provided!"})

        print("📥 Received text:", text)
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        return jsonify({"summary": summary[0]["summary_text"]})
    except Exception as e:
        print("❌ Error during summarization:", e)
        return jsonify({"summary": "Something went wrong 💥"}), 500

if __name__ == "__main__":
    app.run(debug=True)