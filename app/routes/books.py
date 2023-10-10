
from flask import Flask,render_template,request, jsonify, Response,redirect, url_for
import sqlite3

from flask.views import MethodView



app = Flask(__name__)

class BookListView(MethodView) :
    def get(self) :
        try :
            connecion = sqlite3.connect('my_database.db')
            cursor = connecion.cursor()
            
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            #books = [Book.fromTuple(row).to_dict() for row in rows]
            return rows
        except Exception as e :
            return dict(status="Error" ,data = dict(error = e.args[0]))
    def post(self) :
        if request.method=='POST' :
            data = request.get_json()

            bookId = data['bookId']
            bookName = data['bookName']
            authorId = data['authorId']
            price = data['price']
            journal = data['journal']

            try :
                connection = sqlite3.connect('my_database.db')
                cursor = connection.cursor()

                cursor.execute("INSERT INTO books(bookId,bookName,authorId,price,journal) values(?,?,?,?,?)",(bookId,bookName,authorId,price,journal))
                connection.commit()
                return jsonify({'status':'OK','message':'Book added Successfully'})
            except sqlite3.Error as catch:
                connection.rollback()
                print("SQLite error:", catch)
                return jsonify({'status':'error','message':str(catch)})
            finally:
                print("connection is closed in finally-------")
                connection.close()



app.add_url_rule('/books',view_func=BookListView.as_view('index'))

if __name__ == '__main__' :
    app.run(debug=True)