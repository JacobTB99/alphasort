#List sorting experiment
#Jacob Beauchamp - 11/1/18

def listscan(list):
    """Scans the given list for unsorted items.
    Takes a list as its parameter
    Returns true if any are unsorted, false if list completely sorted
    """
    n = len(list)  #Assign length of list to variable n
    x = 0  #Position variable. Start at beginning of list
    for rep in range(n - 1):  #Perform scanning operation for length of list. Subtract one due to pairing
        if list[x] > list[x + 1]:  #Compare values of selected index, and that ahead of it, this happens if list out of order
            return True
        elif list[x] <= list[x + 1] and x + 1 < n - 1:  #If values not out of order, move forward, and continue scan
            x = x + 1
        else:  #Base case. Once scan is through, exit
            print(list)
            return False

def shifter(list):
    """Moves to, and finds out-of-order pairs, and reorders
    Accepts a list as a parameter
    """
    #sc1 = "objects "  #Scaffolding message variables. Temporary
    #sc2 = " and "
    #sc3 = " switched"
    #sc4 = " in order"
    n = len(list)  #Assign length of list to variable n
    x = 0  #Start at first position in list
    while listscan(list):
        if list[x] > list[x + 1]:
            t1= list[x]  #Assign both items to a variable, then reinsert in opposite positions
            t2 = list[x + 1]
            list[x + 1] = t1
            list[x] = t2
            #print(sc1 + str(x) + sc2 + str(x + 1) + sc3)
            if x + 1 < n - 1:  #Only when not at end
                x = x + 1 #Move position one more right
            else:  #Base case when unsorted
                x = 0  #Restart Cycle
        else: #If sorted, and more room to right, move over one, leave items in position.
            if x + 1 < n - 1:
                #print(sc1 + str(x) + sc2 + str(x + 1) + sc4)
                x = x + 1
            else:  #Base case. If at end of list, and items in order, leave.
                print(sc1 + str(x) + sc2 + str(x + 1) + sc4)
                x = 0  #Restart cycle
