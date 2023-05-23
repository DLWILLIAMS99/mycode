#!/usr/bin/env python3
# standard shebang

# here is the list that is referenced
my_list = [ "192.168.0.5", 5060, "UP" ]
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# The list is numbered starting with zero
# The 3 print commands combine two strings using a list item and quotes
# print("The first item in the list (IP): " + my_list[0] )
# print("The second item in the list (port): " + str(my_list[1]) )
# print("The last item in the list (state): " + my_list[2] )
print(my_list[0] + " :  " + iplist[3] + " : " + iplist[4] )

