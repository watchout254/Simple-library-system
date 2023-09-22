import sys

def actions():
    print(f"1.Add User\n"
          f"2.View user\n"
          f"3.Add book\n"
          f"4.View books\n"
          f"5.User Delete book\n"
          f"6.Delete book\n"
          f"7.Exit\n")

print(f"Welcome to Mukenyas's Library System (MLS)")
admin = input("Your name please: ").lower()
if admin == "admin":
    password = int(input("Password: "))
    if password == 12345:
        print(f"Welcome {admin}")
        actions()
        print(f"Choose from these above options")
        choice = int(input("Choice: "))


        if choice == 1:
            jina = input("Name: ").lower()
            role = input("Role: ").lower()
            no = int(input("Number: "))

            print(f"{jina},{role},{no} is added successfully.")

        #elif choice == 2:

        #elif choice == 3:

        #elif choice == 4:

        #elif choice == 5:

        #elif choice == 6:

        #elif choice == 7:
            #sys.exit()

    else:
        print("Wrong password.")

else:
    print("Wrong credentials. Sorry....")
    sys.exit()

