
from flask import Flask,render_template,request, jsonify, Response,redirect, url_for
import sqlite3

from flask.views import MethodView

app = Flask(__name__)

class BookListView(MethodView) :
    def get(self) :
        try :
            connecion = sqlite3.connect('my_database.db')
            cursor = connecion.cursor()
            
            cursor.execute("SELECT * FROM transactions")
            rows = cursor.fetchall()
            print(type(rows))
            print("+++++++++++++++++")
            return {"status":"Success","data":rows}
        except Exception as e :
            return dict(status="Error" ,data = dict(error = e.args[0]))   
app.add_url_rule('/',view_func=BookListView.as_view('index'))

if __name__ == '__main__' :
    app.run(debug=True)