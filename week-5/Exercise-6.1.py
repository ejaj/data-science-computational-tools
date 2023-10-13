num_items = 100
num_baskets = 100
basket_counts = [0] * (num_items + 1)
for item in range(1, num_items + 1):
    for basket in range(1, num_baskets + 1):
        if basket % item == 0:
            basket_counts[item] += 1
support_threshold = 5

# Find frequent items
frequent_items = [item for item in range(1, num_items + 1) if basket_counts[item] >= support_threshold]
print("Frequent items with a support threshold of 5:", frequent_items)


# Initialize a list to count how many baskets each pair of items is in
pair_counts = [[0] * (num_items + 1) for _ in range(num_items + 1)]

# Iterate through each pair of items and baskets to update the counts
for item1 in range(1, num_items + 1):
    for item2 in range(1, num_items + 1):
        if item1 != item2:
            for basket in range(1, num_baskets + 1):
                if basket % item1 == 0 and basket % item2 == 0:
                    pair_counts[item1][item2] += 1

# Define the support threshold
support_threshold = 5

# Find frequent pairs of items
frequent_pairs = [(item1, item2) for item1 in range(1, num_items + 1) for item2 in range(1, num_items + 1) if item1 != item2 and pair_counts[item1][item2] >= support_threshold]

print("Frequent pairs of items with a support threshold of 5:")
for item1, item2 in frequent_pairs:
    print(f"({item1}, {item2})")
largest_basket = basket_counts.index(max(basket_counts))

print(f"The largest basket is basket {largest_basket} with {max(basket_counts)} items.")