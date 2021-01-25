from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "SELAMAT DATANG DI WEB KAMI"

@app.route("/submit", methods=["POST"])
def submit():
    return "Percobaan Post"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
