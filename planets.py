# A spaceship is approaching some planets that are arranged in a 1-dimensional line. It needs to pass through the line of the planets, but can't get too close to any planet, otherwise it would get caught in that
# planet's gravitational field.
# Given a list of planets, where each planet is specified by its position along the line and the range of its gravitational field, compute the list of gaps from [0, 1000] through which the spaceship can fly.



# input                output (gaps)           reasoning
# [location, orbit]
# [3,2]                [0,1],[5,1000]          The field covers [1,5].
# [3,2],[5,1]          [0,1],[6,1000]          The fields cover [1,5] and [4,6].
# [2,1],[5,1]          [0,1],[3,4],[6,1000]    The fields cover [1,3] and [4,6].
# [2,2],[7,1],[4,1]    [5,6],[8,1000]          The fields cover [0,4], [6,8], and [3,5].

input = [[2,2],[7,1],[4,1]]
input2 = [[3,3],[5,1],[990,15]]

def gaps(planets):
    # Create the intervals of planets
    intervals = []
    for planet in planets:
        center, side = planet
        intervals.append([center-side, center+side])

    # Sort the planets and merge them. Use new array. Iterate through intervals and compare with
    # top element of new array. If subsequent, append interval. If not, simply change the values
    # of the topmost interval.
    intervals.sort(key = lambda x : x[0])
    print(f"The sorted intervals are {intervals}")
    final = [intervals[0]]

    for i in range(1,len(intervals)):
        prev, next = final[-1], intervals[i]
        if next[0] > prev[1]:
            final.append(next)
        else:
            final[-1] = [min(prev[0],next[0]), max(prev[1],next[1])]
    print(f"The merged intervals are {final}")

    # Construct the gaps array of intervals.
    res = []
    if final[0][0] > 0:
        res.append([0,final[0][0]])
    for i in range(len(final) - 1):
        prev_start, prev_end = final[i]
        next_start, next_end = final[i+1]
        res.append([prev_end, next_start])
    if final[-1][1] < 1000:
        res.append([final[-1][1], 1000])
    else:
        res[-1][1] = 1000

    print(f"The gaps in between planets are {res}")

#gaps(input2)




hand = ['10H','QC','4S', 'QS']
def order(cards):
    cardVals = { str(i): i for i in range(2,11) }
    cardVals['J'] = 11
    cardVals['Q'] = 12
    cardVals['K'] = 13
    cardVals['A'] = 14

    suitVals = {
        'S': 4,
        'C': 3,
        'H': 2,
        'D': 1
    }
    val, suit = cards[:-1], cards[-1]
    print(val, suit)
    return (cardVals[val], suitVals[suit])

def arrangeHand(hand):
    hand.sort(key = order, reverse = True)
    print(hand)

arrangeHand(hand)









