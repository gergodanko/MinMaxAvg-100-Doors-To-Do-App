command=None
while command!="list" and command!="add" and command!="mark" and command!="archive":
    command=str(input("Please specify your command [list, add, mark archive]"))
    print(command)

with open("todo.txt", "r") as file_handle:
    lines=file_handle.readlines()
if command=="add":
    with open("todo.txt", "a") as file_handle:
        task=str(input("Add an item: "))
        file_handle.write("[] " + task + "\n")
        print("Item added")
if command=="list":
    print("You saved the following to do items:")
    for i in range(len(lines)):
        print("{0}. {1}".format(i+1,lines[i]))
if command=="mark":
    print("You saved the following to do items:")
    for i in range(len(lines)):
        print("{0}. {1}".format(i+1,lines[i]))
    mark=int(input("Which one do you want to mark as completed? "))
    with open("todo.txt","w") as file_handle:
        for i in range(len(lines)):
            if i+1!=mark:
                file_handle.write(lines[i])
            elif i+1==mark:
                file_handle.write(lines[i][0] + "x" +lines[i][1:])
    print("Task {0} is marked as completed!".format(mark))
if command=="archive":
    with open("todo.txt","w") as file_handle:
        for i in range(len(lines)):
            if lines[i][1]=="x":
                continue
            else:
                file_handle.write(lines[i])
    print("All completed tasks got deleted!")



            

