import math
from random import randint

from kata_machine_python.two_crystal_balls import two_crystal_balls

def test_two_crystal_balls():
    idx = math.floor(randint(0, 10000))
    data = [False for _ in range(0, 10000)]

    for i in range (idx, 10000):
        data[i] = True

    assert two_crystal_balls(data) == idx
    assert two_crystal_balls([False for _ in range(0,821)]) == -1

