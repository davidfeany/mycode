#!/usr/bin/env python3
first_list=["eggs", "bacon", "milk", "butter", "bread", "cheddar", 5, 2.75]
print(first_list)

# identify
ctr=0
for item in first_list:
    print("{: 3}>  {: >10}   {}".format(ctr, item, type(item)))
    ctr += 1

print("\nI need to get {}, {}, {}, {}, {}, and {} before {}.  It will be more than ${}.\n\n".format(*first_list))

second_list = (input("First user input:  "), input("Second user input: "))
print("\n\nNew list created is:  ", second_list, "\n")


