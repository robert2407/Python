class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} checked out successfully"
        else:
            return f"{self.title} is checked out"

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} returned successfully"
        else:
            return f"{self.title} is available"

    def display_info(self):
        status = 'Checked out' if self.checked_out else 'Available'
        return f"Title: {self.title}, Item ID: {self.item_id}, Status: {status}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author, num_pages):
        super().__init__(title, item_id)
        self.author = author
        self.num_pages = num_pages

    def display_info(self):
        book_info = super().display_info()
        return f"{book_info}, Author: {self.author}, Type: Book, Pages: {self.num_pages}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        dvd_info = super().display_info()
        return f"{dvd_info}, Director: {self.director}, Type: DVD, Duration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        magazine_info = super().display_info()
        return f"{magazine_info}, Type: Magazine, Issue Number: {self.issue_number}"

if __name__ == "__main__":
    book = Book("Myths of the Ancient Greeks", "515", "Richard P. Martin", 300)
    dvd = DVD("Sherlock", "015232", "Dexter Fletcher, Guy Ritchie", 158)
    magazine = Magazine("ProMotor", "144", 5)

    print(book.display_info())
    print(dvd.display_info())
    print(magazine.display_info())

    print(book.check_out())
    print(dvd.check_out())
    print(magazine.check_out())

    print(book.return_item())
    print(dvd.return_item())
    print(magazine.return_item())

    print(book.return_item())