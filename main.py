#!/usr/bin/env python3

import time
import cmd_args
import gfx_stack as gfx
from file_io import MapData, TileType
from pathfinding import PathFinding


def draw_maze(maze: MapData):
    for i, row in enumerate(maze.data):
        y = i
        for j, tile in enumerate(row):
            x = j
            match tile:
                case TileType.START:
                    gfx.set_pixel((x, y), "Elf Green")
                case TileType.FINISH:
                    gfx.set_pixel((x, y), "Tahiti Gold")
                case TileType.WALL:
                    # gfx.set_pixel((x, y), "Light Steel Blue")
                    gfx.set_pixel((x, y), "Black")
                case TileType.PATH:
                    gfx.set_pixel((x, y), "Pancho")


def assign_colors(path) -> []:
    colorA = "Venice Blue"
    colorB = "Cornflower"
    colorMapping = {}
    result = []
    for pos in path:
        if pos not in colorMapping:
            colorMapping[pos] = colorA
        else:
            colorMapping[pos] = colorB if colorMapping[pos] == colorA else colorA
        result.append((pos, colorMapping[pos]))
    return result


def draw_path_tile(pos: (int, int), color: str):
    gfx.set_pixel((pos), color)


if __name__ == "__main__":
    args = cmd_args.parse()

    try:
        maze = MapData(args.file, args.mtype)
    except Exception as e:
        print(e)
        exit(1)

    width = maze.get_rows()
    height = maze.get_cols()

    gfx.init_once((height, width), "Praktikum 3")
    draw_maze(maze)

    alg = PathFinding('trivial', maze)
    visited = alg.solve()
    path = assign_colors(visited)

    while not gfx.stop_prog:
        # check for last element
        if len(path) == 1:
            gfx.stop_prog = True
        pos, color = path.pop(0)
        gfx.set_pixel(pos, color)
        time.sleep(args.delay)
        gfx.event_loop()

    gfx.quit_prog()
