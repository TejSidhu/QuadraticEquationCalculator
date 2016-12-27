import random
import math
import Ans1_Ans2

x = 0
while x < 1001:
    a_array = {}  # Stores random values
    b_array = {}
    c_array = {}

    a = int(random.randrange(1, 1000))
    b = int(random.randrange(1, 1000))
    c = int(random.randrange(1, 1000))

    if c < 0 & a < 0:
        continue
    elif b ** 2 < a * c * 4:
        continue

    x += 1

    print(x)  # keeps track of how many correct calculations have been made
    print(Ans1_Ans2.Answer1(a, b, c))
    print(Ans1_Ans2.Answer2(a, b, c))
    print(a, b, c)
    print('(x ' + str(Ans1_Ans2.Answer1(a, b, c)) + ')(x ' + str(Ans1_Ans2.Answer2(a, b, c)) + ')')
    # Writes to the txt file
    file_write = open('Equations.csv', 'a')
    file_write.write(
        '\n' + str(Ans1_Ans2.Answer1(a, b, c)) + ',' + str(Ans1_Ans2.Answer2(a, b, c)) + ',(' + str(a) + ' ' + str(
            b) + ' ' + str(c) + ')' + '(x ' + str(Ans1_Ans2.Answer1(a, b, c)) + ')(x ' + str(
            Ans1_Ans2.Answer2(a, b, c)) + ')')
    file_write.close()
