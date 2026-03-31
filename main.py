from functions import *
from storage import load_data, save_data

def menu():
    while True:
        print("=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add")
        print("2. Show")
        print("3. Find")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        option = input("Choose an option: ")
        # while option not in ["1", "2", "3", "4", "5", "6"]:
        #     print("Invalid option. Try again.\n")
        #     option = input("Choose an option: ")


        if option == "1":
            add_student()
        elif option == "2":
            show_students()
        elif option == "3":
            find_student()
        elif option == "4":
            update_student()
        elif option == "5":
            delete_student()
        elif option == "6":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


# Load data before starting
load_data() # Cargar datos antes de iniciar


# Run program
menu()


