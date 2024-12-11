#!/usr/bin/env python3

'''
Reading in python map data from txt file
'''

from typing import List
from enum import Enum


class TileType(Enum):
    INVALID = -1
    PATH = 0
    WALL = 1
    START = 2
    FINISH = 3

    def __str__(self):
        tile_type_map = {
                TileType.INVALID: "Invalid",
                TileType.PATH: "Path",
                TileType.WALL: "Wall",
                TileType.START: "Start",
                TileType.FINISH: "Finish",
        }
        return f"{tile_type_map[self]}"


def tiles_type_one(data: str) -> TileType:
    global maze_numbers
    if data.isdigit():
        return TileType.PATH
    match data:
        case 'W':
            return TileType.WALL
        case '.':
            return TileType.PATH
        case 'S':
            return TileType.START
        case 'Z':
            return TileType.FINISH
        case _:
            return TileType.INVALID


def tiles_type_two(data: str) -> TileType:
    global maze_numbers
    if data.isdigit():
        return TileType.PATH
    match data:
        case 'X':
            return TileType.WALL
        case 'W':
            return TileType.PATH
        case 'S':
            return TileType.START
        case 'Z':
            return TileType.FINISH
        case _:
            return TileType.INVALID


def tile_row_from_str(data: str, maze_type: int) -> List[TileType]:
    row = []
    if maze_type == 1:
        for tile in data:
            t = tiles_type_one(tile)
            if t == TileType.INVALID:
                raise Exception("Invalid TileType")
            row.append(t)
    elif maze_type == 2:
        for tile in data:
            t = tiles_type_two(tile)
            if t == TileType.INVALID:
                raise Exception("Invalid TileType")
            row.append(t)
    else:
        raise Exception("Invalid File Type")
    return row


class MapData:
    data = []
    _maze_type: int = 0
    _rows: int = 0
    _cols: int = 0
    _start: (int, int) = (0, 0)
    _end: (int, int) = (0, 0)

    def __init__(self, path: str, maze_type: int):
        self._maze_type = maze_type
        if not self.__from_file__(path):
            raise Exception("Could not convert Map Data, returning...")
        for y, row in enumerate(self.data):
            for x, tile in enumerate(row):
                if tile == TileType.START:
                    self._start = (x, y)
                if tile == TileType.FINISH:
                    self._end = (x, y)

    def __str__(self):
        s = ""
        for row in self.data:
            s += "{"
            for tile in row:
                s += f" {tile}"
            s += "}"
        return s

    def __from_file__(self, path: str) -> bool:
        try:
            file = open(path, "r")
        except OSError as e:
            print(f"Loading {path} - {e}")
            return False
        for line in file:
            try:
                row = tile_row_from_str(line.strip('\n'), self._maze_type)
                self.data.append(row)
                self._rows += 1
            except Exception as e:
                print(f"Error reading tiles from file: {e}")
                file.close()
                return False
        file.close()
        # All rows have the same length
        self._cols = len(self.data[0])
        return True

    def get_rows(self) -> int:
        return self._rows

    def get_cols(self) -> int:
        return self._cols

    def get_start(self) -> (int, int):
        return self._start

    def get_end(self) -> (int, int):
        return self._end

    def get_tile_at(self, x_y: (int, int)) -> TileType:
        x = x_y[0]
        y = x_y[1]
        if x >= self._cols or y >= self._rows:
            raise Exception("Out of bounds")
        return self.data[y][x]


if __name__ == "__main__":
    md1 = MapData("./lab_1.txt", 1)
    print(md1)
    print(md1.get_cols(), md1.get_rows())
    md2 = MapData("./lab_2.txt", 1)
    print(md2)
    print(md2.get_cols(), md2.get_rows())
    md3 = MapData("./lab_3.txt", 2)
    print(md3)
    print(md3.get_cols(), md3.get_rows())
