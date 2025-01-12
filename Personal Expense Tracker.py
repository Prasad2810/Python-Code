import json

def load_expenses(filename='expenses.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses, filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file)

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    save_expenses(expenses)

def list_expenses(expenses):
    for expense in expenses:
        print(f"Amount: ₹{expense['amount']}, Category: {expense['category']}")

if __name__ == "__main__":
    expenses = load_expenses()
    while True:
        action = input("Enter 'add' to add an expense, 'list' to view expenses, or 'quit' to exit: ")
        if action == 'add':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            add_expense(expenses, amount, category)
        elif action == 'list':
            list_expenses(expenses)
        elif action == 'quit':
            break
        else:
            print("Invalid action.")