# 🎯 Campo Minado com Bandeiras (Terminal)

Este é um jogo de **Campo Minado** feito em Python, jogado totalmente no terminal. Ele implementa mecânicas clássicas do jogo original, com adição de **bandeiras**, **níveis de dificuldade** e **ranking de jogadores**.

---

## 🕹️ Como Jogar

1. **Execute o arquivo Python**:
   ```bash
   python campo_minado.py
2. Escolha a dificuldade:

1 - Fácil (5x5, 5 minas)

2 - Médio (7x7, 10 minas)

3 - Difícil (10x10, 20 minas)

3. Ações disponíveis:

[J]ogar → Revelar uma célula

[B]andeira → Colocar ou remover uma bandeira


🚩 Bandeiras
Você começa com 3 bandeiras a mais que o número total de minas.

Bandeiras removidas não podem ser reutilizadas.

Bandeiras são representadas por:

F → Bandeira em posição errada

✓ → Bandeira corretamente colocada sobre uma mina

🧠 Regras
Se revelar uma célula com uma mina: 💥 você perde.

Se revelar todas as células sem minas: 🏆 você vence.

O número exibido após revelar uma célula indica quantas minas estão ao redor daquela posição.

📄 Funcionalidades
Seleção de nível de dificuldade.

Controle de quantidade de bandeiras disponíveis.

Contador de jogadas.

Sistema de ranking salvo em ranking.txt.

Interface em modo texto, com coordenadas claras para jogadas.

Códigos organizados e comentados para fácil entendimento.

