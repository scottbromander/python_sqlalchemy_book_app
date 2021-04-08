from models import (Base, session, Book, engine)
import datetime
import csv

# import models
# main menu - add, search, analysis, exit, view

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input('''
              \n*****''')
        pass
    else:
        return return_date



    return

def clean_price(price_str):
    price_float = float(price_str)
    print(price_float)
    return int(price_float * 100)

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

def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                print(row)
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=date, price=price)
                session.add(new_book)
            else:
                print('Already haz that book')
        session.commit()

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            title = input('Title: ')
            author = input('Author: ')
            date = input('Published Date (Ex: October 25, 2017): ')
            date = clean_date(date)
            price = input('Price (Ex: 25.99):')
            price = clean_price(price)
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
    # app()
    add_csv()
    # clean_date('October 25, 2017')

    for book in session.query(Book):
        print(book)