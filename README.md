# Library Management System

A simple console-based Library Management System built in Python using
Object-Oriented Programming. It lets users register, view available books,
borrow books, return books, and lets a librarian add new books to the
collection.

## Features

- **Register** — Enter your name, age, and grade to register with the system.
- **View Book Menu** — See the list of currently available books.
- **Borrow a Book** — Borrow any book that's currently available.
- **Return a Book** — Return a book you previously borrowed.
- **Add a New Book** — Add a new title to the library collection.
- Tracks who has borrowed which book using a dictionary (`borrowed_books`).
- Prevents borrowing a book that's already checked out (it's removed from
  the available list once borrowed).
- Prevents adding duplicate book titles.

## How to Run

```bash
python LibraryManagementSystem.py
```

> **Note:** The screen-clear command (`os.system("cls")`) is written for
> Windows. If you're running this on Linux or macOS, replace it with:
> ```python
> os.system("cls" if os.name == "nt" else "clear")
> ```

## How to Use

When you run the program, you'll see a menu:

```
0. Exit
1. Register
2. View Our Book Menu
3. Borrow Book
4. Return Book
5. Add New Book
```

Enter the number of the option you want and follow the on-screen prompts.
After each action, you'll be asked to press:
- **E** to exit the program
- **M** to return to the main menu

### Example Flow

1. Choose `2` to view available books.
2. Choose `3` to borrow a book — enter your name and the exact book title.
3. Type `borrow` when prompted to confirm.
4. Later, choose `4` to return the book by typing its title again.

## Class Overview: `BookLibrary`

| Method | Purpose |
|---|---|
| `user_data()` | Registers a user (name, age, grade). |
| `view_books_menu()` | Displays all currently available books. |
| `borrow_book()` | Lets a user borrow an available book; records it in `borrowed_books`. |
| `return_book()` | Lets a user return a borrowed book; removes it from `borrowed_books`. |
| `add_new_book()` | Adds a new book title to the library (skips duplicates). |
| `selection_to_do()` | Runs the main menu loop. |

## License

Free to use and modify for learning purposes.

## Author
**Hadiqa Hanif** — Beginner, Learner, and Observer
