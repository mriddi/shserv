import random
import asyncio
import websockets
import json
from datetime import datetime as dt


async def notify_state():
    if USERS:
        message = json.dumps(GAME, cls=RumEncoder)
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    print(f"{dt.now()} {websocket.remote_address[0]} was registered")
    await notify_state()


async def unregister(websocket):
    USERS.remove(websocket)
    print(f"{dt.now()} {websocket.remote_address[0]} was unregistered")


async def handler(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            GAME.update_game_state(message)
            print(f"{dt.now()} {websocket.remote_address[0]} send message: {message}")
            await notify_state()
    finally:
        await unregister(websocket)


class Game:

    def __init__(self):
        self.id = random.randrange(100000)
        self.map = Map()
        self.pirates = self.gen_pirates()
        self.ships = self.gen_ships()
        self.coins = self.gen_coins()
        self.rums = self.gen_rums()
        self.cannonballs = self.gen_cannonballs()
        self.boat = Boat(0, 53)
        self.cart = Cart(0, 54)

    def update_game_state(self, message):
        data = json.loads(message)
        try:
            if "flip_tile" in data:
                next((x for x in self.map.tiles if x.id == data["flip_tile"])).flip()
            elif "select_tile" in data:
                next((x for x in self.map.tiles if x.id == data["select_tile"])).select()
            elif "rotate_pirate" in data:
                next((x for x in self.pirates if x.id == data["rotate_pirate"])).rotate()
            elif "object_type" in data:
                objs = {"pirate": self.pirates, "coin": self.coins, "ship": self.ships, "rum": self.rums, "cannonball": self.cannonballs, "boat": self.boat, "cart": self.cart}
                next((x for x in objs[data["object_type"]] if x.id == data["object_id"])).move_to(
                    data["move_to_x"], data["move_to_y"])
            elif "cmd" in data:
                self.__init__()
        finally:
            pass

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
    def gen_cannonballs():
        cannonballs = []
        for idx in range(2):
            cannonballs.append(Cannonball(idx, 48))
        return cannonballs

    @staticmethod
    def gen_pirates():
        pirates = [Pirate(0, 55, False), Pirate(1, 55, False), Pirate(2, 55, False), Pirate(3, 56, False),
                   Pirate(4, 56, False), Pirate(5, 56, False), Pirate(6, 57, False), Pirate(7, 57, False),
                   Pirate(8, 57, False), Pirate(9, 58, False), Pirate(10, 58, False), Pirate(11, 58, False),
                   Pirate(12, 49, False), Pirate(13, 50, False), Pirate(14, 51, False)]
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
            tiles.append(Tile(idx, self.get_sprite_id(sprite_ids), random.choice((0, 90, 180, 270)), False, False))
        return tiles

    @staticmethod
    def get_sprite_id(sprite_ids):
        num = random.randrange(len(sprite_ids))
        sprite_id = sprite_ids[num]
        del (sprite_ids[num])
        return sprite_id


class Tile:

    def __init__(self, id, sprite_id, rot, flipped, selected):
        self.id = id
        self.sprite_id = sprite_id
        self.rot = rot
        self.flipped = flipped
        self.selected = selected

    def flip(self):
        self.flipped = not self.flipped

    def select(self):
        self.selected = not self.selected


class MovingObj:

    def __init__(self, id, sprite_id, x_px, y_px):
        self.id = id
        self.sprite_id = sprite_id
        self.xy_px = [x_px, y_px]

    def move_to(self, x_px, y_px):
        self.xy_px = [x_px, y_px]


class Pirate(MovingObj):

    def __init__(self, id, sprite_id, rotated, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)
        self.rotated = rotated

    def rotate(self):
        self.rotated = not self.rotated


class Ship(MovingObj):

    def __init__(self, id, sprite_id, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Coin(MovingObj):

    def __init__(self, id, sprite_id, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Rum(MovingObj):

    def __init__(self, id, sprite_id, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Cannonball(MovingObj):

    def __init__(self, id, sprite_id, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Boat(MovingObj):

    def __init__(self, id, sprite_id, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class Cart(MovingObj):

    def __init__(self, id, sprite_id, x_px=-1, y_px=-1):
        MovingObj.__init__(self, id, sprite_id, x_px, y_px)


class RumEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


if __name__ == '__main__':
    GAME = Game()
    USERS = set()
    start_server = websockets.serve(handler, "", 6789)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
