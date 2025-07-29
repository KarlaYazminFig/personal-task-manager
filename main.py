########## Personal Task Manager (basic - intermediate)
from colorama import Fore, Style
class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title} - Description: {self.description} - Status: {self.status}"
    
class Task_manager:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.task = []

    def __str__(self):
        return f"User name: {self.username} | Email: {self.email}"

    def add_task(self, task):
        found = False
        for i in self.task:
            if i.title == task.title and i.description == task.description:
                found = True
                print(f"{Fore.YELLOW}{task} is already registered{Style.RESET_ALL}")
        
        if found == False:
            if task.title != "" and task.description != "" and task.status != "":
                self.task.append(task)
                print(f"{Fore.GREEN}{task} | Has been added{Style.RESET_ALL}")
            else:
                print(Fore.YELLOW + "Incomplete information. Please try again" + Style.RESET_ALL)

    def show_all_task(self):
        if not self.task:
            print(Fore.YELLOW + "You have not yet registered any task" + Style.RESET_ALL)
        else:
            for i in self.task:
                print(i)

    def show_one_task(self, title):
        found = False
        if not self.task:
            print(Fore.YELLOW + "You have not yet registered any task" + Style.RESET_ALL)
            return
        else:
           for i in self.task:
               if i.title == title:
                   print(i)
                   found = True
                   
        if found == False:
            print(f"{Fore.YELLOW}{title} is not registered{Style.RESET_ALL}")

    def change_status(self, title, description, status):
        found = False
        if not self.task:
            print(Fore.YELLOW + "You have not yet registered any task" + Style.RESET_ALL)
            return
        else:
            for i, todo in enumerate(self.task):
                if todo.title == title and todo.description == description:
                    found = True
                    print(f"{Style.BRIGHT}Current state: {todo.status}{Style.RESET_ALL}")
                    x = input("Do you want to change the status? si/no: ").lower()
                    if x == "si":
                        task = Task(title,description,status)
                        self.task[i] = task
                        print(Fore.GREEN + "Status modified" + Style.RESET_ALL)
                    else:
                        print("The status has not been unchanged")
        if found == False:
            print(f"{Fore.YELLOW}The task is not registered{Style.RESET_ALL}")

    def delete_task(self, title, description):
        found = False
        if not self.task:
            print(Fore.YELLOW + "You have not yet registered any task" + Style.RESET_ALL)
            return
        else:
            for i in self.task:
                if i.title == title and i.description == description:
                    found = True
                    x = input(f"{i} | Do you want to delete? yes/no: ").lower()
                    if x == "yes":
                        self.task.remove(i)
                        print(f"{Style.BRIGHT}{i} | Has been deleted{Style.RESET_ALL}")
                    else:
                        print("The task has not been deleted")
                
        if found == False:
            print(f"{Fore.YELLOW}The task is not registered{Style.RESET_ALL}")

u1 = Task_manager("Carlos Fierro", "CarlosFi@gmail.com")

def menu():
    count = 1
    y = False
    while y == False:
        pin1 = "1234"
        if count <= 3:
            print(Style.BRIGHT + "PERSONAL TASK MANAGER" + Style.RESET_ALL)
            pin2 = input(Style.BRIGHT + "PASSWORD: " + Style.RESET_ALL)
            if pin1 == pin2:
                y = True
                while True: 
                    print()
                    print(f"{Style.BRIGHT}**************************************")
                    print("******* PERSONAL TASK MANAGER *******")
                    print("----------- M E N U -----------")
                    print("1. Add task")
                    print("2. Show all task")
                    print("3. Show one task")
                    print("4. Change task status")
                    print("5. delete task")
                    print("6. Go out")

                    try:
                        option = int(input(f"Enter a number: {Style.RESET_ALL}"))
                        print()

                        if option == 1:
                            title = input("Add task title: ").lower()
                            description = input("Add task description: ").lower()
                            status = input("Add status: ").lower()
                            task = Task(title, description,status)
                            u1.add_task(task)
                            continue

                        elif option == 2:
                            u1.show_all_task()
                            continue

                        elif option == 3:
                            title = input("Task title: ").lower()
                            u1.show_one_task(title)
                            continue

                        elif option == 4:
                            title = input("Task title: ").lower()
                            description = input("Task description: ").lower()
                            status = input("Enter new status: ").lower()
                            u1.change_status(title,description,status)
                            continue

                        elif option == 5:
                            title = input("Task title: ").lower()
                            description = input("Task description: ").lower()
                            u1.delete_task(title,description)
                            continue

                        elif option == 6:
                            break

                        else:
                            print("Please enter a number in the range 1 - 6")
        
                    except ValueError:
                        print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")
                        continue

            else:
                print(Fore.YELLOW + "Incorrect password. You have only three attempts before access is locked" + Style.RESET_ALL)
                print(f"{Fore.YELLOW}Attempt number: {count}{Style.RESET_ALL}")
                count += 1
                continue    
        
        else:
            print()
            print(f"{Fore.RED}ACCESS LOCKED{Style.RESET_ALL}")
        break
menu()