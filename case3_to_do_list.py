
to_do_list = []
is_on = True

while is_on:
    print("=========================================================================================================")
    option = int(input("-> press 1 to add task\n-> press 2 to see your task\n-> press 3 to complete a task\n-> press 4 to finish session\n-> enter your option: "))
    if option == 1:
        print("=========================================================================================================")
        task = input("please enter the task to add to the list: ")
        to_do_list.append(task)
        print("task added to list")
    elif option == 2:
        print("=========================================================================================================")
        print("this is your to do list...")
        for task in to_do_list:
            print(task, sep=" ")
    elif option == 3:
        print("=========================================================================================================")
        complete_task = input("please enter the task you want to complete: ")
        for task in to_do_list:
            if task == complete_task:
                to_do_list.remove(task)
                print("task completed...")
    elif option == 4:
        print("=========================================================================================================")
        print("shutting down system...")
        is_on = False
    else:
        print("invalid option")

