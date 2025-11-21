"""
Assignment 1: eBook Store
Student Name: EBRESAFE OGHENEYOMA
Student Number: 9017169
"""

# -----------------------------
# Book Node for Doubly Linked List
# -----------------------------
class BookNode:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.prev = None
        self.next = None

    def __str__(self):
        return (f"[ISBN: {self.isbn}, Title: {self.title}, "
                f"Author: {self.author}, Price: ${self.price:.2f}]")


# -----------------------------
# Doubly Linked List (Book Catalog)
# -----------------------------
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
            print(f"Book with ISBN {isbn} already exists. Rejected.")
            return False

        new_node = BookNode(isbn, title, author, price)

        # If empty catalog
        if not self.head:
            self.head = self.tail = new_node
            print(f"Book '{title}' by {author} added successfully.")
            return True

        # Traverse catalog to find last book by the same author
        current = self.head
        last_author_node = None
        while current:
            if current.author == author:
                last_author_node = current
            current = current.next

        if last_author_node:  # Insert after last book by this author
            new_node.next = last_author_node.next
            new_node.prev = last_author_node
            if last_author_node.next:
                last_author_node.next.prev = new_node
            else:
                self.tail = new_node
            last_author_node.next = new_node
        else:  # Append to the end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        print(f"Book '{title}' by {author} added successfully.")
        return True

    def get_books_by_author(self, author):
        results = []
        current = self.head
        while current:
            if current.author.lower() == author.lower():
                results.append(current)
            current = current.next
        return results

    def get_books_by_title(self, title):
        results = []
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                results.append(current)
            current = current.next
        return results

    def get_books_by_isbn(self, isbn):
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

                print(f"Book removed → {current}")
                return current
            current = current.next

        print(f"No book found with ISBN {isbn}.")
        return None

    def __str__(self):
        books = []
        current = self.head
        while current:
            books.append(str(current))
            current = current.next
        return " <-> ".join(books) if books else "Catalog is empty."


# -----------------------------
# Stack (Checkout Cart)
# -----------------------------
class CheckoutCart:
    def __init__(self):
        self.stack = []

    def add_to_cart(self, title):
        self.stack.append(title)
        print(f"Book '{title}' added to cart.")

    def remove_from_cart(self):
        if self.is_cart_empty():
            print("Cart is empty. Nothing to remove.")
            return None
        removed = self.stack.pop()
        print(f"Removed '{removed}' from cart.")
        return removed

    def peek_cart(self):
        if self.is_cart_empty():
            print("Cart is empty.")
            return None
        print(f"Top of cart: '{self.stack[-1]}'")
        return self.stack[-1]

    def cart_size(self):
        print(f"Cart contains {len(self.stack)} book(s).")
        return len(self.stack)

    def is_cart_empty(self):
        return len(self.stack) == 0


# -----------------------------
# Menu System
# -----------------------------
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
    print("11. Exit Program")
    print("============================")


def main():
    catalog = BookCatalog()
    cart = CheckoutCart()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            catalog.add_book(isbn, title, author)

        elif choice == "2":
            print(catalog)

        elif choice == "3":
            author = input("Enter Author: ")
            books = catalog.get_books_by_author(author)
            if books:
                print(f"Books by {author}:")
                for b in books:
                    print(b)
            else:
                print(f"No books found by {author}.")

        elif choice == "4":
            title = input("Enter Title: ")
            books = catalog.get_books_by_title(title)
            if books:
                print(f"Books titled '{title}':")
                for b in books:
                    print(b)
            else:
                print(f"No books found with title '{title}'.")

        elif choice == "5":
            isbn = input("Enter ISBN: ")
            book = catalog.get_books_by_isbn(isbn)
            if book:
                print(f"Book found → {book}")
            else:
                print(f"No book found with ISBN {isbn}.")

        elif choice == "6":
            isbn = input("Enter ISBN to remove: ")
            catalog.remove_book_by_isbn(isbn)

        elif choice == "7":
            title = input("Enter book title to add to cart: ")
            cart.add_to_cart(title)

        elif choice == "8":
            cart.remove_from_cart()

        elif choice == "9":
            cart.peek_cart()

        elif choice == "10":
            cart.cart_size()

        elif choice == "11":
            print("Exiting Bookstore System. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
