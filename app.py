from models import (Base, session, Book, engine)



# import models
# main menu - add, search, analysis, exit, view
# add books to the database
# edit books
# delete books
# search function
# data cleaning
# loop that runs the program


if __name__ == '__main__':
    Base.metadata.create_all(engine)