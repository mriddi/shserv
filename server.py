import random

ALIVE = 10
SLEEP = 11
DEAD = 12

WHITE = 20
BLACK = 21
RED = 22
YELLOW = 23


class Game:

    def __init__(self):
        self.map = Map()
        self.players = self.gen_players()
        self.pirates = pirates
        self.ships = ships
        self.coins = coins
        self.rums = rums

    def gen_players(self):
        return [Player(0, "Nik", WHITE), Player(1, "Pav", BLACK), Player(2, "Koz", RED), Player(3, "Gay", YELLOW)]

    def gen_pirates(self):
        players = []
        for idx in range(4):
            players.append()

    def gen_ships(self):

    def gen_coins(self):

    def gen_rums(self):

class Map:

    def __init__(self):
        self.tiles = self.gen_tiles()

    def gen_tiles(self):
        tiles = []
        sprite_ids = []
        sprite_num = [1, 1, 5, 4, 2, 3, 2, 1, 2, 4, 1, 1, 2, 2, 4, 6, 1, 1, 1, 1, 5, 5, 3, 2, 1, 1, 4, 40, 2, 1, 1, 4,
                      1, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 3]

        for idx in range(len(sprite_num)):
            for _ in range(sprite_num[idx]):
                sprite_ids.append(idx + 1)

        for idx in range(144):
            tiles.append(Tile(idx, self.get_sprite_id(sprite_ids), random.choice((0, 90, 180, 270))))
        return tiles

    def get_sprite_id(self, sprite_ids):
        num = random.randrange(len(sprite_ids))
        sprite_id = sprite_ids[num]
        del (sprite_ids[num])
        return sprite_id

    def print_info(self):
        for idx, tile in enumerate(self.tiles):
            txt = str(tile.id) + "/" + str(tile.sprite_id) + "/" + str(tile.rot)
            if (idx + 1) % 12 == 0:
                print(txt)
            else:
                print(txt, " ", end='')


class Tile:

    def __init__(self, id, sprite_id, rot):
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
        self.xy_px = [x_px, y_px]


class Rum:

    def __init__(self, id, x_px=10, y_px=10):
        self.id = id
        self.xy_px = [x_px, y_px]


def main():
    game = Game()
    map.print_info()


main()
