#!/usr/bin/env python3

import cmd_args
import gfx_stack as gfx
from file_io import MapData, TileType


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

    while not gfx.stop_prog:
        gfx.event_loop()

    gfx.quit_prog()
