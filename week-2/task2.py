a = input()
b = input()

k = len(b)
bb = b + b
count = 0

for i in range(len(a) - k + 1):
    sub = a[i:i + k]
    if sub in bb:
        count += 1

print(count)