from models import (Base, session, Book, engine)

# import models
# main menu - add, search, analysis, exit, view

def menu():
    while True:
        print('''
                \nPROGRAMMING BOOKS
                \r1) Add Book
                \r2) View all books
                \r3) Search for book
                \r4) Book Analysis
                \r5) Exit
                ''')
        choice = input('What would you like to do? ')
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''
                  \nPlease choose one of the options above.
                  \rA number from 1-5
                  \rPress any key to see the options again.''')

# add books to the database
# edit books
# delete books
# search function
# data cleaning
# loop that runs the program

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            pass
        elif choice == '2':
            # view books
            pass
        elif choice == '3':
            # search for book
            pass
        elif choice == '4':
            # book analysis
            pass
        else:
            print('GOODBYE')
            app_running = False

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()