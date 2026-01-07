import os
from flask import Flask
app = Flask(__name__)
@app.router("/")
def home():
  return "PrepPilot backend is running"
application = app

if __name__ == "main":
  port = int(os.environ.get("PORT",8000))
  app.run(host="0.0.0.0", port=port)
