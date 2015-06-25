#!/usr/bin/python
# dijkstras-shortest-path-algorithm in Python
# For help see:
#  http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/

# Node object
# Contains nodes connected in adjacent list
class Node:
    def __init__(self,num):
        self.num = num # nodenumber
        self.adjacent = [] # adjacent nodes
        self.distance = 9999999 # calculated distance

def main():
    # Graph construction
    nodes = [
    Node(0),Node(1),Node(2),Node(3),Node(4),Node(5),Node(6),Node(7),Node(8)
    ]
    # Links / Connections / Arcs + weight
    nodes[0].adjacent = [(nodes[1],4),(nodes[7],8)]
    nodes[1].adjacent = [(nodes[0],4),(nodes[2],8),(nodes[7],11)]
    nodes[2].adjacent = [(nodes[1],8),(nodes[3],7),(nodes[8],2),(nodes[5],4)]
    nodes[3].adjacent = [(nodes[2],7),(nodes[5],14),(nodes[4],9)]
    nodes[4].adjacent = [(nodes[3],9),(nodes[5],10)]
    nodes[5].adjacent = [(nodes[6],2),(nodes[2],4),(nodes[3],14),(nodes[4],10)]
    nodes[6].adjacent = [(nodes[7],1),(nodes[8],6),(nodes[5],2)]
    nodes[7].adjacent = [(nodes[0],8),(nodes[1],11),(nodes[8],7),(nodes[6],1)]
    nodes[8].adjacent = [(nodes[2],2),(nodes[6],6),(nodes[7],7)]

    calculated = []
    endnode = 4

    # Process nodes, start from node 0
    curnode = 0
    nodes[0].distance = 0
    prev = [-1,-1,-1,-1,-1,-1,-1,-1,-1] # shortest path, node numbers


    while not curnode == endnode:
        # Pick closest node calculated distance and NOT in calculated list
        mn = 999999
        curnode = 0
        for n in nodes:
            if n.distance < mn and n.num not in calculated:
                mn = n.distance
                prevnode = curnode
                curnode = n.num

        print "Selected  node: " + str(curnode) + " calculated distance " + str(mn)

        calculated.append(curnode)

        # Through all adjacent nodes
        # update distance in those adjacent nodes where current node distance + adjacent node weight
        # is bigger than adjacents calculated distance
        for ad in nodes[curnode].adjacent:
            nodenum = ad[0].num
            nodeweight = ad[1]

            if (nodes[curnode].distance + nodeweight) < nodes[nodenum].distance:
                nodes[nodenum].distance = nodes[curnode].distance + nodeweight
                # save parent nodenumber where array-index = node distance calculated
                prev[nodenum] = curnode

    # print shortest path
    # start from array index  = endnode -> value is its parent ... so on ....
    print " Shortest path is:"
    path = str(endnode)
    index = endnode

    while not index == 0:
        v = prev[index]
        index = v
        path = str(v) + "-" + path

    print path + " and total distance: " + str(nodes[endnode].distance)

    # **** END OF MAIN *******

if __name__ == "__main__": main()
