# ---------------------------------- #
#     COMP20O2 PROGRAMMING TASKS     #
#                                    #
#     WEEK 1, TASK 2 - FIBONACCI     #
#                                    #
#        STARTED 7TH FEB 2023        #
#       COMPLETED 7TH FEB 2023       #
# ---------------------------------- #

def fibonacci(number1, number2, o):
    number3 = number1 + number2
    print(number3)
    o = o + 1
    if o < 8:
        fibonacci(number2, number3, o)


print(0)
print(1)

fibonacci(0, 1, 0)
