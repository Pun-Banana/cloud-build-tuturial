import os
from flask import Flask

app = Flask(__name__)

@app.route("/message")
def hello_world():
    return f"Hello! Your Python service is live. In Version 2"

if __name__ == "__main__":
    # Use the port assigned by Cloud Run or default to 8080
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))