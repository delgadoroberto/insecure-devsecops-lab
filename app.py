from flask import Flask

app = Flask(__name__)

SECRET_KEY = "super-secret-password"

@app.route("/")
def home():
    return "Insecure DevSecOps Lab"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
