from math import pi

#finds area of circle
def circle_area(r):
    #checks parameters is correct data type and that the numbers are greater than 0
    if isinstance(r, (int, float)) and r > 0:
        #returns the calculated area
        return pi * (r ** 2)
    #if parameters are invalid raise an error message
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

#finds area of a trapezium
def trapezium_area(a, b, h):
    #checks parameters is correct data type
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(h, (int, float)):
        #checks parameters are greater than 0
        if a > 0 and b > 0 and h > 0:
            #returns the calculated area
            return 0.5 * (a + b) * h
        #raises error if parameters do not pass error checks
        else:
            raise ValueError("One of the values given is a negative number.")
    else:
        raise ValueError("All inputs must be numeric (int or float).")
#finds area of an ellipse
def ellipse_area(a, b):
    #checks parameters is correct data type
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        #checks parameters are greater than 0
        if a > 0 and b > 0 : 
            #returns the calculated area
            return pi * a * b
        #raises error if parameters do not pass error checks
        else:
            raise ValueError("Negative value given, positive values only.")
    else:
        raise ValueError("Invalid entry given")
    
  
#finds the area of a rhombus
def rhombus_area(d1, d2):
    #checks parameters is correct data type
    if isinstance(d1,(int,float)) and isinstance(d2,(int,float)):
        #checks parameters are greater than 0
        if d1 > 0 and d2 > 0:
            #returns the calculated area
            return 0.5 * d1 * d2
        #raises error if parameters do not pass error checks
        else:
            raise ValueError("Positive values only.")
    else:
        raise ValueError("Invalid entry given.")
    