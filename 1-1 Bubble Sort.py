# ---------------------------------- #
#     COMP20O2 PROGRAMMING TASKS     #
#                                    #
#    WEEK 1, TASK 1 - BUBBLE SORT    #
#                                    #
#        STARTED 7TH FEB 2023        #
#       COMPLETED 7TH FEB 2023       #
# ---------------------------------- #

def bubblesort(nlist):
    for passnum in range(len(nlist) - 1, 0, -1):  # in range of the list
        for i in range(passnum):  # if i is in the range that passum is in
            if nlist[i] > nlist[i + 1]:  # if n list i is greater than n list i+1
                temp = nlist[i]  # temp number to make sure previous one is saved
                nlist[i] = nlist[i + 1]  # This will overide with the next number in the list
                nlist[i + 1] = temp  # Stores the number you store in temp in list


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubblesort(nlist)
print(nlist)
