#!/usr/bin/python
import sys
import numbers
#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():

    a = ""
  
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        

    except ValueError:
        number = False
        print("Please enter a valid number")

    assert isNumber(a)

    if a == 0:
        print ("x = ", -c/b)

    else:

        x1, x2 = find_roots(a, b, c)

        if isinstance(x1, complex) or isinstance(x2, complex):
            
            print("This  is  x1: ", x1)
            print("This  is  x2: ", x2)
        else:
            print ("This is x1: %f" %x1)
            print ("This is x2: %f" %x2)

def find_roots(a,b,c):

    mid = b**2 - 4*a*c

    if mid < 0:
        mid = -mid
        sqrt_mid = mid**(1/2)
        xIm = sqrt_mid / (2*a)
        xReal = -b/(2*a)
        return complex(xReal, xIm), complex(xReal, -xIm)

    else:
        sqrt_mid = mid**(1/2)
        x1 = (-b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
        return x1, x2


def isNumber(x):
    return isinstance(x, numbers.Number)

if __name__=="__main__":
        main()
