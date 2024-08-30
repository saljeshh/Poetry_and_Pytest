PI = 3.14


def area_of_circle(radius: float) -> float:
    """
    area_of_circle calculate area of circle

    Args:
        radius: radius of the circle
    
    Returns:
        area 
    
    Examples:
        >>> area_of_circle(1)
        3.14
        >>> area_of_circle(2)
        12.56

    """
    return multiply(PI, radius**2)
    #return PI * radius ** 2


def multiply(x, y): 
    return x * y


if __name__ == '__main__':
    radius = float(input("Enter the radius of circle"))
    area = area_of_circle(5.6)
    print("Area is " + area)