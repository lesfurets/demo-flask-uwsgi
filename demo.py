from flask import Flask
import settings

app = Flask(__name__)

@app.route("/")
def hello():
    return "<html>{}</html>".format(settings.content)

    if __name__ == "__main__":
        app.run(host='0.0.0.0')
