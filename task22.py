print ("Введите множество 1")
mn1 = set(input().split())
print ("Введите множество 2")
mn2 = set(input().split())
mn3=mn1.intersection(mn2)

print(f"Множество 1 и 2 пересекаются в значениях {sorted(mn3)}")