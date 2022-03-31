# Bookish - Python
Welcome to Bookish, a Softwire training project. Bookish is a website to keep track of all the books in a library. As it is, it's functionality is limited to seeing all books in the library and searching the library to see if a given title is present, but there is potential for much more!

## Setup & Running the code
- Install [Python](https://www.python.org/downloads/) if you don't have it installed yet
- Install a code editor, if you don't have one already (for example [Visual Studio Code](https://code.visualstudio.com/))
- Clone this project by running `git clone https://github.com/Softwire/Bookish-Python.git`
- Install Flask by running `pip3 install flask`
- Open the project in your code editor, navigate to `app.py` and press Run (in VSCode the Run button is in the right top corner)
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
	-   In `dbManager.py` add to the `CREATE TABLE` statement
	-   In `book.py` add a field called genre to the Book class
    -   Update the `add_book` function
	-   Update the `get_all_books` function
	-   Update the `print_all_books_to_terminal` function
	-   Update the `get_book_by_title` function
	-   In `App.py`, update the seeding data
	-   Update the add-book flow

## Helpful notes
- On downloading Python and VSCode, if you get an error that you are not allowed to run the installer, move the downloaded file out of your downloads folder (e.g. to your desktop) and try running it again.
- The code will keep running when you make changes. Refresh your browser page to see the changes in your browser.
- Sometimes partial changes you make will crash the code. Just rerun it by clicking Run like you did when running the code the first time.
- When you make changes to the `CREATE TABLE` sql statement, you will have to delete `bookish.db` and rerun the code, which will generate a new `bookish.db` following your new specified structure for the table.

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