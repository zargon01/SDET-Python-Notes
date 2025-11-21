class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author


    def get_title(self):
        return self.title



def main():

    title = input()
    author = input()
    
    book = Book(title,author)

    print(f"Title: {book.get_title()}")
    print(f"Author: {book.get_author()}")


if __name__ == "__main__":
    main()
