import sys
from component.student import student

if __name__ == '__main__':
        print("WELCOME TO STUDENT ATTENDANCE MANAGEMENT SYSTEM")

        while True:
            print("PRESS FROM THE FOLLOWING OPTION : \n")

            print("PRESS 1 : ADD STUDENT ATTENDANCE INFORMATION.")
            print("PRESS 2 : DELETE STUDENT ATTENDANCE INFORMATION.")
            print("PRESS 3 : UPDATE STUDENT ATTENDANCE INFORMATION.")
            print("PRESS 4 : VIEW ALL STUDENT ATTENDANCE INFORMATION.")
            print("PRESS 5 : SEARCH STUDENT ATTENDANCE INFORMATION.")
            print("PRESS 6 : EXIT SYSTEM.")
            
            try:
                    OPTION = int(input("ENTER YOUR OPTION : "))
                    print(end="\n")

                    if OPTION == 1:
                        student.addAttendance()
                    elif OPTION == 2:
                        student.deleteAttendance()
                    elif OPTION == 3:
                        student.updateAttendance()
                    elif OPTION == 4:
                        student.viewAttendance()
                    elif OPTION == 5:
                        student.searchAttendance()
                    elif OPTION == 6:
                        print("THANK YOU FOR USING STUDENT ATTENDANCE MANAGEMENT SYSTEM! VISIT AGAIN.")
                        sys.exit()

                    else:
                        print ("Invalid Choice.")
                        response = (input("Try again? [Y/N]: ")).upper()
                        print(" ")
                        if response == "Y":
                            continue
                        elif response == "N":
                            break

            except ValueError:
                    print ("Invalid Entry! Input should be a number.")
                    response = (input("Try again? [Y/N]: ")).upper()
                    print(" ")
                    if response == "Y":
                        continue
                    elif response == "N":
                        break