import math


def two_crystal_balls(breaks: list[bool]) -> int:

    floors = len(breaks)
    jump_size = math.floor(math.sqrt(floors))

    current_floor = jump_size
    for floor in range(jump_size, floors, jump_size) :
        current_floor = floor
        if breaks[current_floor]:
            break

    start_floor = current_floor - jump_size + 1
    end_floor = current_floor
    for floor in range(start_floor, end_floor):
        current_floor = floor
        if breaks[current_floor]:
            return current_floor

    return -1
