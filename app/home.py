from flask import Flask,render_template,jsonify
from markupsafe import escape
import sys
app = Flask(__name__)
books=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/hello/<username>',methods=["GET"])
def home(username):
    return render_template('hello.html',username= escape(username))

#API ROUTES
@app.route('/api/books',methods=["GET"])
def all_books():
    return jsonify(books)

#une route qui retourne un book selon son `id` 
@app.route('/api/book/<int:id>',methods=["GET"])
def book_id(id):
    book = [o for o in books if o["id"] == int(id)]
    return jsonify(book)

#une route qui retourne un book selon son titre 
@app.route('/api/book/<title>',methods=["GET"])
def book_title(title):
    print(title,file=sys.stderr)
    book = [b for b in books if b["titre"].find(escape(title)) !=-1]
    print(book,file=sys.stderr)
    return jsonify(book)




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5050)
