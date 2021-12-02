# Advent of Code 2021 Day 2 Solution
# Author: Sreekaran

import time

start = time.time()
with open((__file__.rstrip("solution.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()

print("Part One: ")

x, y = 0, 0
for line in input:
    num = int(line.split()[1])
    if line.startswith("forward"):
        x += num
    elif line.startswith("up"):
        y -= num
    elif line.startswith("down"):
        y += num

print(x * y)

print("Part Two: ")

aim, x, y = 0, 0, 0
for line in input:
    num = int(line.split()[1])
    if line.startswith("forward"):
        x += num
        y += num * aim
    elif line.startswith("up"):
        aim -= num
    elif line.startswith("down"):
        aim += num

print(x * y)

print("Time Taken: ", time.time() - start)
