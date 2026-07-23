expenses = []




def add_expense():
    print("\n----- Add Expense -----")

    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    note = input("Enter Note: ")

    expense = {}

    expense["category"] = category
    expense["amount"] = amount
    expense["note"] = note

    expenses.append(expense)

    print("Expense Added Successfully!")


def menu():
    print("\n" + "=" * 40)
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

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        print("✅ View Expense Selected")

    elif choice == "3":
        print("✅ Search Expense Selected")

    elif choice == "4":
        print("✅ Delete Expense Selected")

    elif choice == "5":
        print("✅ Total Expense Selected")

    elif choice == "6":
        print("👋 Thank You!")
        break

    else:
     print("Invalid Choice")
        