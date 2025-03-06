import time
import ast

def get_last_id():
    last_line = None
    with open("database.txt", "r") as database:
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
    task_object = {"id": get_last_id(),"task": task, "date": readable_date}
    database = open("database.txt", "a")
    database.write(str(task_object) + "\n")
    database.close()
def print_tasks():
    database = open("database.txt", "r")
    print(database.read())
def prompt_task():
    while True:
        print("1 - adicionar tarefa || 2 - listar tarefas || 0 - sair")
        input_result = input()

        if input_result == "0":
            break
        elif input_result == "2":
            print_tasks()
        elif input_result == "1":
            task_input = input("Tarefa: ")
            save_task(task_input)
    
prompt_task()
