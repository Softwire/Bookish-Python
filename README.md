# Bookish - Python
Welcome to Bookish, a Softwire training project. Bookish is a website to keep track of all the books in a library. As it is, it's functionality is limited to seeing all books in the library and searching the library to see if a given title is present, but there is potential for much more!

## Setup & Running the code
- Install [Python](https://www.python.org/downloads/) if you don't have it installed yet
- Install a code editor, if you don't have one already (for example [Visual Studio Code](https://code.visualstudio.com/))
- Clone this project by running `git clone https://github.com/Softwire/Bookish-Python.git`
- Open `app.py` in your code editor and press Run (in VSCode the Run button is in the right top corner)
- Go to `http://127.0.0.1:5000/` in your browser to see the Bookish website

## TODO
As you can see, this web app needs some work! Here are some proposed improvements:
- Change the font and colours.
- Change the text on the Home Page from "TODO" to a description of the website.
- Change the text in the Navigation bar from "Navbar" to "Bookish".
- The All Books Page shows only titles of books. Change it to show author and year published too.
- The "Delete Book" button in the Navbar routes to the Home Page. Change this to route to the Delete Book Page.
- The Add Book Page has not been implemented yet. Implement this:
	- Create a template with a form (tip: look at `delete.html`) 
	-  On get, return template.
	-  On Post, call `dbManager.add_book()` with Book object (tip: look ad the seeding data at the top of `app.py`)
- Change the Delete Book Page to delete by author instead of by title:
	-   In `dbManager.py`, add a function (tip: look at `delete_book`)
	-   In `delete.html` change the title field to author
	-   In `app.py`, in the delete-book route, change the logic to delete by author
- Add a database field with information about the genre of a book:
	-  In `dbManager.py` add to the `CREATE TABLE` statement
	-   Update the `add_book` function
	-   Update the `get_all_books` function
	-   Update the `print_all_books_to_terminal` function
	-   Update the `get_book_by_title` function
	-   In `App.py`, update the seeding data
	-   Update the add-book flow

## Extra credit
Here is some vaguely specified extra functionality our fictional client has asked for:
-   Add user pages
-   Add login for users
-   Add admin users
-   Admin users can delete users
-   Users can borrow books
-   Users can get fines
-   Admin can change fines
-   Admin can delete books