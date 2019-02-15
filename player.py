class Player:

    def __init__(self, gold_coins=0, health_points=10, lives=5):
        self.coins = gold_coins
        self.health = health_points
        self.lives = lives

    def __str__(self):
        return "This is your player. They have {} gold coins, their health is currently at {}, and you have {} lives remaining".format(self.coins, self.health, self.lives)

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.coins += 1
        if self.coins % 10 == 0:
            self.level_up()

    def do_battle(self, damage):
        self.health -= damage
        if self.health < 0:
            self.lives -= 1
            self.health = 10
            if self.lives < 0:
                self.restart()

    def restart(self):
        return self.__init__()

my_player = Player()
print(my_player)
my_player.collect_treasure()
my_player.collect_treasure()
my_player.collect_treasure()
my_player.collect_treasure()
my_player.collect_treasure()
print(my_player)
my_player.do_battle(16)
print(my_player)
