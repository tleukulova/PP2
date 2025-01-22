#Write a function that computes the volume of a sphere given its radius.
import math
def compute_volume(radius):
    volume = 4/3 * math.pi * pow(radius, 3)
    return volume

radius = int(input())
print(compute_volume(radius))