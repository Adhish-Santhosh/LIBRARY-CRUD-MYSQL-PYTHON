import mysql.connector


class LibraryManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Adhish@123",
            database="book_db"
        )
        print("Connected Successfully...!")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into book_details(Bookname,Author_name,Price,Book_type,Published_year)values(%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Book added successfully...!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM book_details"

            self.cursor.execute(query)
            records = self.cursor.fetchall()

            # for data in records:
            #     print(data)
            return(records)

        except Exception as e:
            return []

book_instance=LibraryManager()
# book_instance.post(Bookname="wings of fire", Author_name="Abdul Kalam", Price=300, Book_type="Biography",Published_year=1999)
book_instance.get()