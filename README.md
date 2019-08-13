# a_star_algorithm
Implementation of A* algorithm in python

Short description: A* is efficitent graph algorithm, used in quite a few maps, searches and so on. Its main advantage (compared to for example dijkstra algorithm) is that we include "heuristic value" - an approximation of the distance from the current point to the point we're looking for. The main cause of the efficiency of A* is making a greedy choice at each step, selecting f(n) = g(n) + h(n) where g is the cost of path from start node to current node and h is the heuristic value of that node. the minimal f is always chosen. The purpose of g is keeping the cost (fairly) cheap, whereas the mission of h is to keep the path directed towards the goal. Heuristic value must never be higher that actual value.
