def main():
    task = []
    while True:
        print("------- To Do List App ------")
        print("1. Add Tasks")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            n = int(input("How many tasks you want to add: "))
            for t in range(n):
                task_name = input("Enter task name: ")
                task.append({"Task": task_name, "Done": False})
                print("Task added!!")
        elif choice == '2':
            print("Tasks: ")
            for i, t in enumerate(task):
                status = "Done" if t["Done"] else "Not Done" 
                print(f"{i + 1}. {t['Task']} - {status}")
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(task):
                task[task_index]["Done"] = True
                print("Task marked as done!!")
            else:
                print("Invalid task number")
        elif choice == '4':
            print("Exit app")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()