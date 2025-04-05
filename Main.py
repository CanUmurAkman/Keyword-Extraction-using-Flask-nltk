from flask import Flask, render_template, request
from rake_nltk import Rake

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    keywords = []
    text = ""
    num_keywords = 5  # Default number of keywords

    if request.method == "POST":
        text = request.form.get("text", "")
        try:
            num_keywords = int(request.form.get("num_keywords", 5))
        except ValueError:
            num_keywords = 5

        # Initialize RAKE. You can customize the stopwords or language if needed.
        rake = Rake()
        rake.extract_keywords_from_text(text)
        ranked_phrases = rake.get_ranked_phrases()
        # Get only the top N keywords based on their rank
        keywords = ranked_phrases[:num_keywords]

    return render_template("index.html", keywords=keywords, text=text, num_keywords=num_keywords)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)