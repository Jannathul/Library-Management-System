# Check Available Books
def available():
    # No Books
    if not books_available:
        print("\nSorry...\n No Book is available")
    # To print book_id - book_name
    else:
        print("\nAvailable Books are:\n")
        for key, value in books_available.items():
            print("{} - {}".format(key, value))

# Student Details
def stud_details():
    stu_name=input("\nEnter student name: ").lower()
    # Old user
    if stu_name in students.keys():
        print('Welcome back {}'.format(stu_name))
    # New user
    else:
        students[stu_name]=[]
        print("Welcome New User")
    return stu_name

# Add New Book 
def new_book():
    #Enter book_id and book_name
    book_num=int(input("\nEnter the new book ID (only numbers):"))
    add_book=input("Enter the new book name:").upper()
    books_available[book_num]=add_book 
    books_list[book_num]=add_book
    print("\nBooks Available:\n\n",books_available)
    
# Withdraw Books
def withdraw(books_available):
    name=stud_details()
    print("\nNumber of books taken: ",len(students[name]))
    # Can withdraw book
    if len(students[name])<=1:
        available()
        remove=int(input("\nEnter the book id to withdraw:"))
        book=books_available.get(remove)
        book_detail={remove:book}
        students[name].append(book_detail)
        books_available.pop(remove)
    # Took more than 2 books    
    else:
        print("\nSorry... Your minimum withdrawal is over!!!!")
        
# Student Dashboard
def dashboard():
    name=stud_details()
    details=students[name]
    if not details:
        print("\nNo book taken...")
    else:
        print("\n{} books are taken\n".format(len(details)))
        for x in range(len(details)):
            for key,value in details[x].items():
                print("{}) Book ID = {} : Book Name = {}".format(x+1,key,value))
                
# Returning Books
def returning():
    name=stud_details()
    books=students[name]
    print("\n{} have : {}".format(name,books))
    # Have Books to return
    if len(books)>0:
        num=int(input("\nEnter the Book Id to return: "))
        for x in range(len(books)):
            for key,value in books[x].items():
                if num==key:
                    print("Book found")
                    del books[x]            #remove book from students dashboard        
                    #Add to books available
                    value=books_list[key]   
                    books_available[key]=value
                    books_list[key]=value
                    print("\nBook added successfully..\nBooks Available in library are:\n",books_available)
                else:
                    print("Failed.. You have entered wrong book number")
            break    
        print("\nBooks to return:")
        if len(books)>0:
            print(" You have {} more - {}".format(len(books),students[name]))
        else:
            print(" All books returned\n Thank you {}".format(name))
    # No Books to Return
    else:
        print("\nYou have returned all books..")

books_list={101:"PYTHON",102:"C",103:"C++",104:"RUBY"}
books_available={101:"PYTHON",102:"C",103:"C++",104:"RUBY"}
students={"firdouse":[],"shahana":[],"fiya":[]}

def choose_action():
    print("Welcome to College Library")
    print("\n\ta) Add a new book to library\n\tb) Show the list of all available books")
    print("\tc) Withdraw an available book\n\td) Return book\n\te) My dashboard\n\tf) Exit")

    action = ''
    
    while not (action == 'a' or action == 'b' or action == 'c' or action == 'd' or action == 'e' or action == 'f'):
        action = input('\nEnter a choice (a - f) : ').lower()

        if action == 'a':
            new_book()
        elif action == 'b':
            available()
        elif action == 'c':
            withdraw(books_available)
        elif action == 'd':
            returning()
        elif action == 'e':
            dashboard()
        elif action == 'f':
            print("\n\tThank You...")
            break
        else:
            print("Invalid input")
        
        action = ''
choose_action()
