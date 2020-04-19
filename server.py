import random

ALIVE = 10
SLEEP = 11
DEAD = 12


class Game:

    def __init__(self):
        self.map = Map()
        self.pirates = self.gen_pirates()
        self.ships = self.gen_ships()
        self.coins = self.gen_coins()
        self.rums = self.gen_rums()

    @staticmethod
    def gen_ships():
        ships = [Ship(0, 45), Ship(1, 45), Ship(2, 45), Ship(3, 45)]
        return ships

    @staticmethod
    def gen_coins():
        coins = [Coin(36, 47)]
        for idx in range(36):
            coins.append(Coin(idx, 46))
        return coins

    @staticmethod
    def gen_rums():
        rums = []
        for idx in range(9):
            rums.append(Rum(idx, 52))
        return rums

    @staticmethod
    def gen_pirates():
        pirates = []
        for idx in range(3):
            pirates.append(Pirate(idx, 55, ALIVE))
            pirates.append(Pirate(idx, 56, ALIVE))
            pirates.append(Pirate(idx, 57, ALIVE))
            pirates.append(Pirate(idx, 58, ALIVE))
        pirates.append(Pirate(idx, 49, ALIVE))
        pirates.append(Pirate(idx, 50, ALIVE))
        pirates.append(Pirate(idx, 51, ALIVE))
        return pirates

    def print_info(self):
        for idx, tile in enumerate(self.map.tiles):
            txt = str(tile.id) + "/" + str(tile.sprite_id) + "/" + str(tile.rot)
            if (idx + 1) % 12 == 0:
                print(txt)
            else:
                print(txt, " ", end='')


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
            tiles.append(Tile(idx, self.get_sprite_id(sprite_ids), random.choice((0, 90, 180, 270)), False))
        return tiles

    @staticmethod
    def get_sprite_id(sprite_ids):
        num = random.randrange(len(sprite_ids))
        sprite_id = sprite_ids[num]
        del (sprite_ids[num])
        return sprite_id


class Tile:

    def __init__(self, id, sprite_id, rot, fliped):
        self.id = id
        self.sprite_id = sprite_id
        self.rot = rot
        self.fliped = fliped


class MovingObj:

    def __init__(self, id, sprite_id, x_px, y_px):
        self.id = id
        self.sprite_id = sprite_id
        self.xy_px = [x_px, y_px]


class Pirate(MovingObj):

    def __init__(self, id, sprite_id, state_id, x_px=0, y_px=0):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)
        self.state_id = state_id


class Ship(MovingObj):

    def __init__(self, id, sprite_id, x_px=0, y_px=0):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Coin(MovingObj):

    def __init__(self, id, sprite_id, x_px=0, y_px=0):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Rum:

    def __init__(self, id, sprite_id, x_px=0, y_px=0):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


def main():
    game = Game()
    game.print_info()


main()
