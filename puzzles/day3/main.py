import re

part1, part2 = 0, 0
corrupted_memory = ""
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        corrupted_memory += f"{line}\n"

# Regax for instructions
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"     # Valid mul instructions
do_pattern = r"do\(\)"                          # do() instruction
dont_pattern = r"don't\(\)"                     # don't() instruction

is_enabled = True # Start enabled

# Process the corrupted memory
for match in re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", corrupted_memory):
    instruction = match.group()
    
    if re.match(mul_pattern, instruction):
        x, y = map(int, re.findall(r"\d{1,3}", instruction))

        part1 += x * y
        if is_enabled:
            part2 += x * y 

    elif re.match(do_pattern, instruction):
        is_enabled = True
    elif re.match(dont_pattern, instruction):
        is_enabled = False

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")