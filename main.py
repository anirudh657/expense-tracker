import csv


expenses = []


def add_expense():
    print("\n----- Add Expense -----")

    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount! Expense Not Added.")
        return

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

def total_expense():
    print("\n----- Total Expense -----")

    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense =", total)       

def fix_year(y):
    if len(y) == 2:
        y = "20" + y
    return int(y)


def monthly_report():
    print("\n----- Monthly Report -----")

    month = input("Enter Month and Year (MM-YYYY): ")
    m, y = month.split("-")

    total = 0
    found = False

    for expense in expenses:
        day, mon, year = expense["date"].split("-")

        if int(mon) == int(m) and fix_year(year) == fix_year(y):
            print("-----------------------")
            print("Date :", expense["date"])
            print("Category :", expense["category"])
            print("Amount :", expense["amount"])
            print("Note :", expense["note"])
            total = total + expense["amount"]
            found = True

    if found == False:
        print("No Expenses Found.")
    else:
        print("-----------------------")
        print("Total Expense =", total)

def export_to_csv():
    print("\n----- Export to CSV -----")

    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Date", "Category", "Amount", "Note"])

        for expense in expenses:
            writer.writerow([
                expense["date"],
                expense["category"],
                expense["amount"],
                expense["note"]
            ])

    print("Expenses Exported Successfully!")        

def menu():
    print("=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Monthly Report")
    print("7. Export to CSV")
    print("8. Exit")


while True:
    menu()

    choice = input("Enter your choice: ")
    print("You entered:", choice)

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        total_expense()

    elif choice == "6":
        monthly_report()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")