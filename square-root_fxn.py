# Using the  Babylonian method to find approx square root of an integer
# Xn+1 = 0.5 * (Xn + (s/Xn))

def square_root(s):     # where s could be any integer

    x0 = s/2            # x0 is an initial guess which is closest to the sqrt of s. in this case x0 = half of s
    difference = 1     # difference between the first and next value
    accuracy = 0.0000001
    if s > 0:           # in this case we have s as a positive integer

        while difference > accuracy:   # the loop get values of x until the difference <= accuracy
            x1 = 0.5 * (x0 + (s / x0))
            difference = (x0 - x1)   # Also this tells the program when to stop... almost like a stopping condition
            x0 = x1
            return x0

    elif s == 0:    # in the case where s = 0
        exit("result = 0")

    else:               # -s == (-1 * n) in the case where s is negative, sqrt(-s) = sqrt(-1)* sqrt(n)
                                             # from our knowledge of complex numbers sqrt(-1) = i
         n = float(input("positive part: "))  # Also n is |-s|
         x0 = n / 2

         while difference > accuracy:
             x1 = 0.5 * (x0 + (n / x0))
             difference = (x0 - x1)
             x0 = x1

             result = f"{x0}i"      # the f string substitute the variable x0 with its actual value
         return result

s = float(input("Input an integer of your choice: "))





