import csv

attribute_name = ['ID Number','Full Name',  '\tSection', '\tDate', '\t    Time']
attendance_database = 'attendance.csv'

class student():
    def addAttendance():
        print("\nAdd Student Attendance")
        global attribute_name
        global attendance_database

        student_data = []

        print("Fill-in Information")

        for field in attribute_name:
            value = input("\nEnter " + field + ": ")
            student_data.append(value)

        with open(attendance_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([student_data])

        print("Data saved successfully!")
        print("\n")
        return

    #function to view student records
    def viewAttendance():
        global attribute_name
        global attendance_database

        print("\nStudent Attendance\n")

        with open(attendance_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in attribute_name:
                print(x, end="  \t  |  ")
            print("\n")

            for row in reader:
                for item in row:
                    print(item, end="\t\t|  \n")
                print("\n")   
        print("\n")

    #function to search student record
    def searchAttendance():
        global attribute_name
        global attendance_database

        print("Search Student Attendance ")
        idnumber = input("Enter ID Number to search: ")
        with open(attendance_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if idnumber == row[0]:
                        print("Student Attendance \n")
                        print("ID Number: ", row[0])
                        print("Full Name: ", row[1])
                        print("Section: ", row[2])
                        print("Date: ", row[3])
                        print("Time: ", row[4])
                        break
            else:
                print("ID Number is not found in our database!")
        print("\n")

    #function to update student records
    def updateAttendance():
        global attribute_name
        global attendance_database

        print("Update Student Attendance \n")
        idnumber = input("Enter ID Number to update: ")
        index_student = None
        updated_data = []
        with open(attendance_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if idnumber == row[0]:
                        index_student = counter
                        print("Student found at index [",index_student, "] ")
                        print("Fill-in New Record \n")
                        student_data = []
                        for field in attribute_name:
                            value = input("Enter " + field + ": ")
                            student_data.append(value)
                        updated_data.append(student_data)
                        print("Data saved successfully! ")
                        
                        print
                    else:
                        updated_data.append(row)
                    counter += 1
                    
        #checks if the student record is found or not
        if index_student is not None:
            with open(attendance_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("ID Number not found in our database!")

        print("\n")

    #function to delete student records
    def deleteAttendance():
        global attribute_name
        global attendance_database

        print("\nDelete Student Information\n")
        idnumber = input("Enter ID Number to delete: ")
        updated_data=[]
        attendance_found = False
        with open(attendance_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if idnumber != row[0]:
                        updated_data.append(row)
                    else:
                        attendance_found = True
    #checks if the student record is found or not
        if attendance_found is True:
            with open(attendance_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("ID Number", idnumber, "deleted successfully!")

    #if no record is found
        else:
            print("ID Number not found in our database!\n")

        print("\n")


