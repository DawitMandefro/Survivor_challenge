# josephus simulation implementation


def josephus_simulation(n, k) :

# create list of people 
    people = list(range(1, n + 1))

# start counting from the first person
    current_index = 0

# continue until only one person is left    
    while len(people) > 1:  

        # find the index of the person to be eliminated
        current_index = (current_index + k - 1) % len(people)

        # eliminate the person
        eliminated = people.pop(current_index)   

        # display elimination order
        print(f"Eliminated: {eliminated}")   

    # return the last remaining person  
    return people[0];   

#get input from user

n = int(input("Enter the number of people(N): "))
k = int(input("Enter the skip value(K): "))   

#validate input

if n < 1 or k < 1:
    print("N and k must be positive integers")
else:
 survivor = josephus_simulation(n, k)
 print(f"\nSurvivor: {survivor}") 
