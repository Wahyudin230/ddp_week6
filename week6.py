(Nomor 1 )
a = 0
while a <= len(numbers):
    if numbers [a] % 2:
        print(numbers[a])
    if numbers[a] == 553:
        break
    a+=1

(Nomor 2)
for b1 in range(1,5):
    for b2 in range(b1):
        print("*", end=" ")
    print()