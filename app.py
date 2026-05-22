import os
from flask import Flask

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return "Secure DevSecOps Lab"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # nosec B104 required for Docker container exposure
