import g4f
from g4f.Provider import Bard, Bing, You
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    content = request.form["content"]

    return chat_gpt(content).replace("\n", "<br>")


def chat_gpt(message):
    text = f'Сохрани форматирование текста! Переведи текст на русский язык:\n {message}'
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            provider=g4f.Provider.You,
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response
    except Exception as e:
        print('Error: ', e)


if __name__ == "__main__":
    app.run(debug=True)
