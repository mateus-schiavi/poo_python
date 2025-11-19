from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Lista de frutas (contagem)
fruits = ["Maçã", "Banana", "Uva", "Melão", "Maracujá",
          "Laranja", "Melancia", "Pêra", "Abacaxi", "Laranja",
          "Tangerina", "Uva", "Banana"]

print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4 Remake", 300, 4.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
students = {
    "Pedro": 23,
    "Ana": 23,
    "Ronaldo": 26,
    "Janaina": 25,
}
a = sorted(students.items(), key=itemgetter(0))
print(a)

deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
deq.pop()
print(deq)
