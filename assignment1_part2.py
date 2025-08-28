# assignment1_part2.py

class Book:
    author = ""
    title = ""

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    b1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    b2 = Book("Walter Scott", "Ivanhoe: A Romance")
    b1.display()
    b2.display()
