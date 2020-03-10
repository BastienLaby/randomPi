import random

'''
Given one only function random.random() which produces a uniformly generated number, calculate PI.

Circle area of radius 1 : C = PI * r^2 = PI
Area of a square of size 2 : S = (2 * r)^2 = 4
Generate X 2D points (x, y) with both x and y in [0, 1]
Finally, C / S = number of points in the circle / number of points in the square.
'''

def estimatePi(iterations):
    pi = 0
    circlePointsCount = 0
    for i in range(iterations):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1: # no need to sqrt() because if x < 1, sqrt(x) < 1 and if x > 1, sqrt(x) > 1
            circlePointsCount += 1
    return 4 * circlePointsCount / iterations


print(estimatePi(100))
print(estimatePi(1000))
print(estimatePi(10000))
print(estimatePi(100000))
print(estimatePi(1000000))
print(estimatePi(10000000))
