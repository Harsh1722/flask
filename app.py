from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('digital_market_site.html')


if __name__=='__main__':
    app.run(debug=True)