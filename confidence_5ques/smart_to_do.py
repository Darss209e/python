def menu():
    menu_list = ['1.ADD TASK', '2.VIEW TASK','3.COMPLETE TASK','4.DELETE TASK','5.EXIT']
    for item in menu_list:
        print(item)

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task[0] + "," + str(task[1]) + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                name, status = line.strip().split(",")
                tasks.append([name, status == "True"])
    except:
        pass

tasks = []
load_tasks()
while True:
    menu()
    choice = input("enter your choice: ")

    if choice == "1":
        task = input("enter your task: ")
        tasks.append([task,False])
        save_tasks()
        print("task added!!")
        
    elif choice == "2":
        if len(tasks)==0:
            print("no task available")
        else:
            for i in range(len(tasks)):
                task_name = tasks[i][0]
                status = tasks[i][1]

                if status:
                    print(i + 1, ".", task_name, "✅")
                else:
                    print(i + 1, ".", task_name, "❌")

    elif choice == "3":
        if len(tasks) == 0:
            print("no task available")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i][0])

        num = int(input("enter task number to complete: "))
        tasks[num - 1][1] = True
        save_tasks()
        print("task marked as completed!")   

    elif choice == "4":
        if len(tasks)==0:
            print("no task available to delete")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i][0])
            num = int(input("enter the number of task to delete: "))   

            tasks.pop(num -1)
            save_tasks()
            print("task deleted!!")


            


