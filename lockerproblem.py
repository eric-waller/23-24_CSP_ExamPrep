lockers = []
def findperfectsquares(maxx):
def printList():
    for locker in range(1,maxx):
        if lockers[locker] == 1:
            print("Locker" + str(locker) + ":" + str(lockers[locker]))

def swaplocker(locker):
    if lockers[locker] == 0:
        lockers[locker] = 1
    else:
        lockers[locker] = 0

for elem in range(maxx):
    lockers.append(0)
for elem in range(maxx):
    lockers[elem] = 1

for elem in range(maxx):
    if elem % 2 == 0:
        lockers[elem] = 0

for student in range(3,maxx):
    for elem in range(maxx):
        if elem % student == 0:
            swaplocker(elem)

printList()