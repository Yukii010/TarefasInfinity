alunos = {}

while True:
    print("Escolha uma opção:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Visualizar alunos")
    print("4 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        nome = input("Nome do aluno: ")
        matricula = input("Número de matrícula: ")

        alunos[matricula] = nome

    elif escolha == "2":
        matricula = input("Número de matrícula do aluno: ")

        if matricula in alunos:
            del alunos[matricula]
        else:
            print("Aluno não encontrado.")

    elif escolha == "3":
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

    elif escolha == "4":
        break

    else:
        print("Opção inválida.")

