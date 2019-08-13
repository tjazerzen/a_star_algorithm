# a_star_algorithm
Implementation of A* algorithm in python

Short description: A* is efficitent graph algorithm, used in quite a few maps, searches and so on. Its main advantage (compared to for example dijkstra algorithm) is that we include "heuristic value" - an approximation of the distance from the current point to the point we're looking for. The main cause of the efficiency of A* is making a greedy choice at each step, selecting f(n) = g(n) + h(n) where g is the cost of path from start node to current node and h is the heuristic value of that node. the minimal f is always chosen. The purpose of g is keeping the cost (fairly) cheap, whereas the mission of h is to keep the path directed towards the goal. Heuristic value must never be higher that actual value.

The entire map is split into 3 zones: explored zone, frontier and unexplored zone. When a node in a graph is first seen is appended into the frontier. That node is popped out when its f(n) value is minimal, frontier list is implemented with priority queue. When an item is popped out of frontier, it is appended into the explored list (or dictionary in my case). After that, all neighbours of the explored node are put into frontier priority queue and process repeats until we either find the cheapest path to the node (when we've explored the end node) or we run out of possible nodes to explore meaning there's no path to the node. In this case, the function returns -1.

My repository consists of 5 files:
- Helper functions: Few functions where heuristic distance values between to adjacent nodes are calculated
- a_star_algorithm: The core of this repository, shortest path is calculated here and the list of path returned
- intersections.txt: a text file with the information of node possition in coordinate system. The map is made out of 40 nodes (I mark them 0-39) and each of those nodes has x and y coordinates written in its own line. 1 is the maximum value of this coordinate system
- adjacency_list.txt: Similar to intersections.txt, there's 40 lines in text file but this time each line holds the information of the node's adjacent nodes - for example, if there are numbers 32, 16 and 14 in the line 6 of this text file, the adjacent nodes of node 6 are nodes 32, 16, 14.
- test_file: some automated testing provided for easier use of this program
