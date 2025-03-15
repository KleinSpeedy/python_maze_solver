#!/usr/bin/env python3

'''
Implements different pathfinding algorithms for the maze solver
'''

import time
from file_io import MapData, TileType
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Trivial:
    def __init__(self, md: MapData):
        self._md = md
        self._cols = md.get_cols()
        self._rows = md.get_rows()
        self._pos = md.get_start()
        self._view = Direction.SOUTH
        self._visited = [(int, int)]

    def move(self) -> (int, int):
        pos = (0, 0)
        match self._view:
            case Direction.NORTH:
                # right, up, left, down
                order = [1, 0, 3, 2]
                view, pos = self._check_positions(order,
                                                  self._get_next_positions())
            case Direction.SOUTH:
                # left, down, right, up
                order = [3, 2, 1, 0]
                view, pos = self._check_positions(order,
                                                  self._get_next_positions())
            case Direction.WEST:
                # up, left, down, right
                order = [0, 3, 2, 1]
                view, pos = self._check_positions(order,
                                                  self._get_next_positions())
            case Direction.EAST:
                # down, right, up, left
                order = [2, 1, 0, 3]
                view, pos = self._check_positions(order,
                                                  self._get_next_positions())
        self._pos = pos
        self._view = view
        return self._pos

    def _get_next_positions(self) -> [(int, int)]:
        current = self._pos  # tuple of (x, y) coordinates
        return [
                (current[0], current[1]-1),  # up (0)
                (current[0]+1, current[1]),  # right (1)
                (current[0], current[1]+1),  # down (2)
                (current[0]-1, current[1])   # left (3)
        ]

    def _check_positions(self, order, pos) -> (Direction, (int, int)):
        # sort position tuples according to order of view
        newSeq = sorted(zip(order, pos))
        for i, pos in newSeq:
            if self._md.get_tile_at(pos) != TileType.WALL:
                return (Direction(order[i]), pos)
        raise Exception('Position is surrounded by walls')


class PathFinding:
    ''' Base class for pathfinding algorithm used to compute path '''

    def __init__(self, name: str, md: MapData):
        self._name = name
        self._md = md
        # TODO: Use generic way to support multiple pathfinding algs
        self._impl = Trivial(md)

    def __str__(self):
        return self._name

    def solve(self) -> []:
        visited = []  # all visited tiles
        solved = False
        while not solved:
            next = self._impl.move()
            visited.append(next)
            if self._md.get_tile_at(next) == TileType.FINISH:
                solved = True
        return visited


if __name__ == "__main__":
    maze = MapData("lab_1.txt", 1)
    alg = PathFinding("trivial", maze)
    tiles = alg.solve()
