part1, part2 = 0, 0

with open('temp.txt', 'r') as file:
    # Read each line, strip newline characters, and convert into a list of characters
    puzzle = [list(line.strip()) for line in file]

# Directions: (row_offset, col_offset)
directions = [
    (0, 1),  # Right
    (0, -1), # Left
    (1, 0),  # Down
    (-1, 0), # Up
    (1, 1),  # Down-right diagonal
    (-1, -1),# Up-left diagonal
    (1, -1), # Down-left diagonal
    (-1, 1)  # Up-right diagonal
]

rows, cols = len(puzzle), len(puzzle[0])

# Loop through the puzzle
# for row in range(rows):
#     for col in range(cols):
#         for dr, dc in directions: # Check all directions
#             match = True
#             for k in range(word_length):
#                 nr, nc = row + k * dr, col + k * dc
#                 if not (0 <= nr < rows and 0 <= nc < cols) or puzzle[nr][nc] != target_word[k]:
#                         match = False
#                         break
#             if match:
#                 part1 += 1

# Part 1 Optimized
# Count occurrences of 'X' and 'S'
count_X = sum(row.count('X') for row in puzzle)
count_S = sum(row.count('S') for row in puzzle)

# Choose the less frequent character
start_chars = 'X' if count_X < count_S else 'S'
target_word = 'XMAS' if start_chars == 'X' else 'SAMX'
word_length = len(target_word)

# Function to check for the word 'XMAS' starting from a given position
def check_word(puzzle, x, y, word, directions):
    for dr, dc in directions:
        match = True
        for k in range(len(word)):
            nr, nc = x + k * dr, y + k * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or puzzle[nr][nc] != word[k]:
                match = False
                break
        if match:
            return True
    return False

# Loop through the puzzle, focusing on the less frequent starting letter
for x in range(rows):
    for y in range(cols):
        if puzzle[x][y] in start_chars:  # Start only at 'X' or 'S' as decided
            if check_word(puzzle, x, y, target_word, directions):
                part1 += 1

# Part 2: Find X-shaped MAS patterns
valid_letters = ['M', 'A', 'S']
for row in puzzle:
     for letter in row:
         if letter not in valid_letters:
            puzzle[puzzle.index(row)][row.index(letter)] = '.'

# Function to check if a valid X-MAS exists centered on (x, y)
def check_is_valid_xmas(puzzle, x, y):
    # Sanity check: 'A' should not be at the borders
    if x <= 0 or x >= rows - 1 or y <= 0 or y >= cols - 1:
        return False
    
    # Define possible X-MAS orientations
    diagonals = [
        [(x - 1, y - 1), (x, y), (x + 1, y + 1)],  # Top-left to Bottom-right
        [(x - 1, y + 1), (x, y), (x + 1, y - 1)],  # Top-right to Bottom-left
    ]

    # Check each diagonal pair
    for diag1, diag2 in zip(diagonals, diagonals[::-1]):
        if (
            ''.join([puzzle[r][c] for r, c in diag1]) in ['MAS', 'SAM']
            and ''.join([puzzle[r][c] for r, c in diag2]) in ['MAS', 'SAM']
        ):
            return True

    return False

for x in range(rows):
    for y in range(cols):
        if puzzle[x][y] == 'A':  # Check only when encountering 'A'
            if check_is_valid_xmas(puzzle, x, y):
                part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")