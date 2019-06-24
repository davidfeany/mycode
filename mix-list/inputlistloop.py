#!/usr/bin/env python3

def main():
    # Read in list data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip:
            # append adds to the end of list
            # rstrip removes special chars on right of string
            # split breaks string into list
            # result is a list of driver and IP
            networklists.append(sline.rstrip("\n").split(' '))

    print(networklists)

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()


