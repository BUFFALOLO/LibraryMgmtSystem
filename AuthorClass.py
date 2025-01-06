class Author:
    def __init__(self, name, bio):
        self.__name = name
        self.__bio = bio

    def display_details(self):
        return f"Author Name: {self.__name}, Biography: {self.__bio}"