def circle_check(BF_map, current, counter):
    print(current)
    first = current[0]
    last = current[-1]
    if BF_map[first] == last or BF_map[last] == first:
        return current
    #if BF_map[first] == last and counter:
    #    return current
    #elif BF_map[last] == first and not counter:
    #    return current
    currents = {}
    currents.setdefault(first, [x for x in current if x != first])
    currents.setdefault(last, [x for x in current if x != last])
    circle_check(BF_map, currents[first], counter)
    circle_check(BF_map, currents[last], counter)
    return max(currents.values(), key=len)

def BFtree(BF_map, current, reverse=False):
    if reverse:
        current = current[::-1]
    possible = [x for x in BF_map.keys() if BF_map[x]==current[-1] and x not in current]
    if len(possible) == 0:
        if reverse:
            return False, current[::-1]
        else:
            return False, current
    currents = {}
    for p in possible:
        currents.setdefault(p, [x for x in current])
        currents[p][len(current):] = [p]
    for cur in currents.keys():
        if BF_map[cur] not in currents[cur]:
            currents[cur].append(BF_map[cur])
        else:
            currents[cur] = BFtree(BF_map, currents[cur])
    if reverse:
        return True, max(currents.values(), key=len)[::-1]
    else:
        return True, max(currents.values(), key=len)

def MainMethod(serials):
    BF_map = {(i+1):serials[i] for i in range(len(serials))}
    circles = []
    done = set()
    idx = 1
    while idx < len(serials)+1:
        circle = [idx, BF_map[idx]]
        while 1:
            idx = BF_map[idx]
            if BF_map[idx] not in circle:
                circle.append(BF_map[idx])
            else:
                counter, circle = BFtree(BF_map, circle)
                counter, circle = BFtree(BF_map, circle, True)
                circle = circle_check(BF_map, circle, counter)
                circles.append(circle)
                done = done.union(set(circle))
                break
        idx = len(serials)+1
        for i in range(len(serials)):
            if i+1 not in done:
                idx = i+1
                break
    print(max(circles, key=len))
    return len(max(circles, key=len))

import sys
# transfer TestCase from file to input suitable for the function
TestCase = []
testname = sys.argv[1]
test_file = open(testname, "r")
n = 0
for line in test_file:
    if n == 0:
        n = int(line)
        now_idx = 0
    else:
        if now_idx == 0:
            now_idx += 1
            continue
        TestCase.append([int(x) for x in line.split()])
        now_idx = 0
test_file.close()
# start 
output = ""
for i in range(n):
    test = TestCase[i]
    print(i+1)
    outputline = "Case #" + str(i+1) + ": " + str(MainMethod(test))
    output = output + outputline + "\n"
outname = testname.replace("in", "out")
output_file = open(outname, 'w');
output_file.write(output)
output_file.close()

