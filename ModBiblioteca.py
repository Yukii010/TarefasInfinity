modulename = "gerenciamento_alunos"

alunos = {}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")

    matricula = input("Digite o número de matrícula do aluno: ")

    alunos[matricula] = nome

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")

    del alunos[matricula]

def atualizar_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")

    nome = input("Digite o novo nome do aluno: ")

    alunos[matricula] = nome

def ver_alunos():
    for matricula, nome in alunos.items():
        print(f"Matrícula: {matricula} - Nome: {nome}")

if __name__ == "__main__":
    while True:
        print("Escolha uma opção:")
        print("1 - Adicionar aluno")
        print("2 - Remover aluno")
        print("3 - Atualizar aluno")
        print("4 - Listar alunos")
        print("0 - Sair")

        opcao = int(input())

        if opcao == 1:
            adicionar_aluno()
        elif opcao == 2:
            remover_aluno()
        elif opcao == 3:
            atualizar_aluno()
        elif opcao == 4:
            ver_alunos()
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

            
