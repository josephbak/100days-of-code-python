from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


app = Flask(__name__)

## CREATE DATEBASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: but it will silence the dprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

#CREATE a new RECORD
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# Read all records
# all_books = session.query(Book).all()
#
# Read a particular record by query
# book = Book.query.filter_by(title="Harry Potter").first()
#
# Update a particular record by query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
#
# Update a record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
#
# Delete a particular record by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
#
# You can also delete by querying for a particular value e.g. by title or one of the other properties.

all_books = []


@app.route('/')
def home():
    ##READ ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template("index.html", books = all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        new_book = Book(
            title= data["title"],
            author= data["author"],
            rating= data["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        # all_books.append(new_book)
        # print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

