from flask import Flask, render_template

from utils import get_values

app = Flask(__name__)

@app.route("/")
def index():
    try:
        data = get_values()

        return render_template('index.html', data=data)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
