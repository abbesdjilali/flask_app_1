from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, BG!'


@app.route('/hello-name/<name>')
def home_name(name):
    return 'Hello,  %s' % escape(name)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5050)


    #os.environ.get('HOST')