def reverse(a: list[str]) -> list[str]:
    i = 0
    while i < len(a) / 2:
        temp = a[i]
        a[i] = a[len(a) - 1 - i]
        a[len(a) - 1 - i] = temp
        i += 1
    return a

