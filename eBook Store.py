# Assignment 2: eBook Store
# Student Name: EBRESAFE OGHENEYOMA
# Student Number: 9017169

class BookNode:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.prev = None
        self.next = None

    def __str__(self):
        return f"[ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}]"


class BookCatalog:
    def __init__(self):
        self.head = None
        self.tail = None

    def isbn_exists(self, isbn):
        current = self.head
        while current:
            if current.isbn == isbn:
                return True
            current = current.next
        return False

    def add_book(self, isbn, title, author, price):
        if self.isbn_exists(isbn):
            print(f"Book with ISBN {isbn} already exists.")
            return
        new_node = BookNode(isbn, title, author, price)
        if not self.head:
            self.head = self.tail = new_node
            print("Book added to catalog.")
            return
        current = self.head
        last_same_author = None
        while current:
            if current.author == author:
                last_same_author = current
            current = current.next
        if last_same_author:
            nxt = last_same_author.next
            new_node.prev = last_same_author
            new_node.next = nxt
            last_same_author.next = new_node
            if nxt:
                nxt.prev = new_node
            else:
                self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print("Book added successfully.")

    def get_books_by_author(self, author):
        matches = []
        current = self.head
        while current:
            if current.author == author:
                matches.append(current)
            current = current.next
        return matches

    def get_books_by_title(self, title):
        matches = []
        current = self.head
        while current:
            if current.title == title:
                matches.append(current)
            current = current.next
        return matches

    def get_book_by_isbn(self, isbn):
        current = self.head
        while current:
            if current.isbn == isbn:
                return current
            current = current.next
        return None

    def remove_book_by_isbn(self, isbn):
        current = self.head
        while current:
            if current.isbn == isbn:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                print(f"Book with ISBN {isbn} removed.")
                return
            current = current.next
        print(f"No book found with ISBN {isbn}.")

    def to_list(self):
        books = []
        current = self.head
        while current:
            books.append(current)
            current = current.next
        return books

    def __str__(self):
        if not self.head:
            return "Catalog is empty."
        parts = []
        current = self.head
        while current:
            parts.append(str(current))
            current = current.next
        return " <-> ".join(parts)


class CheckoutCart:
    def __init__(self):
        self.stack = []

    def add_to_cart(self, title):
        self.stack.append(title)
        print(f"Book '{title}' added to cart.")

    def remove_from_cart(self):
        if not self.stack:
            print("Cart is empty.")
            return
        removed = self.stack.pop()
        print(f"Book '{removed}' removed from cart.")

    def peek_cart(self):
        if not self.stack:
            print("Cart is empty.")
        else:
            print(f"Top of cart: '{self.stack[-1]}'")

    def cart_size(self):
        print(f"Cart size: {len(self.stack)} book(s).")


def get_non_empty_string(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Field cannot be empty.")


def get_valid_price(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Enter a valid number.")


def bubble_sort_books_by_price(books):
    print("Before:", [b.price for b in books])
    n = len(books)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if books[j].price > books[j + 1].price:
                books[j], books[j + 1] = books[j + 1], books[j]
    print("After (Bubble):", [b.price for b in books])


def insertion_sort_books_by_price(books):
    print("Before:", [b.price for b in books])
    for i in range(1, len(books)):
        key = books[i]
        j = i - 1
        while j >= 0 and books[j].price > key.price:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key
    print("After (Insertion):", [b.price for b in books])


def quick_sort_books_by_price(books):
    if len(books) <= 1:
        return books
    pivot = books[len(books) // 2]
    left = [b for b in books if b.price < pivot.price]
    mid = [b for b in books if b.price == pivot.price]
    right = [b for b in books if b.price > pivot.price]
    return quick_sort_books_by_price(left) + mid + quick_sort_books_by_price(right)


def display_menu():
    print("\n===== eBook Store Menu =====")
    print("1. Add Book to Catalog")
    print("2. Display Catalog")
    print("3. Search Books by Author")
    print("4. Search Books by Title")
    print("5. Search Book by ISBN")
    print("6. Remove Book by ISBN")
    print("7. Add Book to Checkout Cart")
    print("8. Remove Book from Cart")
    print("9. Peek Cart")
    print("10. Display Cart Size")
    print("11. Sort Books by Price (Bubble Sort)")
    print("12. Sort Books by Price (Insertion Sort)")
    print("13. Sort Books by Price (Quick Sort)")
    print("14. Exit Program")
    print("============================")


def main():
    catalog = BookCatalog()
    cart = CheckoutCart()
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            isbn = get_non_empty_string("Enter ISBN: ")
            title = get_non_empty_string("Enter Title: ")
            author = get_non_empty_string("Enter Author: ")
            price = get_valid_price("Enter Price: ")
            catalog.add_book(isbn, title, author, price)
        elif choice == "2":
            print(catalog)
        elif choice == "3":
            author = get_non_empty_string("Enter Author: ")
            books = catalog.get_books_by_author(author)
            if books:
                for b in books:
                    print(b)
            else:
                print("No books found.")
        elif choice == "4":
            title = get_non_empty_string("Enter Title: ")
            books = catalog.get_books_by_title(title)
            if books:
                for b in books:
                    print(b)
            else:
                print("No books found.")
        elif choice == "5":
            isbn = get_non_empty_string("Enter ISBN: ")
            book = catalog.get_book_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("Not found.")
        elif choice == "6":
            isbn = get_non_empty_string("Enter ISBN to remove: ")
            catalog.remove_book_by_isbn(isbn)
        elif choice == "7":
            title = get_non_empty_string("Enter title to add to cart: ")
            cart.add_to_cart(title)
        elif choice == "8":
            cart.remove_from_cart()
        elif choice == "9":
            cart.peek_cart()
        elif choice == "10":
            cart.cart_size()
        elif choice == "11":
            books = catalog.to_list()
            if books:
                bubble_sort_books_by_price(books)
                for b in books:
                    print(b)
            else:
                print("Catalog empty.")
        elif choice == "12":
            books = catalog.to_list()
            if books:
                insertion_sort_books_by_price(books)
                for b in books:
                    print(b)
            else:
                print("Catalog empty.")
        elif choice == "13":
            books = catalog.to_list()
            if books:
                print("Before:", [b.price for b in books])
                books = quick_sort_books_by_price(books)
                print("After (Quick):", [b.price for b in books])
                for b in books:
                    print(b)
            else:
                print("Catalog empty.")
        elif choice == "14":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
