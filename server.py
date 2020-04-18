import random

ALIVE = 10
SLEEP = 11
DEAD = 12

WHITE = 20
BLACK = 21
RED = 22
YELLOW = 23


class Game:

    def __init__(self, map, players, ships, pirates, coins, rums):
        self.map = map
        self.players = players
        self.pirates = pirates
        self.ships = ships
        self.coins = coins
        self.rums = rums


class Map:

    def __init__(self):
        self.tiles = self.gen_tiles()

    def gen_tiles(self):
        sprite_num = [1, 1, 5, 4, 2, 3, 2, 1, 2, 4, 1, 1, 2, 2, 4, 6, 1, 1, 1, 1, 5, 5, 3, 2, 1, 1, 4, 40, 2, 1, 1, 4, 1, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3]
        tiles = []
        for i in range(143):
            tiles.append(Tile(i, 0, random.choice((0, 90, 180, 270))))
        print(len(tiles))
        print(tiles)
        return tiles

    def get_sprite_num(self, sprite_num):
        expected = random.choice(sprite_num)
        return expected

class Tile:

    def __init__(self, id,  sprite_id,  rot):
        self.id = id
        self.sprite_id = sprite_id
        self.rot = rot


class Player:

    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color


class Pirate:

    def __init__(self, id, sprite_id, state_id, x_px, y_px):
        self.id = id
        self.sprite_id
        self.state_id = state_id
        self.xy_px = [x_px, y_px]


class Ship:

    def __init__(self, id, x_px, y_px):
        self.id = id
        self.sprite_id
        self.xy_px = [x_px, y_px]


class Coin:

    def __init__(self, id, x_px=20, y_px=20):
        self.id = id
        self.sprite_id
        self.xy_px = [x, y]


class Rum:

    def __init__(self, id, x_px=10, y_px=10):
        self.id = id
        self.xy_px = [x, y]


def main():
    print("Hello World!")
    # game = Game()
    map = Map();

main()
