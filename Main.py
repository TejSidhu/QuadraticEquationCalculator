import random
import math
def random():
    return int(random.randrange(1,20))


a_array = {} #Stores random values
b_array = {}
c_array = {}
def Main():
    local_a = random()
    local_b = random()
    local_c = random()

    if local_c < 0 & local_a < 0:
        print("there was an error")
        Main()
    elif local_b**2 < local_a*local_c*4:
        print("there was an erorr")
        Main()
    else:
        Answer1(local_a, local_c, local_b)
        Answer2(local_a, local_c, local_b)
    Answer1()
    Answer2()




def Answer1(a,b,c):
    part1 = math.sqrt((b ** 2 - (4 * a * c)))
    part2 = -b + part1
    part3 = (part2/(2*a))
    print(part3)

def Answer2(a,b,c):
    part1 = math.sqrt((b ** 2 - (4 * a * c)))
    part2 = -b - part1
    part3 = (part2/(2*a))
    print(part3)
