class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = True

    def borrow_book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        if not self.__available:
            self.__available = True
            return True
        return False

    def is_available(self):
        return self.__available

    def display_details(self):
        status = "Available" if self.__available else "Borrowed"
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publication Date: {self.__pub_date}, Status: {status}"

    def get_title(self):
        return self.__title