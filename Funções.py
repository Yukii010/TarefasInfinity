def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10"
    else:
        return "Aprovado"

notas = []
while True:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

    resposta = input("Deseja continuar? (S/N): ")
    if resposta.strip().upper() == "N":
        break

media = calcular_media(notas)

situacao = verificar_situacao(media)

print(f"Média: {media}")
print(f"Situação: {situacao}")

