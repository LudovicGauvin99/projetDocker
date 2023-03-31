from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

@app.route("/db")
def connect_mysql():
   #  mydb = mysql.connector.connect(
   #    host='db',
   #    user='root',
   #    password='root',
   #    database='db',
   #    port=8080
   #  )
   mydb = mysql.connection.cursor()

   mydb.execute('''SELECT * FROM personne''')
   Executed_DATA = mydb.fetchall()
   return str(Executed_DATA)

if __name__ == '__main__':
    app.run('0.0.0.0',port=8000)

