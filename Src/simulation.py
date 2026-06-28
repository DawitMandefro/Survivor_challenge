def josephus_simulation(n, k):
    people = list(range(1, n + 1))
    current_index = 0

    while len(people) > 1:
        current_index = (current_index + k - 1) % len(people)
        eliminated = people.pop(current_index)
        print(f"Eliminated: {eliminated}")

    return people[0]
