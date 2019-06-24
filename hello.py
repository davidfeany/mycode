#!/usr/bin/env /usr/bin/python3

# "Hello Tesxas!"
# "Hi Sam, my name is _____.  We are in Texas.  This is day 1."

a = "Hello"
b = "Texas"
c = "Sam"
d = "David"
e = 1

all_l = (a, " ", c, ", ", "my name is ", d, ".  We are in ", b, ".  This is day ", str(e))
print("".join(all_l))

print("{} {}, my name is {}.  We are in {}.  This is day {}.".format(a, c, d, b, e))
print(f"{a} {c}, my name is {d}.  We are in {b}.  This is day {e}.")

