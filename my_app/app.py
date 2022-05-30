from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "First Flask App"

app.run()
