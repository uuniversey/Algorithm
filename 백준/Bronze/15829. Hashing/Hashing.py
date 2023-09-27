L = int(input())
my_s = input()
sum_v = 0
for i in range(L):
    sum_v += (ord(my_s[i])-96) * (31**(i))

print(sum_v)