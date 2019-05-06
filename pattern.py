import math
import random
import sys
import time
start = time. time()
n = int(input("please enter and even number greater than 2"))
if(n == 2 or n % 2 != 0):
    print("please enter and even number greater than 2")
    sys.exit()
else:
    arr = [[random.randrange(20) for i in range(n)] for j in range(n)]

print(arr)
print("\nanswer")


def set_cordinates():
    global x1, y1, x2, y2, x3, y3, x4, y4

    x1 = math.ceil(n/4)
    y1 = x1

    x2 = x1
    y2 = y1 + 1

    x3 = x1 + 1
    y3 = y1 + 1

    x4 = x1 + 1
    y4 = y1


def print_diagnol(x1, y1, x2, y2, x3, y3, x4, y4):
    i = x1
    j = y1
    while(i >= 0 and j >= 0):
        print(arr[i][j])
        i -= 1
        j -= 1
    i = x2
    j = y2
    while(i >= 0 and j >= 0 and i < n and j < n):
        print(arr[i][j])
        i -= 1
        j += 1
    i = x3
    j = y3
    while(i >= 0 and j >= 0 and i < n and j < n):
        print(arr[i][j])
        i += 1
        j += 1
    i = x4
    j = y4
    while(i >= 0 and j >= 0 and i < n and j < n):
        print(arr[i][j])
        i += 1
        j -= 1


set_cordinates()
upper_arr_count = math.floor(n/2)
while(upper_arr_count):
    print("Upper matrix", upper_arr_count)
    print_diagnol(x1, y1, x2, y2, x3, y3, x4, y4)
    x1 -= 1
    y2 += 1
    x3 += 1
    y4 -= 1
    upper_arr_count -= 1

set_cordinates()
y1 -= 1
x2 -= 1
y3 += 1
x4 += 1
lower_arr_count = math.floor(n/2)-1
while(lower_arr_count):
    print("Lower matrix", lower_arr_count)
    print_diagnol(x1, y1, x2, y2, x3, y3, x4, y4)
    y1 -= 1
    x2 -= 1
    y3 += 1
    x4 += 1
    lower_arr_count -= 1

end = time. time()
print("Execution Time:", end - start)
