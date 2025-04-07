# todo.py

class ToDoApp:
    def __init__(self):
        self.todos = []

    def show_menu(self):
        print("\n--- To-Do List App ---")
        print("1. Add To-Do")
        print("2. View To-Dos")
        print("3. Remove To-Do")
        print("4. Exit")

    def add_todo(self):
        todo = input("Enter your to-do: ")
        self.todos.append(todo)
        print(f"'{todo}' added to your to-do list.")

    def view_todos(self):
        if not self.todos:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for idx, todo in enumerate(self.todos, 1):
                print(f"{idx}. {todo}")

    def remove_todo(self):
        self.view_todos()
        try:
            choice = int(input("\nEnter the number of the to-do you want to remove: "))
            removed = self.todos.pop(choice - 1)
            print(f"'{removed}' removed from your to-do list.")
        except (ValueError, IndexError):
            print("Invalid choice, please try again.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.add_todo()
            elif choice == '2':
                self.view_todos()
            elif choice == '3':
                self.remove_todo()
            elif choice == '4':
                print("Exiting To-Do List App.")
                break
            else:
                print("Invalid choice, please choose again.")

