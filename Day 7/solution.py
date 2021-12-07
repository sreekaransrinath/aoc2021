# Advent of Code 2021 Day 7 Solution
# Author: Sreekaran

from math import dist
import time

start = time.time()
with open((__file__.rstrip("solution.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()

nums = [int(_) for _ in input[0].split(",")]

print("Part One: ")

nums.sort()
median = nums[int(len(nums) / 2 - 1)]
distance = 0
for num in nums:
    distance += abs(num - median)
print(distance)

print("Part Two: ")

# mean = round(sum(nums)/len(nums))
distances = []
for item in nums:
    mean = item
    distance = 0
    for num in nums:
        distance += sum(range(1, (abs(num - mean) + 1)))
    distances.append(distance)
print(min(distances))

print("Time Taken: ", time.time() - start)
