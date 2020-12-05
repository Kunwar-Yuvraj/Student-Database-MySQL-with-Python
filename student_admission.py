# Student admission database
import mysql.connector


class Database_Helper:
    # Constructor
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.con = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        str_query = "create table if not exists Student(Student_ID int primary key, Student_Name varchar(100), Phone_Number varchar(12), Fee_Status varchar(2))"
        mycursor = self.con.cursor()
        mycursor.execute(str_query)

    # Insertion method
    def insert_Data(self, id, name, phone, fee):
        str_query = f"insert into Student(Student_ID, Student_Name, Phone_Number, Fee_Status) values({id},'{name}','{phone}','{fee}')"
        cur = self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print(f"Student {name} saved to Databasex\n")

    # Fetching all data
    def fetch_data(self):
        str_query = "select * from Student"
        cur = self.con.cursor()
        cur.execute(str_query)
        for record in cur:
            print(f"Student_ID: {record[0]}")
            print(f"Student_name: {record[1]}")
            print(f"Student_Phone: {record[2]}")
            print(f"Fee Status: {record[3]}")
            print()
            print()

    # Deletion Method
    def delete(self, id):
        str_query = "delete from Student where Student_ID = {}".format(id)
        cur = self.con.cursor()
        cur.execute(str_query)
        self.con.commit()
        print("Student with id {} is deleted\n".format(id))

    # Updation method
    def update_User(self, id, newname, newphone, newstatus):
        str_query = "update Student set Student_Name='{}', Phone_Number='{}' where Student_ID={}".format(
            newname, newphone, id
        )
        cur = self.con.cursor()
        cur.execute(str_query)
        print(f"\nStudent with Id {id} updated\n")


# Main function
if __name__ == "__main__":
    host = input("Enter host: ")
    user = input("Enter user name: ")
    password = input("Enter password: ")
    database = input("Enter database: ")
    db = Database_Helper(host, user, password, database)
    print("\n***** WELCOME TO SCHOOL MANAGEMENT SYSTEM *****\n")
    while True:
        print("Press 1 to insert new Student")
        print("Press 2 to display all Students")
        print("Press 3 to delete a Student")
        print("Press 4 to update a Student")
        print("Press 5 to exit the program\n")
        try:
            choice = int(input("Enter your choice: "))
            print()

            if choice == 1:
                # Insert Student
                uid = int(input("Enter Student ID: "))
                uname = input("Enter Student Name: ")
                uphone = input("Enter Student's Phone: ")
                ustatus = input("Enter Fee Status.'y' for paid and 'n' for not paid: ")[
                    0
                ]
                db.insert_Data(uid, uname, uphone, ustatus)
                pass

            elif choice == 2:
                # display Student
                db.fetch_data()
                pass

            elif choice == 3:
                # delete Student
                uid = int(input("Enter ID to be deleted: "))
                db.delete(uid)
                pass

            elif choice == 4:
                # Update Student
                uid = int(input("Enter Student ID: "))
                uname = input("Enter new name: ")
                uphone = input("Enter new phone number: ")
                ustatus = input(
                    "Enter new Fee Status. 'yes' for paid and 'no' for not paid: "
                )

                if (
                    ustatus == "Yes"
                    or ustatus == "yes"
                    or ustatus == "No"
                    or ustatus == "no"
                ):
                    db.update_User(uid, uname, uphone, ustatus)

                else:
                    print("Invalid choice")

            elif choice == 5:
                break

            else:
                print("Invalid input! Please try again")

        except Exception as e:
            print(e)
            print("Invalid input! Try again")
