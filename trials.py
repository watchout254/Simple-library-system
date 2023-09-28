import sys

books_avail = [
    {
        "id": 100001,
        "Title": "How to get away with murder",
        "Author": "Annalise Keating",
        "Status": "Available"
    },

    {
        "id": 100002,
        "Title": "Game of Thrones",
        "Author": "Khaleesi",
        "Status": "Available"
    }
]

def actions():
    print(f"1.Add User\n"
          f"2.View user\n"
          f"3.Add book\n"
          f"4.View books\n"
          f"5.User Delete book\n"
          f"6.Delete book\n"
          f"7.Exit\n")
new_book = {}
def add_book():
    id = int(input("Book ID: "))
    title = input("Title: ")
    author = input("Author: ")
    status = input("Status(Available/Unavailable): ")
    print(f"{id},{title},{author},{status} added successfully")

again = False
while not again:
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

                elif choice == 2:
                    print(admin)

                elif choice == 3:
                    add_book()

                elif choice == 4:
                   print(books_avail)

                elif choice == 5:
                    print(books_avail)
                    ans = input("Are you sure you want to delete this? ").lower()
                    if ans == "yes":
                        password = int(input("Password: "))
                        if password == 12345:
                            del books_avail
                            print(f"{admin} deleted the books successfully!")
                    else:
                        print("Bye user.")
                        sys.exit()

                elif choice == 6:
                    sure = input("Are you sure you want to delete? ").lower()
                    if sure == "yes":
                        del books_avail
                        print("Deleted successfully!!!!!")
                    else:
                        sys.exit()

                elif choice == 7:
                    print("Closing the program.....")
                    sys.exit()

            else:
                print("Wrong password.")

        else:
            print("Wrong credentials. Sorry....")
            sys.exit()

