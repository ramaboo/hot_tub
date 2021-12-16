from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 5" + os.environ.get("DOMAIN")

if __name__ == '__main__':
    app.debug = True
    app.run