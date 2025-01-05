def missing_numbers(n, lista, m, listb):
    count_a = {}
    count_b = {}

    for i in range(n):
        num = lista[i]
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1

    for i in range(m):
        num = listb[i]
        if num in count_b:
            count_b[num] += 1
        else:
            count_b[num] = 1

    missing_numbers = []
    for num in count_b:
        if num not in count_a or count_b[num] > count_a[num]:
            missing_numbers.append(num)

    return sorted(missing_numbers)


n = int(input())
lista = list(map(int, input().split()))

m = int(input())
listb = list(map(int, input().split()))


missing_numbers = missing_numbers(n, lista, m, listb)


print( " ".join(map(str, missing_numbers)))

