from collections import Counter

# Initialize variables
part1, part2 = 0, 0
left, right = [], []

# Read input data from the file
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()

        # Split into left and right numbers
        left_num, right_num = map(int, line.split('   '))

        # Append to respective lists
        left.append(left_num)
        right.append(right_num)

# Count the occurrences of each number in the left and right lists
left_counts = Counter(left)
right_counts = Counter(right)

# Sort each list
sorted_left = sorted(left)
sorted_right = sorted(right)

for l, r in zip(sorted_left, sorted_right):
    diff = abs(l - r)
    part1 += diff

for l in left:
    sim_score = l * right_counts.get(l, 0)
    part2 += sim_score

# Output the results
print(f"Part1: {part1}")
print(f"Part2: {part2}")
