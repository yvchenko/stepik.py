A, B, H = int(input()), int(input()), int(input())

if A > B:
    print("Некорректно введены условия")
elif A <= H <= B:
    print("Это нормально")
elif H > B:
    print("Пересып")
else:
    print("Недосып")