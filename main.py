# csv is a built-in Python module for reading/writing CSV files
# we need it here for export_to_csv(), which uses csv.writer() to save expenses.csv
import csv


# empty list to store all expenses (each expense will be a dictionary)
# it's empty at the start because no expenses have been added yet
# every function (add/view/delete/etc.) reads from or writes to this same list
expenses_list = []


def add_expense():
    print("\n----- Add Expense -----")

    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        # if amount is not a valid number, stop here
        print("Invalid Amount! Expense Not Added.")
        return

    note = input("Enter Note: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    # .append() -> adds item to end of list: [1,2].append(3) = [1,2,3]
    expenses_list.append(expense)

    print("\nExpense Added Successfully!")


def delete_expense():
    print("\n----- Delete Expense -----")

    # if list is empty, there is nothing to delete
    if len(expenses_list) == 0:
        print("No Expenses Available.")
        return

    print("\nExpense List:")

    number = 1

    # go through each expense one by one and print it
    for x in expenses_list:
        print(number)
        print("Date :", x["date"])
        print("Category :", x["category"])
        print("Amount :", x["amount"])
        print("Note :", x["note"])
        print("-----------------------")

        number = number + 1

    choice = int(input("Enter Expense Number to Delete: "))

    # check if the entered number is a valid expense number
    if 1 <= choice <= len(expenses_list):
        # .pop(index) -> removes and returns item at that index: [1,2,3].pop(0) = 1, list becomes [2,3]
        expenses_list.pop(choice - 1)
        print("Expense Deleted Successfully!")
    else:
        # runs when the number entered is out of range
        print("Invalid Expense Number!")


def view_expenses():
    print("\n----- View Expenses -----")

    # if list is empty, there is nothing to show
    if len(expenses_list) == 0:
        print("No Expenses Found.")
        return

    number = 1

    # go through each expense one by one and print it
    for x in expenses_list:
        print("-----------------------")
        print("Expense Number :", number)
        print("Date :", x["date"])
        print("Category :", x["category"])
        print("Amount :", x["amount"])
        print("Note :", x["note"])

        number = number + 1


def category_expense():
    print("\n----- Category Expenses -----")

    input_category = input("Enter Category: ")

    found = False

    # go through each expense and check its category
    for x in expenses_list:
        # .lower() -> converts text to lowercase: "HELLO".lower() = "hello"
        # if this expense's category matches what the user typed
        # input_category.lower(): FOOD.lower() = food
        # x["category"].lower(): food.lower() = food
        # FOOD!=food, but FOOD.lower() == food.lower()
        if x["category"].lower() == input_category.lower():
            print("-----------------------")
            print("Date :", x["date"])
            print("Category :", x["category"])
            print("Amount :", x["amount"])
            print("Note :", x["note"])
            found = True

    # if we never found a match, tell the user
    if found == False:
        print("No Expense Found.")

def total_expense():
    print("\n----- Total Expense -----")

    # if list is empty, there is nothing to total
    if len(expenses_list) == 0:
        print("No Expenses Found.")
        return

    total = 0

    # add up the amount of every expense
    for x in expenses_list:
        total = total + x["amount"]

    print("Total Expense =", total)       

def fix_year(y):
    # if year is short like "26", turn it into "2026"
    if len(y) == 2:
        y = "20" + y
    return int(y)


def monthly_report():
    print("\n----- Monthly Report -----")

    input_month = input("Enter Month and Year (MM-YYYY): ")
    # .split("-") -> breaks text into a list using "-": "07-2026".split("-") = ["07", "2026"]
    m, y = input_month.split("-")

    total = 0
    found = False

    # go through each expense and check its date
    for x in expenses_list:
        # .split("-") -> breaks text into a list using "-": "28-07-2026".split("-") = ["28", "07", "2026"]
        day, mon, year = x["date"].split("-")

        # if this expense's month and year match what the user entered
        # int(mon) == int(m)   -> compares month numbers (turns "07" and "7" into 7 == 7, so text formatting doesn't matter)
        # fix_year(year) == fix_year(y) -> compares years after making both 4-digit (so "26" and "2026" are treated as equal)
        # "and" means BOTH checks must be true for this expense to count as a match
        if int(mon) == int(m) and fix_year(year) == fix_year(y):
            print("-----------------------")
            print("Date :", x["date"])
            print("Category :", x["category"])
            print("Amount :", x["amount"])
            print("Note :", x["note"])
            total = total + x["amount"]
            found = True

    # if we never found a match, tell the user
    if found == False:
        print("No Expenses Found.")
    else:
        print("-----------------------")
        print("Total Expense =", total)

# this function saves all expenses into a CSV file (like an Excel sheet)
def export_to_csv():
    # show a heading so the user knows this option started
    print("\n----- Export to CSV -----")

    # check if our expenses list is empty
    if len(expenses_list) == 0:
        # if empty, tell the user and stop here
        print("No Expenses Found.")
        return

    # open (or create) a file named expenses.csv in write mode
    # newline="" stops extra blank lines from appearing between rows
    with open("expenses.csv", "w", newline="") as file:

        # create a writer tool that knows how to write rows into the csv file
        writer = csv.writer(file)

        # write the first row as column titles (headings)
        writer.writerow(["Date", "Category", "Amount", "Note"])

        # go through every expense one by one
        for x in expenses_list:
            # write this expense's details as one row in the file
            writer.writerow([
                x["date"],      # the date of the expense
                x["category"],  # the category (like Food, Travel, etc.)
                x["amount"],    # how much money was spent
                x["note"]       # any extra note about the expense
            ])

    # after the file is closed automatically, tell the user it worked
    print("Expenses Exported Successfully!")

def menu():
    # "=" * 40 -> repeats the "=" character 40 times to draw a separator line
    print("=" * 40)
    print("      EXPENSE TRACKER")
    print("=" * 40)

    # just prints the list of options the user can pick from
    # note: this function only displays the menu, it doesn't read the choice
    # or run anything itself - that happens in the while loop below
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

    # run the option the user picked
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
        export_to_csv()

    elif choice == "8":
        # stop the program
        print("Thank You!")
        break

    else:
        # runs if none of the above choices matched
        print("Invalid Choice")