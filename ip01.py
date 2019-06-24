#!/usr/bin/env python3
ip_l = [
        "10.10.10.25",
        "10.20.30.40",
        "10.10.24.47"
        ]

print("I need to access IP's {}, {}, and {}".format(ip_l[0],ip_l[1],ip_l[2]))
print('my_list = ["{}", "{}", "{}"]'.format(ip_l[0],ip_l[2],ip_l[1]))
print('my_list = ["{0}", "{2}", "{1}"]'.format(*ip_l))

