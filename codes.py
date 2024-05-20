import csv
import json
import itertools

# Script to create a list of possible combinations of four letters, where the last letter is always a U.

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create all possible combinations of four letters, where the last one is a 'U'
combinations = list(itertools.product(letters, repeat=3))
codes = [''.join(combination) + 'U' for combination in combinations]

# output as CSV
with open('codes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Code'])
    writer.writerows([[code] for code in codes])

# output as JSON
with open('codes.json', 'w') as jsonfile:
    json.dump({'Codes': codes}, jsonfile)

print("CSV and JSON files have been successfully created.")

# run python3 codes.py  