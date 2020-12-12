from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(r'index.html')


@app.route("/blog")
def blog():
    return render_template("blog-single.html")


if __name__ == '__main__':
    app.run(debug=True)
