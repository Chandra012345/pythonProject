import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                  port='3306',
                  user='root',
                  password='root',
                  database='pythontest')


        query='create table if not exists user(userID int primary key, userName varchar(200),  phone varchar(12))'

        cur=self.con.cursor()
        cur.execute(query)
        print('created')


    def insert_user(self,userid,username,phone):
        query="insert into user(userID,userName,phone) values ({},'{}','{}')".format(userid, username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user daved to db")


    def fetch_all(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user ID:", row[0])
            print("User Name: ", row[1])
            print("user Phone:", row[2])
            print()
            print()

    def delete(self,userID):
        query="delete from user where userID={}".format(userID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")


helper=DBHelper()
helper.fetch_all()
helper.delete(5)

# helper.insert_user(6,"rahul","8978678956")
# helper.insert_user(2,"radha","8978678956")
# helper.insert_user(3,"ram","8978678956")
# helper.insert_user(4,"Manohar","8978678956")
# helper.insert_user(5,"shyam","8978678956")
