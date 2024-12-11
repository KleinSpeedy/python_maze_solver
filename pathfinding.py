#!/usr/bin/env python3

'''
Implements different pathfinding algorithms for the maze solver
'''

from file_io import MapData, TileType
from enum import Enum


class ViewDirection(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3,


class Avatar:
    _visited = [(int, int)]
    _view: ViewDirection = ViewDirection.RIGHT

    def __init__(self, cols, rows, start: (int, int)):
        self._cols = cols
        self._rows = rows
        self._pos = start
        print("Avatar")

    def move(self, pos: (int, int)) -> (int, int):
        next = (0, 0)
        match self._view:
            case ViewDirection.UP:
                next = self._move_up(pos)
            case ViewDirection.DOWN:
                next = self._move_down(pos)
            case ViewDirection.LEFT:
                next = self._move_left(pos)
            case ViewDirection.RIGHT:
                next = self._move_right(pos)
        return next

    def _move_up(self, pos: (int, int)) -> (int, int):
        if pos[0] >= self._rows:
            raise Exception("Up move out of bounds")
        return (pos[0], pos[1] + 1)

    def _move_down(self, pos: (int, int)) -> (int, int):
        if pos[0] < 0:
            raise Exception("Down move out of bounds")
        return (pos[0], pos[1] - 1)

    def _move_left(self, pos: (int, int)) -> (int, int):
        if pos[1] < 0:
            raise Exception("Left move out of bounds")
        return (pos[0] - 1, pos[1])

    def _move_right(self, pos: (int, int)) -> (int, int):
        if pos[1] >= self._cols:
            raise Exception("Down move out of bounds")
        return (pos[0] + 1, pos[1])


class PathFinding:
    _name: str = ""
    _visited = []
    _maze: MapData = None
    _avatar: Avatar = None
    _pos: (int, int) = 0
    attempts: int = 0

    def __init__(self, name: str, md: MapData):
        self._name = name
        self._maze = md
        self._pos = md.get_start()  # Initial position
        self._avatar = Avatar(md.get_cols(), md.get_rows(), md.get_start())

    def __str__(self):
        return self._name

    def next_move(self) -> (bool, (int, int)):
        next_pos = self._avatar.move(self._pos)
        if self._maze.get_tile_at(next_pos) == TileType.FINISH:
            return (True, next_pos)
        else:
            return (False, next_pos)


if __name__ == "__main__":
    maze = MapData("lab_1.txt", 1)
    alg = PathFinding("trivial", maze)

    running = True
    while running:
        (res, pos) = alg.next_move()
        print(res, pos)
        running = not res
