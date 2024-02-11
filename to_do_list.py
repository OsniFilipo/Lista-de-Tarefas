class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Tarefa adicionada com sucesso.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Tarefa concluída.")
        else:
            print("Índice inválido.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Tarefa excluída.")
        else:
            print("Índice inválido.")

    def show_tasks(self):
        if self.tasks:
            print("Lista de Tarefas:")
            for i, task in enumerate(self.tasks):
                status = "Concluída" if task["completed"] else "Pendente"
                print(f"{i+1}. {task['task']} - {status}")
        else:
            print("A lista de tarefas está vazia.")

def main():
    to_do_list = ToDoList()
    
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Tarefa")
        print("2. Concluir Tarefa")
        print("3. Excluir Tarefa")
        print("4. Exibir Tarefas")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a tarefa a ser adicionada: ")
            to_do_list.add_task(task)
        elif choice == "2":
            index = int(input("Digite o índice da tarefa concluída: ")) - 1
            to_do_list.complete_task(index)
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a ser excluída: ")) - 1
            to_do_list.delete_task(index)
        elif choice == "4":
            to_do_list.show_tasks()
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
