dataset = [
    {"Apple", "Banana", "Cereal", "Diapers"},
    {"Banana", "Cereal", "Diapers", "Eggs"},
    {"Apple", "Banana", "Cereal", "Eggs"},
    {"Banana", "Cereal", "Diapers"},
    {"Apple", "Banana", "Cereal"}
]
min_support = 3

# Step 1: Initialization
# Initialize the hash table (with 4 buckets)
bucket_count = [0, 0, 0, 0]

# Step 2: Counting Single Items
for transaction in dataset:
    for item in transaction:
        # Hash the item to a bucket using a hash function
        bucket = hash(item) % 4
        bucket_count[bucket] += 1
# Print the bucket counts
print("Bucket Counts:")
for i, count in enumerate(bucket_count):
    print(f"Bucket {i}: {count}")

# Step 3: Generate Candidate 2-Itemsets
candidates = []
frequent_items = set()

for item in bucket_count:
    if item >= min_support:
        frequent_items.add(item)
print("frequent_items", frequent_items)

for item1 in frequent_items:
    for item2 in frequent_items:
        if item1 != item2:
            # Check if both items hash to buckets with counts above the threshold
            bucket1 = hash(item1) % 4
            bucket2 = hash(item2) % 4
            if bucket_count[bucket1] >= min_support and bucket_count[bucket2] >= min_support:
                candidates.append((item1, item2))

# Print candidate 2-itemsets
print("Candidate 2-Itemsets:")
for candidate in candidates:
    print(candidate)

# Step 4: Counting 2-Itemsets
# Initialize the counter for candidate 2-itemsets
candidate_counts = {}

for transaction in dataset:
    for candidate in candidates:
        item1, item2 = candidate
        if item1 in transaction and item2 in transaction:
            # Both items are in the transaction, hash them to buckets
            bucket1 = hash(item1) % 4
            bucket2 = hash(item2) % 4
            # Update the candidate 2-itemset counter
            if (bucket1, bucket2) in candidate_counts:
                candidate_counts[(bucket1, bucket2)] += 1
            else:
                candidate_counts[(bucket1, bucket2)] = 1

# Print the counts of candidate 2-itemsets
print("Candidate 2-Itemset Counts:")
for candidate, count in candidate_counts.items():
    print(f"{candidate}: {count}")

# Step 5: Prune Candidate 2-Itemsets
frequent_2_itemsets = []

for candidate, count in candidate_counts.items():
    if count >= min_support:
        frequent_2_itemsets.append(candidate)

# Print the frequent 2-itemsets
print("Frequent 2-Itemsets:")
for itemset in frequent_2_itemsets:
    print("Itemset", itemset)
