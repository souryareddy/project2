from flask import flask,render_template

app = flask(__name__)
@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html', context="you are in homepage")
app.run()