# Using the  Babylonian method to find approx square root of an integer

def square_root(s):     # where s is an integer

    x0 = s/2            # x0 is an initial guess, where x0< s
    difference = 1      # between first and next estimate
    accuracy = 0.0000001
    if s < 0:
        exit()
    else:

     while difference > accuracy:
          x1 = 0.5 * (x0 + (s / x0))
          difference = (x0 - x1)
          x0 = x1
    return x0


s = float(input("Input an integer of your choice: "))





