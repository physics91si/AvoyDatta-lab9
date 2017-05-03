import sys
import numbers
def convertIfNumber(x):
    try:
        return int(x)
    except:
        return x
    return x
def isNumber(x):
    return isinstance(x, numbers.Number)
# I CAN SEE YOU!!!!!!!
##############################################
############### Docstrings!!! ################
##############################################

# Use:
# Documenting code to easily know what each function
# 
#def func(x,y,j=True):
#    """What is this?
#    This is a second line"""
#    return x+y
#
#print(func(5,6))

##############################################
### Did someone say they do not make bugs? ###
##############################################
#x=0
#while x<5
#    print('Hello world')
#    x+=1

##############################################
############ Give. Me. Infinity. #############
##############################################
#infty = 1/0

##############################################
################# But my X? ##################
##############################################
#print(X)

##############################################
############# Remember classes? ##############
##############################################
#class Complex:
#    def __init__(self, realpart, imagpart):
#        self.r = realpart
#        self.i = imagpart
#
#x = Complex(3.0, -4.5)
#print(x.r, x.i)

##############################################
#### I mean, can't you just concatenate? #####
##############################################
#print("I'm " + str(19) + " years old")

##############################################
########### I want the solutions #############
##############################################
#import solutions

##############################################
##### Is that all? Can I break it more? ######
##############################################
#https://docs.python.org/3/library/exceptions.html#bltin-exceptions

##############################################
# Maybe you want something like checkpoints? #
##############################################
#maybeANumber = convertIfNumber(input("Please enter a number: "))
#assert isNumber(maybeANumber), "Nope that's not a number. Break"
#print("success!")

##############################################
## That's not fun! Give user another chance ##
##############################################
while True:
    try:
        x = int(input("Please enter a number: "))
        print("success!")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print("Unexpected exception")