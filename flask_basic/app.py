from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("basic_form.html")

app.debug = 1
app.run()
