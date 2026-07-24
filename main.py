expenses = []


def add_expense():
    print("\n----- Add Expense -----")

    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    note = input("Enter Note: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)

    print("\nExpense Added Successfully!")


def delete_expense():
    print("\n----- Delete Expense -----")

    if len(expenses) == 0:
        print("No Expenses Available.")
        return

    print("\nExpense List:")

    number = 1

    for expense in expenses:
        print(number)
        print("Date :", expense["date"])
        print("Category :", expense["category"])
        print("Amount :", expense["amount"])
        print("Note :", expense["note"])
        print("-----------------------")

        number = number + 1

    choice = int(input("Enter Expense Number to Delete: "))

    if 1 <= choice <= len(expenses):
        expenses.pop(choice - 1)
        print("Expense Deleted Successfully!")
    else:
        print("Invalid Expense Number!")


def view_expenses():
    print("\n----- View Expenses -----")

    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    number = 1

    for expense in expenses:
        print("-----------------------")
        print("Expense Number :", number)
        print("Date :", expense["date"])
        print("Category :", expense["category"])
        print("Amount :", expense["amount"])
        print("Note :", expense["note"])

        number = number + 1


def category_expense():
    print("\n----- Category Expenses -----")

    category = input("Enter Category: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("-----------------------")
            print("Date :", expense["date"])
            print("Category :", expense["category"])
            print("Amount :", expense["amount"])
            print("Note :", expense["note"])
            found = True

    if found == False:
        print("No Expense Found.")


def menu():
    print("=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Exit")


while True:
    menu()

    choice = input("Enter your choice: ")
    print("You entered:", choice)

    if choice == "1":
        add_expense()

    elif choice == "2":
        print("DEBUG: Inside option 2")
        view_expenses()

    elif choice == "3":
        category_expense()

    elif choice == "4":
        print("DEBUG: Inside option 4")
        delete_expense()

    elif choice == "5":
        print("Total Expense Selected")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")