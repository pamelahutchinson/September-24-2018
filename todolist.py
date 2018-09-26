
tasks = []
count = 0


#************************************
class Task:
    def __init__(self,title,priority):

        global count

        self.title = title
        self.priority = priority
        count += 1
        self.taskid = count



def delete_task_by_id(task_id):

    index_to_delete = -1 

    for index in range(0,len(tasks)):
        if(tasks[index].taskid == task_id):
            index_to_delete = index 
            break 
    
    return index_to_delete




while True:

    title = input("Enter task title or q to quit: ")
    if (title == "q"):
        break

    priority = input("Enter HIGH/MEDIUM/LOW priority: ")
    
    task = Task(title,priority)
    tasks.append(task)
    

    view_add = input("Press (v) to view Task list or press (any key) to add another task: ")

    if (view_add == "v"):
        for task in tasks:
            #sorted(tasks, key=lambda task:task.priority)
            print(task.taskid,".",task.title,"-",task.priority)

        delete_task = input("Press (d) to delete a specific task, press (any key) to add another task or press (q) to quit app: ")   
        
        if (delete_task == "d"):
            which_task = int(input("Please select task number: "))

            index_to_delete = delete_task_by_id(which_task)
            if(index_to_delete >= 0):
                del tasks[index_to_delete]

            #del tasks[which_task - 1]
            for task in tasks:
                print(task.taskid,".",task.title,"-",task.priority)
                
        elif(delete_task == "q"):
            break
        else:
            continue
    
print("Thank you for using the App!!")