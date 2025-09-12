class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    score = 0

game1 = Game()
# print(game1)
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.score = 9.5

print("Dados do Jogo")
print(f"Nome do jogo: {game1.name}\nAno de lançamento: {game1.yearLaunch}")

game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.score = 8.0

print("Dados do Jogo")
print(f"Nome do jogo: {game2.name}\nAno de lançamento: {game2.yearLaunch}")
