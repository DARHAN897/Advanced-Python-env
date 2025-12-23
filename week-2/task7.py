purchases = "apple banana apple orange banana apple milk"
items = purchases.split()

counts = {}
for item in items:
    if item in counts:
        counts[item] = counts[item] + 1
    else:
        counts[item] = 1

print("Purchase frequency:")
for item in counts:
    print(item + ":", counts[item])

max_count = 0
most_popular = ""
for item in counts:
    if counts[item] > max_count:
        max_count = counts[item]
        most_popular = item
print("Most popular item:", most_popular)

print("Purchased once:", end=" ")
for item in counts:
    if counts[item] == 1:
        print(item, end=" ")
print()

pairs = []
for item in counts:
    pairs.append([item, counts[item]])

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[j][1] > pairs[i][1]:
            temp = pairs[i]
            pairs[i] = pairs[j]
            pairs[j] = temp

print("Sorted by frequency:")
for pair in pairs:
    print(pair[0], pair[1])