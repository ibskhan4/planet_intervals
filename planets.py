# Test cases

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











