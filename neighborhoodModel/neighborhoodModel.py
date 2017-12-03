import random


## (id, neighbors, state)
## probably better way to do this than manually setting the 60 houses but will work as a test
addresses = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
city = [[0,[58,59,1,2],0],
        [1,[59,0,2,3],0],
        [2,[0,1,3,4],0],
        [3,[1,2,4,5],0],
        [4,[2,3,5,6],0],
        [5,[3,4,6,7],0],
        [6,[4,5,7,8],0],
        [7,[5,6,8,9],0],
        [8,[6,7,9,10],0],
        [9,[7,8,10,11],0],
        [10,[8,9,11,12],0],
        [11,[9,10,12,13],0],
        [12,[10,11,13,14],0],
        [13,[11,12,14,15],0],
        [14,[12,13,15,16],0],
        [15,[13,14,16,17],0],
        [16,[14,15,17,18],0],
        [17,[15,16,18,19],0],
        [18,[16,17,19,20],0],
        [19,[17,18,20,21],0],
        [20,[18,19,21,22],0],
        [21,[19,20,22,23],0],
        [22,[20,21,23,24],0],
        [23,[21,22,24,25],0],
        [24,[22,23,25,26],0],
        [25,[23,24,26,27],0],
        [26,[24,25,27,28],0],
        [27,[25,26,28,29],0],
        [28,[26,27,29,30],0],
        [29,[27,28,30,31],0],
        [30,[28,29,31,32],0],
        [31,[29,30,32,33],0],
        [32,[30,31,33,34],0],
        [33,[31,32,34,35],0],
        [34,[32,33,35,36],0],
        [35,[33,34,36,37],0],
        [36,[34,35,37,38],0],
        [37,[35,36,38,39],0],
        [38,[36,37,39,40],0],
        [39,[37,38,40,41],0],
        [40,[38,39,41,42],0],
        [41,[39,40,42,43],0],
        [42,[40,41,43,44],0],
        [43,[41,42,44,45],0],
        [44,[42,43,45,46],0],
        [45,[43,44,46,47],0],
        [46,[44,45,47,48],0],
        [47,[45,46,48,49],0],
        [48,[46,47,49,50],0],
        [49,[47,48,50,51],0],
        [50,[48,49,51,52],0],
        [51,[49,50,52,53],0],
        [52,[50,51,53,54],0],
        [53,[51,52,54,55],0],
        [54,[52,53,55,56],0],
        [55,[53,54,56,57],0],
        [56,[54,55,57,58],0],
        [57,[55,56,58,59],0],
        [58,[56,57,59,0],0],
        [59,[57,58,0,1],0]]
iterations = 400
printIterations = 20
def init(city,addresses):
    state = []
    for i in range(0,27):
        moveIn = random.choice(addresses)
        addresses.remove(moveIn)
        city[moveIn][2] = 1
    for i in range(0,27):
        moveIn = random.choice(addresses)
        addresses.remove(moveIn)
        city[moveIn][2] = 2
    for i in range(0,60):
        state.append(city[i][2])
    print(state)
    return city
def main(city, addresses):
    ##start of loop
    for i in range(0,401):
        emptyLots = []
        dissatifiedOwners = []
        for x in range(0,60):
            if city[x][2] == 0:
                emptyLots.append(x)
            ## if not means lots full check for dissatified people
            else:
                neighborsValues = []
                occupantValue = city[x][2]
                ## print(occupantValue)
                for values in city[x][1]:
                    ## print(values)
                    neighborsValues.append(city[values][2])
                numOne = 0
                numTwo = 0
                for numValues in neighborsValues:
                    if numValues == 1:
                        numOne += 1
                    if numValues == 2:
                        numTwo += 1
                ##print(numOne)
                ##print(numTwo)
                if (occupantValue == 1 and numOne < 2) or (occupantValue == 2 and numTwo < 2):
                    dissatifiedOwners.append(x)
                    ##print("addes dissastified")
        ##now we have all empty lots and dissatified owners
        ## choose random owner and move to random lot
        if len(dissatifiedOwners) != 0:
            moveOut = random.choice(dissatifiedOwners)
            moveOutType = city[moveOut][2]
            moveInto = random.choice(emptyLots)
            city[moveInto][2] = moveOutType
            city[moveOut][2] = 0
            state = []
            for currentOccupent in range(0,60):
                state.append(city[currentOccupent][2])
            if (i % 20) == 0:
                print(state)
        else:
            state = []
            for currentOccupent in range(0,60):
                state.append(city[currentOccupent][2])
            print(state)
            return state


city = init(city,addresses)
main(city,addresses)

