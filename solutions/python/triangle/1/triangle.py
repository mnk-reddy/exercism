def isTriangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if all([a > 0, b > 0 , c > 0]):
        return ((a + b) >= c) and ((b + c) >= a) and ((c + a) >= b)  
    return False
    
def equilateral(sides):
    if isTriangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if isTriangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    return False


def scalene(sides):
    if isTriangle(sides):
        return not isosceles(sides)
    return False