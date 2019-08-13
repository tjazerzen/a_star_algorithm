from helper_functions import calculate_distance, heuristic_value, calculate_connections
import heapq
from copy import deepcopy
# Note: if it isn't possible to get from one point to another, -1 is returned

def shortest_path(coordinates, connection_list, start_point, end_point):

    list_for_calculations = deepcopy(connection_list)
    heuristic_values = heuristic_value(start_point, coordinates)
    connection_distances = calculate_connections(coordinates, list_for_calculations)
    explored = {i: False for i in range(len(connection_list))}
    frontier = []
    first_a_star_score = heuristic_values[start_point]
    heapq.heappush(frontier, (first_a_star_score, 0, start_point, [start_point]))

    while len(frontier) != 0:
        a_score, current_distance, current_point, current_path = heapq.heappop(frontier)
        explored[current_point] = True
        children = connection_list[current_point]

        if current_point == end_point:
            return current_path

        for index in range(len(children)):
            child = children[index]
            new_distance = current_distance + connection_distances[current_point][index]
            new_a_score = new_distance + heuristic_values[child]
            if explored[child] is not True:
                heapq.heappush(frontier, (new_a_score, new_distance, child, current_path + [child]))

    return -1