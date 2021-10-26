class Library:
    def __init__(self, listofbooks) -> None:
        self.books = listofbooks
        pass
    def displayavailblebooks(self):
        print("Books Present  in tha library :")
        for books in self.books:
            print(books)
    
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} is Please Keep it safe and handle in proper and return book within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry , This book is already being issued to another Student.Please wait until the book is return")    
            return False

    def returBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for Returning this book! Hope you enjoyed reading it!")
class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return : ")
        return self.book   

    

if __name__ == "__main__":
    CentralLibrary = Library(["Additive Manufacturing", "Machine Learning", "Catia","MATHS","Machine Design"]) #only one copy of books is present
    Student = Student()
    CentralLibrary.displayavailblebooks()
    while(True):
        welcomeMsg = '''*********Welcome to Central library *************
        Please choose an Option :
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice :"))
        if a == 1 :
            CentralLibrary.displayavailblebooks()
        elif a == 2:
            CentralLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            CentralLibrary.returBook(Student.returnBook())
        elif a == 4:
            print("Thanks for using this library! Have a great day")
            exit()
        else:
            print("Invalid Choice!")       
        

