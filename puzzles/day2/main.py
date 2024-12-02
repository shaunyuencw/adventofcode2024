part1, part2 = 0, 0

reports = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()

        # Each line contains 5 numbers
        report = list(map(int, line.split(' ')))
        reports.append(report)

# Function to check if a report is valid
def is_valid(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(1, len(report)):
            diff = abs(report[i] - report[i - 1])
            if diff < 1 or diff > 3:
                return False
        return True
    return False

for report in reports:
    # Part1: Check if the report is valid as is
    if is_valid(report):
        print(report)
        part1 += 1
        part2 += 1
    
    else:
        # Part2: Check if removing one element makes it valid
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_valid(modified_report):
                part2 += 1
                break

print(f"Part1: {part1}")
print(f"Part2: {part2}")