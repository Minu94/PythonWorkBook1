list1 = [3, 4, 7, 8]
list2 = []
for j in range(0, 4):
    k = 1
    while (k <= 3) & (j != k):
        a = list1[j] + list1[k]
        list2.append(a)
        k += 1
print(list2[::-1])

