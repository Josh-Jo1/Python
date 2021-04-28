# Problem C
# Given random numbers between 0 and 1, calculate the value of pi.

from random import uniform

# Method 1
# Since cos(pi) = 1, inverse cos(1) = pi

# from math import acos       # inverse cosine

# pi = 0

# for i in range(1000000):
#     number = -uniform(0,1)

#     if acos(number) > pi:
#         pi = acos(number)

# print(pi)

########################################################################################################################

# Method 2
# After doing some research, I found a way to calculate pi without any other functions (like inverse cos from before).
# Consider: https://www.stealthcopter.com/blog/wp-content/uploads/2009/09/pypi2.png.
# The area of the quarter circle and the square have a pi/4 : 1 ratio.
# Each random point is either in the circle and sqaure (point a in picture) or only the square (point b in picture).
# The number of points inside the circle divided by the total points represents the area of the quarter circle.
# The area calculated multiplied by 4 will yield an approximation for pi.

loops = 1000000
inside = 0

for i in range(loops):
    x = uniform(0,1)
    y = uniform(0,1)

    l = x**2 + y**2     # sqrt not needed since sqrt of number <1 is still <1, which is same for >1
    if l <= 1:
        inside += 1

print(4*inside/loops)
