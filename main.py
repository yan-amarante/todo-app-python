import time
import ast
import os

YELLOW = "\033[1;33m"
RED_BG = "\033[41m"
GREEN_BG = "\033[42m"
#BLUE_BG = "\033[44m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
#BLUE = "\033[34m"
#RED_TEXT_GREEN_BG = "\033[31;42m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
#print(f"{BOLD}This text is bold.{RESET}")
#print(f"{UNDERLINE}This text is underlined.{RESET}")
#print(f"{RED}This text is red.{RESET}")
#print(f"{RED_TEXT_GREEN_BG}Red text on green background{RESET}")
#print(f"{RED_BG}This has a red background.{RESET}")
def get_last_id():
    last_line = None
    with open("/home/yan/database.txt", "r") as database:
            lines = database.readlines()
            if lines: 
                last_line =  lines[-1].strip()  
            else:
                return 1 
    data_dict = ast.literal_eval(last_line)
    last_id = data_dict["id"]
    return last_id + 1

def save_task(task):
    timestamp = time.time()
    readable_date = time.ctime(timestamp)
    task_object = {"id": get_last_id(),"task": task, "date": readable_date, "status": "Undone"}
    database = open("/home/yan/database.txt", "a")
    database.write(str(task_object) + "\n")
    database.close()

def print_tasks():
    tasks = {}
    count = 0
    with open("/home/yan/database.txt", "r") as database:
        for line in database:
            count += 1
            line.strip()
            if not(line.isspace()):
                tasks.update({"line " + str(count) :ast.literal_eval(line)})

    for key, value in tasks.items():
        if value["status"] == "Undone":
            print(f"{RED}{value}{RESET}")
        elif value["status"] == "in progress":
            print(f"{YELLOW}{value}{RESET}")
        elif value["status"] == "completed":
            print(f"{GREEN}{value}{RESET}")
        else:
            print(f"{value}")

def write_app_commands():
    print(f"{BOLD}1-{RESET}adicionar tarefa  {BOLD}2{RESET}-listar tarefas {BOLD}3-{RESET}editar tarefa {BOLD}0-{RESET}sair")

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def select_task(id):
    with open("/home/yan/database.txt", "r") as database:
        for line in database:
            line.strip()
            if ast.literal_eval(line)["id"] == int(id):
                return ast.literal_eval(line)
            
def edit_line(selected_line, new_status):
        match new_status:
            case "1": selected_line.update({"status": "completed"})
            case "2": selected_line.update({"status": "in progress"})
            case "3": selected_line.update({"status": "Undone"})

        count = 0

        with open("/home/yan/database.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            if ast.literal_eval(line)["id"] == selected_line["id"]:
                break
            count += 1
        lines[count] = str(selected_line) + "\n"
        
        with open("/home/yan/database.txt", "w") as database:
            for line in lines:
                database.write(line)
            database.close()

def prompt_task():
    count = 0
    while True:
        if count == 0:
            clear_terminal()
            write_app_commands()
        count += 1
        input_result = input()

        match input_result:
            case "0":
                clear_terminal()
                break
            case "2":
                print_tasks()
            case "1":
                task_input = input("Tarefa: ")
                save_task(task_input)
                print(f"{GREEN}{BOLD}Tarefa Adicionada{RESET}")
            case "3":
                id = input("Selecione uma tarefa por id: ")
                target_task = select_task(id)
                print(target_task)
                edit_input = input("1-para completa 2-em progresso 3- não completa: ")
                match edit_input:
                    case "1":
                        edit_line(target_task, "1")
                    case "2":
                        edit_line(target_task, "2")
                    case "3":
                         edit_line(target_task, "3")                       
            
prompt_task()
