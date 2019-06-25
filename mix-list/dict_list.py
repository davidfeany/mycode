#!/usr/bin/env python3

def main():
    hosts = [
            {"server": "North", "ip": "10.1.2.3"},
            {"server": "South", "ip": "10.4.5.6"},
            {"server": "West",  "ip": "10.7.8.9"}
            ]
    
    hosts.append( {"server": "East",  "ip": "10.10.11.12"})
    #hosts.append( {"server": input("Enter location:"),  "ip": input("Enter IP:")})
    
    print_servers(hosts)


def print_servers(hostlist):
    for location in hostlist:
        #print(location["server"])
        #print(location["ip"])
        #print(f'Server Location:  {location["server"]}\nIP:  {location["ip"]}\n\n')
        print('Server Location:  {}\nIP:               {}\n\n'.format(location["server"], location["ip"]))



main()


