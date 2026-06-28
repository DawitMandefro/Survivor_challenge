from simulation import josephus_simulation
from recurrence import josephus_recursive


def main():
    while True:
        print("\n===== Josephus Survivor Problem =====")
        print("1. Simulation Approach")
        print("2. Recursive Approach")
        print("3. Exit")

        choice = input("Choose an approach: ")

        if choice == "3":
            print("Goodbye!")
            break

        if choice not in ("1", "2"):
            print("Invalid choice.")
            continue

        n = int(input("Enter number of people (N): "))
        k = int(input("Enter skip value (K): "))

        if n <= 0 or k <= 0:
            print("N and K must be positive integers.")
            continue

        if choice == "1":
            survivor = josephus_simulation(n, k)
            print(f"\nSurvivor: {survivor}")

        else:
            survivor = josephus_recursive(n, k)
            print(f"\nSurvivor: {survivor}")

        again = input("\nDo you want to try again? (y/n): ").lower()

        if again != "y":
            print("Thank you for using the program.")
            break


if __name__ == "__main__":
    main()
