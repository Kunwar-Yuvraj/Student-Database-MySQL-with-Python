# Student admission database
import mysql.connector

class Database_Helper:
    # Constructor
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            port="3306",
            password="jayant",
            database="Students"
        )

        str_query = "create table if not exists Student(Student_ID int primary key, Student_Name varchar(100), Phone_Number varchar(12), Fee_Status varchar(2))"
        mycursor = self.con.cursor()
        mycursor.execute(str_query)
     
    
    # Insertion method
    def insert_Data(self, id, name, phone, fee):
        str_query="insert into Student(Student_ID, Student_Name, Phone_Number, Fee_Status) values({},'{}','{}','{}')".format(id,name,phone, fee)
        cur=self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Student {} saved to Database".format(name))


    # Fetching all data
    def fetch_data(self):
        str_query="select * from student"
        cur=self.con.cursor()
        cur.execute(str_query)
        for record in cur:
            print(f"Student_ID: {record[0]}")
            print(f"Student_name: {record[1]}")
            print(f"Student_Phone: {record[2]}")
            print(f"Fee Status: {record[3]}")
            print()
            print()


    # Deletion Method
    def delete(self,id):
        str_query="delete from student where Student_ID = {}".format(id)
        cur=self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Student with id {} is deleted\n".format(id))
     


    # Updation method
    def update_User(self,id,newname, newphone):
        str_query="update student set Student_Name='{}', Phone_Number='{}' where Student_ID={}".format(newname, newphone,id)
        cur=self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Student with Id {} updated\n".format(id))
     
 


# Main function
if __name__ == "__main__":
    db=Database_Helper()
    print("***** WELCOME TO SCHOOL MANAGEMENT SYSTEM *****")
    while(True):
        print("Press 1 to insert new Student")
        print("Press 2 to display all Students")
        print("Press 3 to delete a Student")
        print("Press 4 to update a Student")
        print("Press 5 to exit the program")
        try:
            choice=int(input())

            if(choice==1):
                #Insert Student
                uid=int(input("Enter Student ID: "))
                uname=input("Enter Student Name: ")
                uphone=input("Enter Student's Phone: ")
                ustatus=input("Enter Fee Status.'y' for paid and 'n' for not paid: ")[0]
                db.insert_Data(uid,uname, uphone,ustatus)
                pass


            elif choice==2:
                #display Student
                db.fetch_data()
                pass


            elif choice==3:
                #delete Student
                uid=int(input("Enter ID to be deleted: "))
                db.delete(uid)
                pass


            elif choice==4:
                #Update Student
                uid=int(input("Enter Student ID: "))
                uname=input("Enter new name: ")
                uphone=input("Enter new phone number: ")
                ustatus=input("Enter new Fee Status. 'yes' for paid and 'no' for not paid: ")
                db.update_User(uid,uname,uphone,ustatus)


            elif choice==5:
                break


            else:
                print("Invalid input! Please try again")
                
                
        except Exception as e:
            print(e)
            print("Invalid input! Try again")
