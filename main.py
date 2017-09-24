from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value='0' />
            <textarea name="text"></textarea>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form


@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    userstring = request.form['text']
    encryptstring = '<h1>' + rotate_string(userstring,rotate) + '</h1>'
    return encryptstring
app.run()