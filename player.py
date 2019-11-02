class Player:
    def __init__(self):
        self.name = 'Rolf'
        self.numbers = (5,6,7,8,9)

    def total(self):
        return sum(self.numbers)

player = Player()
print(player.name)
print(player.numbers)