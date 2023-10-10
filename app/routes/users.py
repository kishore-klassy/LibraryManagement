
from flask import Flask,render_template,request, jsonify, Response,redirect, url_for
import sqlite3

from flask.views import MethodView

from app.models.user import User



app = Flask(__name__)

class UserListView(MethodView) :
    def get(self) :
        try :
            connection = sqlite3.connect('my_database.db')
            cursor=connection.cursor()

            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            users =[User.fromTuple(row).to_dict() for row in rows]
            connection.close()
            return users
        except Exception as e :
            return dict(status="error",data=dict(error=e.args[0]))
    
    def post(self) :
        if request.method == 'POST' :
            data = request.get_json()
           
            username = data['username']
            email = data['email']

            
            try :
                connection =sqlite3.connect('my_database.db')
                cursor=connection.cursor()
                cursor.execute("INSERT INTO users(UserID,UserName,Email,MobileNumber) values(?,?,?,?)",(UserID,UserName,Email,MobileNumber))
                # cursor.execute("SELECT * FROM users")
                # rows = cursor.fetchall()
                # print(rows)
                connection.commit()
                return jsonify({'status':'OK','message':'User added Successfully'})
            except sqlite3.Error as catch:
                connection.rollback()
                print("SQLite error:", catch)
                return jsonify({'status':'error','message':str(catch)})

            finally:
                print("connection is closed in finally-------")
                connection.close()
        
    
    def put(self) :
        if request.method=="PUT" :
            data = request.get_json() 
            id = data['id']
            username = data['username']
            email = data['email']

            try :
                connection = sqlite3.connect('my_database.db')
                cursor = connection.cursor()
                cursor.execute("UPDATE users set username=? ,email = ? where id=? ",(username,email,id))
                connection.commit()
                return jsonify({'status':"OK",'message':"User Data Updated"})

            except sqlite3.Error as catch :
                connection.rollback()
                print("SQLite error:", catch)
                return jsonify({'status':'error','message':str(catch)})
            finally:
                print("connection is closed in finally-------")
                connection.close()
    def delete(self) :
        if request.method=="DELETE" :
            data =  request.get_json()
            id = data['id']
           
            try :
                connection = sqlite3.connect('my_database.db')
                cursor = connection.cursor()

                cursor.execute("Delete from users where id=?",(id))
                print("below query-----")
                connection.commit()
                return jsonify({'status':"OK",'message':"User Deleted Successfully"})
            except sqlite3.Error as catch :
                connection.rollback()
                print("SQLite error:", catch)
                return jsonify({'status':'error','message':str(catch)})
            finally:
                
                connection.close()
        

app.add_url_rule('/users',view_func=UserListView.as_view('index'))

if __name__ == '__main__':
    app.run(debug=True)

