import math
h = int(input("input height: "))
w = int(input("input width: "))
cov = 5
def paint(height = h, width = w):
    area = height*width
    no_can =math.ceil(area/cov)
    print(f"you need {no_can} number of cans to paint the wall.")


paint()