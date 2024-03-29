import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='dist', static_url_path='', static_folder='dist')

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
