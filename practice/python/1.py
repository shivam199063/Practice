# import os
# import sys
# l=dir(os)
# ll=sys.path
# print(ll)
# import sys
# print(sys.executable)

# import threading

# def s():
#     print("shivam")
    
# def ss():
#     print("saini")

import sys

# a =10
a=3
a=9
# a=
c= 10
# b=a
# c=a
print(sys.getrefcount(c))
for i in range(9):
    a=c+1
    print(sys.getrefcount(c))




