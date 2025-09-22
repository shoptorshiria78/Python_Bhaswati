class Library:
    
    def __init__(self, list, name):
        
        self.bookList = list
        self.name = name
        self.lendDict = {}
        
    def displayBooks(self):
        print(f"We have the following books in our Library: {self.name}")
        for book in self.bookList:
            print(book)
            
    def lendBook(self, user, book):
        
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The lend book database has been updated, you can now take the book")
            
        else:
            print(f"This book is taken by {self.lendDict[book]}")
            
    def addBook(self, book):
        self.bookList.append(book)
        print(f"{book} has been added to the book list.")
        
    def returnBook(self, book):
        self.lendDict.pop(book)
        
if __name__ == '__main__':
    
    books = Library(["Rich dad poor dad", "Ikigai", " Python", " Alogrithm of C++", "Atomic Habits", " Think and grow rich", " the housemaid", " Thousands splendid suns "], "Let's up skill")