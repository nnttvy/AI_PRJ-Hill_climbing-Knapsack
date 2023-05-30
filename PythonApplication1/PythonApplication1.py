import random
#generate items for the Knapsack
def generate_items(n_items, max_item_weight):
    items = []
    for i in range(n_items):
        weight = random.randint(1, max_item_weight)
        value = random.randint(1, 10)
        items.append((value, weight))
    return items
items = generate_items(5, 50)

def knapsack(items, capability):
    while True: 
      # Generate a random initial solution
      solution = [random.randint(0, 1) for _ in range(len(items))]
      solution1 = solution.copy()
      # Calculate the value and weight of the initial solution
      solution_value, solution_weight = 0, 0
      for i, item in enumerate(items):
          if solution[i] == 1:
              solution_value += item[0]
              solution_weight += item[1]
      if solution_weight <= capability:
        break

    # Generate all neighbors of the current solution
    neighbors = []
    for i in range(len(items)):
        neighbor = solution.copy()
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)

    # Iterate until we can no longer find a better solution
    while True:
        # Evaluate the neighbors and find the best one
        best_neighbor = None
        best_value = solution_value
        for neighbor in neighbors:
            neighbor_value, neighbor_weight = 0, 0
            for i, item in enumerate(items):
                if neighbor[i] == 1:
                    neighbor_value += item[0]
                    neighbor_weight += item[1]
            if neighbor_weight <= capability and neighbor_value > best_value:
                best_neighbor = neighbor
                best_value = neighbor_value
                solution_weight = neighbor_weight

        # If we found a better neighbor, update the solution
        if best_neighbor is not None:
            solution = best_neighbor
            solution_value = best_value
        else:
            break

    # Return the best solution we found
    return  solution, solution_value, solution_weight, solution1

capability = 100

print (f"Input: {len(items)} items, capability: {capability}\nItems:",items)
print("*******************************************************************************")
for i in range (3):
    solution, solution_value, solution_weight, solution1 = knapsack(items, capability)
    print(f"Sample {i}")
    print(f"Output\nValue: {solution_value}")
    print(f"Solution: {solution}")
    print(f"Weight: {solution_weight}")
    print(f"Intial solution: {solution1}")
    print("*******************************************************************************")