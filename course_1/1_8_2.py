X = int(input())
H = int(input())
M = int(input())

bedtime = H * 60 + M

print((bedtime + X) // 60)
print((bedtime + X) % 60)