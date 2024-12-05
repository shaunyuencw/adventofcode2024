from collections import defaultdict, deque

# Helper function to perform topological sort
def topological_sort(update, rules):
    # Create a graph and in-degree tracker for the update pages
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph and count in-degrees based on rules
    for x in update:
        for y in rules.get(x, []):
            if y in update:
                graph[x].append(y)
                in_degree[y] += 1

    # Start with nodes that have no incoming edges
    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the sorted list contains all pages, it's valid; otherwise, there's a cycle
    return sorted_pages if len(sorted_pages) == len(update) else []

part1, part2 = 0, 0
with open('input.txt', 'r') as file:
    data = file.read()

# Split the input into rules and updates
rules_section, updates_section = data.split("\n\n")

# Parse rules into a dictionary with integers
rules = defaultdict(list)
for rule in rules_section.split("\n"):
    rule_name, rule_value = map(int, rule.split("|"))  # Convert to integers
    rules[rule_name].append(rule_value)

incorrect_rules = []

# print(f"Rules Section: {rules_section}")
print(f"Updates: ")
for update in updates_section.split("\n"):
    update_items = list(map(int, update.split(",")))  # Convert to integers
    num_items = len(update_items)

    for i in range (0, num_items - 1):
        valid = True
        update_key = update_items[i]
        update_check = update_items[i + 1:]

        for item in update_check:
            if item not in rules: # Skip if no rule for this item
                continue
            if update_key in rules[item]: # Rule violated
                valid = False
                break

        if not valid:
            break

    if valid:
        # Add center item to part1
        center_index = num_items // 2
        part1 += int(update_items[center_index])
    else:
        # print(f"Incorrect Update: {update}")
        incorrect_rules.append(update)

# Fix the incorrect rules
for update in incorrect_rules:
    update_items = update.split(",")
    update_items = list(map(int, update_items)) # Convert to integer to sort
    corrected_order = topological_sort(update_items, rules)
    # print(corrected_order)

    if corrected_order:
        center_index = len(corrected_order) // 2
        part2 += corrected_order[center_index]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")