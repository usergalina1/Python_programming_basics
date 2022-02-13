# break  continue

for i in range(1, 10):
    print(i)  # 1....9

for i in range(1, 10):
    if i == 5:
        break
    print(i)  # 1,2,3,4
print("program exited")

for i in range(1, 10):
    if i == 5:
        continue
    print(i)  # 1,2,3,4,6,7,8,9 (5 is skipped)
print("program exited")

for i in range(1, 10):
    if i == 3 or i == 5 or i == 7:
        continue
    print(i)  # 1,2,4,6,8,9 (3,5,7 are skipped)
print("program exited")

for i in range(3, 7, 2):
    print(i) # 3,5
