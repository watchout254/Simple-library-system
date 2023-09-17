#Title: Library management system
#Author: Daniel Mukenya Nyongesa
#License: MIT
#Date: 9/7/2023
#Simple system

import sys

def librarian():
          print(f"1. Add book\n"
                f"2. view books\n"
                f"3. Delete books\n"
                f"4. Issue books\n"
                f"5. Return books\n")
          
def student():
      admin_no = int(input("Admission number: \n"))
      name = input("Student's name: \n")
      form = int(input("Form(1,2,3,4):\n"))

def staff():
      teachers_no = int(input("Staff's number: \n"))
      name = input("Staff's name: \n")



print(f"********************************************************************FRADS SCHOOL ********************************************************************\n"
      "********************************************************************LIBRARY MANAGEMENT SYSTEM********************************************************************\n")
print(f"\t\t\t\t\t\tAre you a(an):\n"
      f"\t\t\t\t1.Admin(Librarian)\n"
      f"\t\t\t\t2.Student\n"
      f"\t\t\t\t3.Staff\n")
wozzah = int(input("Choose one to enter details: \n"))
if wozzah == 1:
      librarian()

elif wozzah == 2:
      student()

else:
      staff()
