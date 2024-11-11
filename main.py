def save_task(task):
        database = open("database.txt", "a")
        database.write(task + "\n")
        database.close()
def print_tasks():
    database = open("database.txt", "r")
    print(database.read())
def prompt_task():
    while True:
        print("informe uma tarefa \nDigite 0 para sair")
        input_result = input()

        if input_result == "0":
            break
        else:
            save_task(input_result)
    print_tasks()
    
prompt_task()
