from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

def connect_mysql():
    mydb = mysql.connector.connect(
      host='localhost',
      user='root',
      password='root',
      database='db'
    )

    if mydb.is_connected():
       print("succes")
    else:
        print("failed")

if __name__ == '__main__':
    app.run('0.0.0.0',port=8000)

