#Rebecca Glatts
#Project 1 Task 2


import random
import math

#changes the random seed each time the program runs, just replace n
n = 5   
random.seed(n)

#gets number of darts from user
numDarts = int(input("Please enter how many Darts you'd use: "))
inCircle = 0

#for loop that loop for number of darts
for i in range (numDarts) :
    #decides a random x and y point for each dart
    x=random.random()
    y=random.random()

    #calculates how far away the dart is from the center of the circle
    distance = math.sqrt(x**2+y**2)

    #if the distance is smaller than or equal to the radius (1) then it adds the dart to a counter that counts
    #how many total darts are in the circle
    if distance <= 1:
        inCircle += 1
#creates a ratio of the number of darts inside the circle to the total multiplied by 4
#which estimates the value of pi
pi = inCircle / numDarts * 4
print(pi)

"""
Intermediate results: 

Please enter how many Darts you'd use: 10
3.2

Please enter how many Darts you'd use: 1000
3.132

Please enter how many Darts you'd use: 10000000
3.1407744

Final result: 

Please enter how many Darts you'd use: 100000000
3.14178318


"""