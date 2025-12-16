n = int(input())

a = n // 1000    
b = n % 1000     

s1 = 0
s2 = 0

for i in range(3):
    s1 += b % 10
    b //= 10

    s2 += a % 10
    a //= 10

if s1 == s2:
    print("YES")
else:
    print("NO")