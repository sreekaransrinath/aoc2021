# Any time a revised solution pops up, the previous solution is archived in this file to keep track of the author's thought process.

import time
from collections import Counter

start = time.time()
with open((__file__.rstrip("solution.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()

print("Part One: ")

transpose = ["".join(item).strip() for item in zip(*input)]
gamma = "".join([max(set(_), key=_.count) for _ in transpose])
epsilon = "".join(["1" if char == "0" else "0" for char in gamma])
gamma_dec, epsilon_dec = 0, 0
for i in range(len(gamma)):
    gamma_dec += int(gamma[i]) * 2 ** (len(gamma) - i - 1)
    epsilon_dec += int(epsilon[i]) * 2 ** (len(epsilon) - i - 1)
print(gamma_dec * epsilon_dec)

print("Part Two: ")

new_lines = input
new_transpose = transpose
oxygen_rating = ""
co2_rating = ""
oxygen_rating_dec, co2_rating_dec = 0, 0
while len(new_lines) > 1:
    modes = Counter(new_transpose[0]).most_common()
    print(modes[0][1], modes[1][1])
    if modes[0][1] == modes[1][1]:
        most_common = "1"
    else:
        most_common = modes[0][0]
    oxygen_rating += most_common
    new_lines = [line[1:] for line in new_lines if line.startswith(most_common)]
    new_transpose = ["".join(item).strip() for item in zip(*new_lines)]
    print(most_common)
if not new_lines[0] == oxygen_rating:
    oxygen_rating += new_lines[0]
oxygen_rating = oxygen_rating.strip()
print(oxygen_rating)

new_lines = input
new_transpose = transpose

while len(new_lines) > 1:
    modes = Counter(new_transpose[0]).most_common()
    print(modes[-1][1], modes[-2][1])
    if modes[-1][1] == modes[-2][1]:
        least_common = "0"
    else:
        least_common = modes[-1][0]
    co2_rating += least_common
    new_lines = [line[1:] for line in new_lines if line.startswith(least_common)]
    new_transpose = ["".join(item).strip() for item in zip(*new_lines)]
    print(least_common)
if not new_lines[0] == co2_rating:
    co2_rating += new_lines[0]
co2_rating = co2_rating.strip()
print(co2_rating)

for i in range(len(oxygen_rating)):
    oxygen_rating_dec += int(oxygen_rating[i]) * 2 ** (len(oxygen_rating) - i - 1)
    co2_rating_dec += int(co2_rating[i]) * 2 ** (len(co2_rating) - i - 1)

print(oxygen_rating_dec * co2_rating_dec)
print("Time Taken: ", time.time() - start)
