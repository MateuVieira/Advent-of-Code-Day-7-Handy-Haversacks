import re
import sys
from os import path, getcwd
from time import perf_counter
from functools import reduce

def read_file(filename):
  try:
    with open(filename) as f:
        content = f.readlines()

    bag_rules = dict()
    for line in content:
        outer_bag, inner_bags = line.split(" bags contain")
        items = re.findall(r'([0-9]+) ([a-z ]+) bag[s]?', inner_bags.strip())
        bag_rules[outer_bag] = dict((key, number) for (number, key) in items)

  except:
    print('Error to read file')
    sys.exit(1)

  return bag_rules

def check_rules_for_bag(data, target):
  parents = set([
    parent_name
    for (parent_name, parent_contents) in data.items()
    if target in parent_contents
  ])

  return reduce(
    lambda a, b: a.union(
      check_rules_for_bag(data, b)
    ), 
    parents, 
    parents
  )

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    target = 'shiny gold'

    result = check_rules_for_bag(data=input_data, target=target)

    print(f'Result: {len(result)}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)