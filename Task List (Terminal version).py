# to do list app

def edit(todo):
    choice = int(input("Enter the list no. you want to edit: "))-1
    if 0 <= choice <= len(todo):
        edit = input("Enter Edited to-do: ")
        todo[choice] = edit
        print("Edited Successfully")
    else:
        print("Invalid task number")
def delete(todo):
    choice = int(input("Enter the to-do to delete: "))-1
    if 0 <= choice <= len(todo):
        removed = todo.pop(choice)
        print(f"Removed {removed} successfully")
    else:
        print("Invalid task number")
def add(todo):
    add = input("Enter the new todo list: ")
    todo.append(add)
    print(f"Added task : {add} successfully")

def view_all(todo):
    if not todo:
        print("No tasks found")
    else:
        for idx,task in enumerate(todo,start = 1):
            print(f"{idx}.{task}")

print("Welcome to to-do list app (terminal version)")
todo = []
flag = True
while(flag == True):
    operation =  input("Enter operation (view all, edit, delete, mark, add: ").lower()
    match operation:
        case "view all":
            view_all(todo)

        case "edit":
            view_all(todo)
            edit(todo)

        case "delete":
            view_all(todo)
            delete(todo)

        case "add":
            add(todo)

        case "exit":
            flag = False
            print("Exited Operation")
        case _:
            print("Enter valid operation")



