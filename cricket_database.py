import mysql.connector as mysql
db=mysql.connect(
    host="localhost"
    username="root"
    password="psysam"
    database="realprogrammers"
)
cursor=db.cursor()
cursor.execute("CREATE TABLE user(name VARCHAR(255).user.name varchar(255)")")