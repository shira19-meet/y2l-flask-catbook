from flask import Flask
from flask import render_template, request
from database import get_all_cats
from database import get_cat
from database import create_cat
from database import new_vote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
	cats = get_all_cats()
	return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def catbook_profile(id):
	cats = get_cat(id)
	return render_template("cat.html", cats=cats)

@app.route('/add', methods=['GET', 'POST'])
def catbook_add():
	if request.method == 'GET':
		return render_template("add.html")
	else:
		name = request.form['name']
		create_cat(name) 
		cats = get_all_cats()       
		return render_template("home.html", cats= cats)

@app.route('/vote', methods=['GET', 'POST'])
def catbook_vote():
	if request.method == 'GET':
		return render_template("cats.html")
	else:
		print("post!")
		vote = request.form['vote']
		new_vote(id)  
		cats = get_all_cats()  
		return render_template("home.html", cats= cats)

		



if __name__ == '__main__':
   app.run(debug = True)
