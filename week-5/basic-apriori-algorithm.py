# Step 1: Generate Frequent 1-Itemsets (Single Items)
# Initialize the dataset
dataset = [
    {"Apple", "Banana", "Cereal", "Diapers"},
    {"Banana", "Cereal", "Diapers", "Eggs"},
    {"Apple", "Banana", "Cereal", "Eggs"},
    {"Banana", "Cereal", "Diapers"},
    {"Apple", "Banana", "Cereal"}
]

#####using defaultdict#####
# item_counts = defaultdict(int)
# for transaction in transactions:
#     for item in transaction:
#         item_counts[item] += 1
# # Filter frequent 1-itemsets
# frequent_1_itemsets = {item: count for item, count in item_counts.items() if count >= min_support}
# print(frequent_1_itemsets)

# Count the support of 1-itemsets
min_support = 3
item_counts = {}  # Dictionary to store support counts

for transaction in dataset:
    for item in transaction:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

# Find frequent 1-itemsets
frequent_1_itemsets = {item: count for item, count in item_counts.items() if count >= min_support}
print("frequent", frequent_1_itemsets)

# Step 2: Generate Candidate 2-Itemsets
candidate_2_itemsets = []
for item1 in frequent_1_itemsets:
    for item2 in frequent_1_itemsets:
        if item1 != item2:
            candidate_2_itemsets.append({item1, item2})
print("candid", candidate_2_itemsets)

# Step 3: Prune Candidate 2-Itemsets
# Count the support of 2-itemsets and prune those below the minimum support threshold
frequent_2_itemsets = {}
for candidate in candidate_2_itemsets:
    count = 0
    for transaction in dataset:
        if candidate.issubset(transaction):
            count += 1
    if count >= min_support:
        frequent_2_itemsets[frozenset(candidate)] = count
print("frequent_2", frequent_2_itemsets)

# Step 4: Generate Candidate 3-Itemsets
# Generate candidate 3-Itemsets using frequent 2-Itemsets
candidate_3_itemsets = []
for itemset1 in frequent_2_itemsets:
    for itemset2 in frequent_2_itemsets:
        # Join two itemsets if their first (k-1) elements are the same
        if len(itemset1.union(itemset2)) == 3 and len(itemset1.intersection(itemset2)) == 2:
            candidate_3_itemsets.append(itemset1.union(itemset2))
print("can-3", candidate_3_itemsets)

# Step 5: Prune Candidate 3-Itemsets
# Count the support of 3-Itemsets and prune those below the minimum support threshold
frequent_3_itemsets = {}
for candidate in candidate_3_itemsets:
    count = 0
    for transaction in dataset:
        if candidate.issubset(transaction):
            count += 1
    if count >= min_support:
        frequent_3_itemsets[frozenset(candidate)] = count

# Step 7: Generate Association Rules
# Generate Association Rules for 2-Itemsets
association_rules = []

for itemset in frequent_2_itemsets:
    for item in itemset:
        antecedent = itemset - {item}
        support_itemset = frequent_2_itemsets[frozenset(itemset)]
        support_antecedent = frequent_1_itemsets[list(antecedent)[0]]
        confidence = support_itemset / support_antecedent
        association_rules.append((antecedent, {item}, confidence))

# Filter association rules based on a confidence threshold (e.g., 0.5)
min_confidence = 0.5
filtered_rules = [rule for rule in association_rules if rule[2] >= min_confidence]
print(filtered_rules)
