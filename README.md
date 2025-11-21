**eBook Store – Linked List Catalog with Sorting Algorithms (Python)**  

### 🔹 Short GitHub Description  
> Enhanced eBook store using a doubly linked list, stack-based cart, and multiple sorting algorithms (bubble, insertion, quick sort) to sort books by price.

# eBook Store – Linked List Catalog with Sorting Algorithms (Python)

This project is an enhanced version of the eBook store system, built in Python.  
It uses a **doubly linked list** for the book catalog, a **stack-based checkout cart**, and introduces several **sorting algorithms** to organize books by price.

The application provides a menu-driven interface for managing the catalog, interacting with a cart, and comparing how different sorting algorithms behave on the same data.

---

## 🚀 Features

### 📚 Book Catalog (Doubly Linked List)
- Custom `BookNode` class representing each book:
  - ISBN
  - Title
  - Author
  - Price
- Doubly linked list structure for the catalog
- Add new books (with duplicate ISBN checks)
- Remove books by ISBN
- Search books by:
  - Author
  - Title
  - ISBN (single match)
- Display the entire catalog

### 🛒 Checkout Cart (Stack)
- Stack-based cart with methods to:
  - Add a book title to the cart
  - Remove the most recent book from the cart
  - Peek at the top item in the cart
  - Show cart size
  - Check if cart is empty
- Clear and user-friendly messages for cart operations

### 📊 Sorting Algorithms (By Price)
The catalog can be converted to a list of book objects and sorted using:

- **Bubble Sort** (by price)
- **Insertion Sort** (by price)
- **Quick Sort** (by price)

For each algorithm, the program:
- Shows the list of prices **before** sorting
- Shows the list of prices **after** sorting
- Prints the sorted books with full details

This provides a practical demonstration of how different sorting algorithms behave on the same dataset.

### 🧾 Menu-Driven Console UI

Main menu options include:

1. Add Book to Catalog  
2. Display Catalog  
3. Search Books by Author  
4. Search Books by Title  
5. Search Book by ISBN  
6. Remove Book by ISBN  
7. Add Book to Checkout Cart  
8. Remove Book from Cart  
9. Peek Cart  
10. Display Cart Size  
11. Sort Books by Price (Bubble Sort)  
12. Sort Books by Price (Insertion Sort)  
13. Sort Books by Price (Quick Sort)  
14. Exit Program  

---

## 🧰 Technologies & Concepts Used

- **Language:** Python
- **Data Structures:**
  - Doubly Linked List (book catalog)
  - Stack (checkout cart)
  - Python lists (for sorting)
- **Algorithms:**
  - Bubble Sort
  - Insertion Sort
  - Quick Sort
- **Concepts:**
  - Object-Oriented Programming (OOP)
  - Algorithm analysis and comparison
  - Input validation helpers (`get_non_empty_string`, `get_valid_price`)
  - Menu-driven user interface in the console

---

## 🔧 How to Run

1. Clone the repository
2. Run with Phython


---

## 🧠 What I Learned
Implementing and working with a doubly linked list in Python
Managing a stack-based data structure for a checkout cart
Converting linked list data into Python lists for sorting
Implementing and comparing classic sorting algorithms:
Bubble Sort
Insertion Sort
Quick Sort
Designing console applications that demonstrate data structures + algorithms in a practical context
Improving input validation and user experience with helper functions

---

## 📌 Possible Future Enhancements
Measure and compare execution time between the sorting algorithms
Persist data to a file or database between runs
Add more sorting options (by title, author, or ISBN)
Build a GUI or web version using a Python framework
Integrate unit tests for the list, cart, and sorting functions

---

## 📄 License
This project is available for educational and portfolio use.
