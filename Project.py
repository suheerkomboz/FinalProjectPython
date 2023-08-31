class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level
        self.is_available = True



class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    # TODO : implement member method
    def borrow_book(self, book):
        book.is_available = False
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.is_available = True



class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # TODO : implement Library methods
    def add_book(self, book):
        self.books.append(book)


    def add_member(self, member):
        self.members.append(member)


    def display_books(self):
        for book in self.books:
            print(f'id: {book.book_id}\t title: {book.title}\t level: {book.level}\t author: {book.author}')

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

    def display_members(self):
        for member in self.members:
            print(f'id: {member.member_id}\t name: {member.name}\t level: {member.level}\t email: {member.email}')


    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

    def delete_member(self,member_id):
        for index in range(0,len(self.members)):
            if self.members[index].member_id == member_id:
                self.members.pop(index)
                print('member deleted success')
                break

    def borrow_book(self,book_id,member_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if member == None:
            print('Member not found')
            return

        if book == None:
            print('Book not found')
            return

        if member.level == book.level:
            member.borrow_book(book)
            print('book is borrow')
        else:
            print('Book is not available for this member level')
        pass

    def return_book(self, book_id, member_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member == None:
            print('Member not found')
            return

        if book == None:
            print('Book not found')
            return
        member.return_book(book)
        print('book is returned')

        pass


library = Library()
library.add_member(Member('Suheer','ss@gmail.com','A'))
library.add_member(Member('Abood','abc@gmail.com','C'))
library.add_member(Member('Masa','Masa@gmail.com','B'))

library.add_book(Book('The Black Cat','spaceton','A'))
library.add_book(Book('Batman','marvel','B'))
library.add_book(Book('Death note','tokyo film','C'))


print(' Welcome to the Library System '.center(100,'-'))
while True:
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. Show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter member name: ")
        email = input("Enter member email: ")
        level = input("Enter member level: ")
        member = Member(name,email,level)
        library.add_member(member)
        print('Member Added success','\n ########################')

    if choice == '2':
        id = input("Enter member id: ")
        member = library.find_member(int(id))
        name = input("Enter member name: ")
        email = input("Enter member email: ")
        level = input("Enter member level: ")
        member.name = name
        member.email = email
        member.level = level
        print('member edit success')

    if choice == '3':
        library.display_members()

    if choice == '4':
        id = input("Enter member id: ")
        library.delete_member(int(id))


    if choice == '5':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        level = input("Enter book level: ")
        book = Book(title,author,level)
        library.add_book(book)
        print('book Added success')

    if choice == '6':
        library.display_books()

    if choice == '7':
        member_id = int(input("Enter member id: "))
        book_id = int(input("Enter book id: "))
        library.borrow_book(book_id,member_id)

    if choice == '8':
        member_id = int(input("Enter member id: "))
        book_id = int(input("Enter book id: "))
        library.return_book(book_id,member_id)

    if choice == '9':
        break
    print('\n\n')
    print('#'*10,'\n','#'*10)
    print('\n\n')

