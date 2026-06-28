
def josephus_recursive(n, k):
    if n == 1:
        return 1

    return (josephus_recursive(n - 1, k) + k - 1) % n + 1
