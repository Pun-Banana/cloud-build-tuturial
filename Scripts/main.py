import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "Cloud Run User")
    return f"Hello {name}! Your Python service is live."

if __name__ == "__main__":
    # Use the port assigned by Cloud Run or default to 8080
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))