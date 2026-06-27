# josephus problem analysis

## 1. problem statement

its developing a system inorder to always find a surviving position no matter the number of people arranged(N) or position of selection(k). it accepts N and K from user and producecs postion in which survivor is located.

## 2. problem understanding

The system is designed to accept N and k from user and ouput the position of surviour.Elemenation starts from first person
and skips k times to elemenate another person . The people are arranged in a circle so counting continues back to the first person after last person on the list.

## 3. input and outputs
 input : N and K
 output : survivour position

## 4. constraints

- arrangement is circle
- N and k muste >= 2

## 5. assumptions

-counting starts at person 1
-counting is done clockwise
-N and k are integers
-invalid inputs are outside of the scope

## 6. Initial Approach (simulation)

I first used direct procedure of elimination simulation becasue it is easy to implement and understand the problem. 

### Algorithm

1. create a list containing people numbered from 1 to N
2. start counting from first person 
3. count k people in circuar manner
4. eliminate K-th person
5. contiue counting from the next remaining person
6. repeat process until only one person remains
7. Return the remaining person's position

### observation 

It correctly solves the problem but  as the number of people increases updating list and position takes more resource and becomes less efficent.

## 7. improved approach(Mathematical Recurrence)

### Motivation 

due to the inefficiency of simulation approach . need to find more mathematical relationship between smaller and larger instances of the problem.

### key observation

if suvivuor for circle of N-1 people is known  then survivuor for N people can be found by adjusting the value by k skip.

### Recurrence problem 

j(1 , k) = 0
j(N , k) = j(j(N-1) + k) mod N

since used zero based indexing 

survivour = j(N , k) + 1 

### algorithm

survivour = 0

for i from 2 to N
     survivour = (survivour + k) mod i

return survivor + 1

## 8. complexity analysis

### simulation approach 

time complexity = O(N^2)
space complexity = O(N)

because it repeatedly removes and updates list of N people and elimination process is done one by one .

### recurrence approach

time complexity = O(N)
space complexity = O(1)

runs only one loop for whole n and have only one variable.

