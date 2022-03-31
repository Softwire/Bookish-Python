from book import Book
from flask import Flask, render_template, request
from dbManager import *

# Setup
app = Flask(__name__)
dbManager = DbManager()

# Seeding data
seedingBooks = [   
    Book('In search of lost Time', 'Proust, Marcel', 1913),
    Book('Ulysses', 'Joyce, James', 1904),
    Book('Don Quixote', 'Cervantes, de, Miguel', 1605),
    Book('One Hundred Years of Solitude', 'Garcia Marquez, Gabriel', 2006),
    Book('The Great Gatsby', 'Fitzgerald, F. Scott', 1925)
]

# Add seeding data to the database
for book in seedingBooks:
    dbManager.add_book(book)

# Routes
@app.route("/")
def home():
    return render_template("home.html", content="TODO: add description")

@app.route("/all-books")
def all_books():
    all_books = dbManager.get_all_books()
    return render_template("books_all.html", books = all_books)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        search_result = dbManager.get_book_by_title(request.form["title"])
        if len(search_result) > 0:
            return render_template("search.html", search_results = search_result[0].title)
        else:
            return render_template("search.html", search_results = "No book found")

@app.route("/delete-book", methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        return render_template("home.html")
    else:
        title = request.form["title"]
        search_result = dbManager.get_book_by_title(title)
        if len(search_result) == 0:
            return render_template("delete.html", result = "No book with that title found")
        else:
            dbManager.delete_book(title)
            return render_template("delete.html", result = f"{title} has been deleted")

@app.route("/add-book")
def add():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug = True)
