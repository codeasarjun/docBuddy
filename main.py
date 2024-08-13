# app.py

from flask import Flask, render_template, request, redirect, url_for
from core.pdf_processing import process_pdf
from core.text_processing import summarize_text, suggest_keywords
from core.qna import ask_question

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            pdf_base64, text_content = process_pdf(file)
            summarized_text = summarize_text(text_content)
            key_words = suggest_keywords(text_content)
            #text_content_html = text_content.replace('\n', '<br>') # to keep the formatting while showing the text content
            return render_template("tabs.html", pdf_base64=pdf_base64, summarized=summarized_text, key_words=key_words,content=text_content)
    return redirect(url_for("home"))

@app.route("/chat", methods=["POST"])
def chat():
    if request.method == "POST":
        question = request.form["question"]
        content = request.form["content"]  # Retrieve content for Q&A
        answer = ask_question(question, content)
        return render_template("tabs.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
