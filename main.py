from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def workspace():
  return render_template("edit.html")

app.run('0.0.0.0', port=81)
