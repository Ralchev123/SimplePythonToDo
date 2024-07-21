
def list_tasks():
     f = open("tasks.txt", "r") 
     print(f.read())
     f.close()

def add_tasks():
    f = open("tasks.txt", "a")
    essen = input("What do you want to add?: ")
    f.write('\n' + essen)
    f.close()

def remove_task(one_to_remove):  
    f = open("tasks.txt", "r")
    lines = f.readlines()
    f.close()
    p = 0
    f = open("tasks.txt", "w")
    for index,p in enumerate(lines):
        if index != one_to_remove - 1:
            f.write(p + '\n')
    f.close()


print("\n\nWelcome to the To Do app. What do you want to do?\n")
print("------------------------------\n")
print("1. List existing tasks\n")
print("2. Add a new task\n")
print("3. Remove a task\n")
print("4. Quit\n")


while 1:
    feed = input("Enter your choice: ")
    feed = int(feed)
    if feed == 1:
        print("You choose to list tasks")
        list_tasks()
    elif feed == 2:
        print("You choose to add a new task")
        add_tasks()
    elif feed == 3:
        print("You chose to remove a task")
        list_tasks()
        one_to_remove = input("Which tasks do you want to remove(1-the top one, 2 - the second from top to bottom and so on)?: ")
        one_to_remove = int(one_to_remove)
        remove_task(one_to_remove)
    elif feed == 4:
        print("Quit")
        exit()
    else:
        print("Non valid option(Valid options: 1, 2, 3, 4). Try again")






    