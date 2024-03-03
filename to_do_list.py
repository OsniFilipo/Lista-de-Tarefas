# Definindo a classe ToDoList para representar a lista de tarefas
class ToDoList:
    # Método inicializador da classe para criar uma lista vazia de tarefas
    def __init__(self):
        self.tasks = []

    # Método para adicionar uma nova tarefa à lista
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})  # Adiciona a nova tarefa à lista de tarefas
        print("Tarefa adicionada com sucesso.")  # Informa ao usuário que a tarefa foi adicionada com sucesso

    # Método para marcar uma tarefa como concluída
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):  # Verifica se o índice fornecido é válido
            self.tasks[index]["completed"] = True  # Marca a tarefa como concluída
            print("Tarefa concluída.")  # Informa ao usuário que a tarefa foi concluída
        else:
            print("Índice inválido.")  # Informa ao usuário que o índice fornecido é inválido

    # Método para excluir uma tarefa da lista
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):  # Verifica se o índice fornecido é válido
            del self.tasks[index]  # Remove a tarefa da lista de tarefas
            print("Tarefa excluída.")  # Informa ao usuário que a tarefa foi excluída
        else:
            print("Índice inválido.")  # Informa ao usuário que o índice fornecido é inválido

    # Método para exibir a lista de tarefas
    def show_tasks(self):
        if self.tasks:  # Verifica se a lista de tarefas não está vazia
            print("Lista de Tarefas:")
            # Itera sobre as tarefas na lista e exibe cada uma com seu status (concluída ou pendente)
            for i, task in enumerate(self.tasks):
                status = "Concluída" if task["completed"] else "Pendente"
                print(f"{i+1}. {task['task']} - {status}")
        else:
            print("A lista de tarefas está vazia.")  # Informa ao usuário que a lista de tarefas está vazia

# Função principal para executar o programa
def main():
    to_do_list = ToDoList()  # Cria uma instância da classe ToDoList para representar a lista de tarefas
    
    # Loop principal do programa
    while True:
        # Exibe o menu de opções para o usuário
        print("\n=== Menu ===")
        print("1. Adicionar Tarefa")
        print("2. Concluir Tarefa")
        print("3. Excluir Tarefa")
        print("4. Exibir Tarefas")
        print("5. Sair")

        choice = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu

        # Verifica a opção escolhida pelo usuário e executa a ação correspondente
        if choice == "1":
            task = input("Digite a tarefa a ser adicionada: ")  # Solicita ao usuário a tarefa a ser adicionada
            to_do_list.add_task(task)  # Chama o método add_task para adicionar a tarefa à lista
        elif choice == "2":
            index = int(input("Digite o índice da tarefa concluída: ")) - 1  # Solicita ao usuário o índice da tarefa concluída
            to_do_list.complete_task(index)  # Chama o método complete_task para marcar a tarefa como concluída
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a ser excluída: ")) - 1  # Solicita ao usuário o índice da tarefa a ser excluída
            to_do_list.delete_task(index)  # Chama o método delete_task para excluir a tarefa da lista
        elif choice == "4":
            to_do_list.show_tasks()  # Chama o método show_tasks para exibir a lista de tarefas
        elif choice == "5":
            print("Saindo...")  # Informa ao usuário que o programa será encerrado
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida.")  # Informa ao usuário que a opção escolhida é inválida

# Verifica se o arquivo está sendo executado como o programa principal
if __name__ == "__main__":
    main()  # Chama a função main para iniciar o programa
