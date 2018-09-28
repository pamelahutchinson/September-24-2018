
import json

tasks = []
count = 0


#***********************************
class Task:
    def __init__(self,title,priority):
        global count
        count += 1
        self.taskid = count
        self.title = title
        self.priority = priority
       

    def asDictionary(self):
        return self.__dict__

def print_menu():
    print("****TO DO LIST****")
    print("-------Menu-------")
    print("1.Add New Task")
    print("2.Delete Task")
    print("3.Quit")

def delete_task_by_id(task_id):
    index_to_delete = -1 
    for index in range(0,len(tasks)):
        if(tasks[index].taskid == task_id):
            index_to_delete = index 
            break 
    return index_to_delete



loop = True
while loop:
    print_menu()
    try:
        option = int(input("Select option [1-3]: "))
        if (option == 1):
            title = input("Enter task title: ")
            priority = input("Enter HIGH/MEDIUM/LOW priority: ")
            task = Task(title,priority)
            tasks.append(task.asDictionary())
            view_add = input("Press (v) to view Task list or press (any key) to go back to Main Menu: ")
            if (view_add == "v"):
                for task in tasks:
                    print(task.taskid,".",task.title,"-",task.priority)
            else:
                continue
        elif (option == 2):
            for task in tasks:
                print(task.taskid,".",task.title,"-",task.priority)
            delete_task = input("Press (d) to delete a specific task, press (any key) to go back to the Main Menu: ")  
            if (delete_task == "d"):
                try:
                    which_task = int(input("Please select task number: "))
                    index_to_delete = delete_task_by_id(which_task)
                    if(index_to_delete >= 0):
                        del tasks[index_to_delete]
                        for task in tasks:
                            print(task.taskid,".",task.title,"-",task.priority)
                except ValueError:
                    print("Invalid entry.Please select numerical number from the task!")
                    
            else:
                continue
        elif(option == 3):
            print("You have existed the app.")
            print("Thank you for using the App!!")
            loop = False

    except ValueError:
        print("Invalid numerical entry. Please try again!")
        

with open("to_do_list.json","w") as file_object:
    json.dump(tasks,file_object,indent=2)


with open("to_do_list.json","r") as file_object:
    task_data = json.load(file_object)
    print(task_data)