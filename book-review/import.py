import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine=create_engine('postgresql+pg8000://postgres:Mango@008@localhost/postgres')
db=scoped_session(sessionmaker(bind=engine))

def main():
    f=open('books.csv')
    r=csv.reader(f)
    for isbn,title,author,year in r:
        db.execute('insert into book (isbn,title,author,year) values (:isbn,:title,:author,:year)',{'isbn':isbn,'title':title,'author':author,'year':year})
    db.commit()
    print('successfully run')

if __name__=="__main__":
    main()
