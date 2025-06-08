import random

print("Campo Minado com Bandeiras\n")

nome = input("Digite seu nome: ")

print("\nEscolha a dificuldade:")
print("\n1 - Fácil (5x5, 5 minas)")
print("2 - Médio (7x7, 10 minas)")
print("3 - Difícil (10x10, 20 minas)")

while True:
    d = input("\nDigite 1, 2 ou 3: ")
    if d == '1':
        tamanho, num_minas = 5, 5
        break
    elif d == '2':
        tamanho, num_minas = 7, 10
        break
    elif d == '3':
        tamanho, num_minas = 10, 20
        break
    else:
        print("Escolha inválida!")


print()

tabuleiro = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
revelado = [[False for _ in range(tamanho)] for _ in range(tamanho)]
bandeiras = [[False for _ in range(tamanho)] for _ in range(tamanho)]

minas = set()
while len(minas) < num_minas:
    minas.add((random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)))

bandeiras_restantes = num_minas + 3
jogadas = 0

def exibir():
    print("\n   " + " ".join(str(i + 1) for i in range(tamanho)))
    

    bandeiras_colocadas = 0
    bandeiras_corretas = 0

    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if bandeiras[i][j]:
                bandeiras_colocadas += 1
                if (i, j) in minas:
                    linha.append('✓')
                    bandeiras_corretas += 1
                else:
                    linha.append('F')
            elif revelado[i][j]:
                linha.append(tabuleiro[i][j])
            else:
                linha.append('#')
        print(f"{i + 1:2} {' '.join(linha)}")

    print("\nStatus do jogo:")
    print(f"Minas totais..............: {num_minas}")
    print(f"Bandeiras disponíveis.....: {bandeiras_restantes}")
    print(f"Bandeiras colocadas.......: {bandeiras_colocadas}")
    print(f"Bandeiras corretas........: {bandeiras_corretas}")

def contar_minas(x, y):
    c = 0
    for i in range(max(0, x - 1), min(tamanho, x + 2)):
        for j in range(max(0, y - 1), min(tamanho, y + 2)):
            if (i, j) in minas:
                c += 1
    return c

while True:
    exibir()
    print()
    acao = input("Ação [J]ogar ou [B]andeira: ").strip().upper()
    if acao not in ['J', 'B']:
        print("Ação inválida.")
        continue
    try:
        x = int(input(f"Linha (1 a {tamanho}): ")) - 1
        y = int(input(f"Coluna (1 a {tamanho}): ")) - 1
    except:
        print("Entrada inválida.")
        continue
    if not (0 <= x < tamanho and 0 <= y < tamanho):
        print("Fora do tabuleiro!")
        continue
    if acao == 'B':
        if bandeiras[x][y]:
            bandeiras[x][y] = False
            print("Bandeira removida (não reutilizável).")
        elif bandeiras_restantes > 0:
            bandeiras[x][y] = True
            bandeiras_restantes -= 1
        else:
            print("Você usou todas as suas bandeiras disponíveis.")
        continue
    if bandeiras[x][y]:
        print("Remova a bandeira antes de jogar.")
        continue
    if revelado[x][y]:
        print("Já revelado.")
        continue

    jogadas += 1
    if (x, y) in minas:
        print("BOOM! Você perdeu!")
        for i, j in minas:
            tabuleiro[i][j] = '*'
            revelado[i][j] = True
        exibir()
        break
    else:
        c = contar_minas(x, y)
        tabuleiro[x][y] = str(c)
        revelado[x][y] = True
        if all(revelado[i][j] or (i, j) in minas for i in range(tamanho) for j in range(tamanho)):
            print("Parabéns! Você venceu!")
            break

with open("ranking.txt", "a") as f:
    f.write(f"{nome}: {jogadas}\n")

try:
    with open("ranking.txt", "r") as f:
        r = []
        for linha in f:
            if ':' in linha:
                n, p = linha.strip().split(':')
                r.append((n.strip(), int(p.strip())))
        r.sort(key=lambda x: x[1], reverse=True)
        print("\nRanking:")
        for i, (n, p) in enumerate(r, 1):
            print(f"{i}. {n} - {p} pontos")
except:
    print("Nenhum ranking disponível.")
