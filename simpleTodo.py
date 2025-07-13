taskList = []


def addTask():
    task_to_add = input("Enter task to add: ")
    if task_to_add:
        taskList.append(task_to_add)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")


def removeTask():
    if not taskList:
        print("The list is empty. No tasks to remove!")
        return
    print("---Tasks in your todo list:---")
    viewTask()
    try:
        user_index = int(input("Enter the index of the completed task: "))
        if 1 <= user_index <= len(taskList):
            taskList.pop(user_index-1)  # pop removes by index
            print(
                f"---Task at given index '{user_index}' removed successfully!---")
        else:
            print("Index out of range!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def viewTask():
    # display index starting from 1
    if taskList:
        for index, task in enumerate(taskList, start=1):
            print(f"{index}: {task}")
    else:
        print("List is empty! No tasks to show!")


def main():
    while True:
        user = input(
            "Enter '1' to add task, '2' to remove task, '3' to view your tasks and '4' to quit: ").strip().lower()
        if user == "1":
            addTask()
        elif user == "2":
            removeTask()
        elif user == "3":
            viewTask()
        elif user == "4":
            print("Thank you for using the app!")
            break
        else:
            print("Invalid Request!")


main()
